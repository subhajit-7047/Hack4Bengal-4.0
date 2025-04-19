import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import joblib

# Load your dataset
df = pd.read_csv("mental_health_dataset.csv")

# Drop ID column if exists
if 'ID' in df.columns:
    df.drop(columns=['ID'], inplace=True)

diagnoses = ['Depression', 'Anxiety', 'OCD', 'PTSD', 'Bipolar', 'Insomnia', 'ADHD', 'Autism']
categorical_cols = ['Gender', 'Sadness_Level', 'Interest_Loss', 'Fatigue_Level', 'Mood_Swings',
                    'Guilt_or_Worthlessness', 'Worry_Level', 'Restlessness', 'Panic_Attacks',
                    'Concentration_Difficulty', 'Obsessions', 'Compulsions', 'Trauma_History',
                    'Flashbacks', 'Nightmares', 'Avoidance_Behavior', 'Manic_Episodes',
                    'Impulsivity', 'Hyperactivity', 'Task_Completion', 'Social_Communication',
                    'Eye_Contact', 'Special_Interests', 'Routine_Rigidity', 'Sensory_Issues']
numerical_cols = ['Age', 'Attention_Span', 'Sleep_Hours'] # Identify numerical columns

# Impute missing values BEFORE encoding and scaling
imputer_categorical = SimpleImputer(strategy='most_frequent')
df[categorical_cols] = imputer_categorical.fit_transform(df[categorical_cols])

imputer_numerical = SimpleImputer(strategy='mean')
df[numerical_cols] = imputer_numerical.fit_transform(df[numerical_cols])

# Fit LabelEncoders and save them
label_encoders = {}
for column in categorical_cols:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le
joblib.dump(label_encoders, 'label_encoders.pkl')

# Scale numerical features and save the scaler
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
joblib.dump(scaler, 'feature_scaler.pkl')

X = df.drop(columns=diagnoses)
y = df[diagnoses]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultiOutputClassifier(RandomForestClassifier(random_state=42))
model.fit(X_train, y_train)
joblib.dump(model, 'mental_health_model.pkl')
joblib.dump(X.columns, 'features.pkl')