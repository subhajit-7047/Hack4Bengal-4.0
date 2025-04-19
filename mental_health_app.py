import streamlit as st
import pandas as pd
import joblib
import io
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from sklearn.impute import SimpleImputer

# Load model and features
model = joblib.load("mental_health_model.pkl")
features = joblib.load("features.pkl")

diagnoses = ['Depression', 'Anxiety', 'OCD', 'PTSD', 'Bipolar', 'Insomnia', 'ADHD', 'Autism']

# Page config
st.set_page_config(page_title="Mental Health Predictor", page_icon="🧠", layout="centered")

# Custom CSS Styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        font-family: 'Poppins', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        color: #000000;
    }
    .title {
        font-size: 50px;
        font-weight: 900;
        color: #ffffff;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.4);
    }
    .form-card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0px 4px 30px rgba(0, 0, 0, 0.2);
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea, #764ba2);
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.5rem;
        color: white;
        font-weight: 600;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #43cea2, #185a9d);
        transform: scale(1.05);
    }
    .risk {
        font-size: 22px;
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        color: white;
        margin-top: 20px;
    }
    .low {background-color: #28a745;}
    .medium {background-color: #ffc107; color: black;}
    .high {background-color: #dc3545;}
    .footer {
        margin-top: 50px;
        font-size: 14px;
        text-align: center;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🧠 Mental Health Disease Predictor</div>", unsafe_allow_html=True)

st.markdown("<div class='form-card'>", unsafe_allow_html=True)

# Input Form
input_data = {}
with st.form("mental_health_form"):
    for feature in features:
        if "Level" in feature or feature in ["Task_Completion", "Social_Communication"]:
            input_data[feature] = st.selectbox(f"{feature}", ['Low', 'Medium', 'High'])
        elif feature in ['Gender']:
            input_data[feature] = st.selectbox(f"{feature}", ['Male', 'Female', 'Other'])
        elif feature in ['Age', 'Attention_Span', 'Sleep_Hours']:
            input_data[feature] = st.number_input(f"{feature}", min_value=0.0)
        else:
            input_data[feature] = st.selectbox(f"{feature}", ['Yes', 'No'])

    submitted = st.form_submit_button("🔍 Predict Now")

st.markdown("</div>", unsafe_allow_html=True)

# Prediction Logic
if submitted:
    input_df = pd.DataFrame([input_data])

    # Handle missing values using SimpleImputer
    imputer = SimpleImputer(strategy="most_frequent")
    input_df = pd.DataFrame(imputer.fit_transform(input_df), columns=input_df.columns)

    # Encode categorical features
    for col in input_df.columns:
        if input_df[col].dtype == 'object':
            le = LabelEncoder()
            input_df[col] = le.fit_transform(input_df[col])

    try:
        predictions = model.predict(input_df)  # Removed [0] here
        probs = model.predict_proba(input_df)

        result = []
        confidence_scores = {}

        for i, disease in enumerate(diagnoses):
            if predictions[0][i] == 1: # Still using [0] because predict returns one row
                try:
                    confidence = round(probs[0][i][1] * 100, 2) # Accessing probabilities correctly
                except:
                    confidence = 50.0  # fallback
                result.append(disease)
                confidence_scores[disease] = confidence

        if result:
            st.markdown("### 🗞 *Detected Conditions:*")
            for d in result:
                st.success(f"🧠 {d} - {confidence_scores[d]}% confidence")

            if len(result) <= 2:
                st.markdown("<div class='risk low'>🟢 Low Risk</div>", unsafe_allow_html=True)
            elif len(result) <= 5:
                st.markdown("<div class='risk medium'>🟡 Moderate Risk</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='risk high'>🔴 High Risk</div>", unsafe_allow_html=True)

            # Confidence Chart
            st.markdown("### 📊 *Prediction Confidence Chart:*")
            fig, ax = plt.subplots()
            sorted_items = dict(sorted(confidence_scores.items(), key=lambda x: x[1], reverse=True))
            ax.bar(sorted_items.keys(), sorted_items.values(), color='#6a11cb')
            plt.xticks(rotation=45)
            plt.ylabel("Confidence (%)")
            plt.ylim(0, 100)
            st.pyplot(fig)

            # PDF Report Generation
            buffer = io.BytesIO()
            c = canvas.Canvas(buffer, pagesize=A4)
            width, height = A4

            c.setFont("Helvetica-Bold", 18)
            c.drawString(50, height - 50, "🧠 Mental Health Assessment Report")

            c.setFont("Helvetica", 12)
            c.drawString(50, height - 90, f"Age: {input_data['Age']}")
            c.drawString(200, height - 90, f"Gender: {input_data['Gender']}")

            c.drawString(50, height - 120, "Symptoms and Responses:")
            y = height - 140
            for key, value in input_data.items():
                if y < 100:
                    c.showPage()
                    y = height - 50
                c.drawString(70, y, f"{key}: {value}")
                y -= 20

            c.setFont("Helvetica-Bold", 14)
            y -= 30
            c.drawString(50, y, "🗞 Predicted Conditions:")
            y -= 20
            c.setFont("Helvetica", 12)
            for d in result:
                c.drawString(70, y, f"{d} - {confidence_scores[d]}%")
                y -= 20

            y -= 10
            risk = "Low Risk" if len(result) <= 2 else "Moderate Risk" if len(result) <= 5 else "High Risk"
            risk_color = colors.green if risk == "Low Risk" else colors.orange if risk == "Moderate Risk" else colors.red
            c.setFillColor(risk_color)
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, y, f"🫪 Risk Level: {risk}")
            c.setFillColor(colors.black)

            c.showPage()
            c.save()
            buffer.seek(0)

            st.download_button(
                label="📅 Download PDF Report",
                data=buffer,
                file_name="mental_health_report.pdf",
                mime="application/pdf"
            )
        else:
            st.info("✅ No strong indication of mental health issues detected.")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")