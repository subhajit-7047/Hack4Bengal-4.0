import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
import joblib

# Load dataset
df = pd.read_csv("mental_health_dataset.csv")

# Define diagnosis columns
diagnoses = ['Depression', 'Anxiety', 'OCD', 'PTSD', 'Bipolar', 'Insomnia', 'ADHD', 'Autism']

# Drop ID column
df.drop(columns=['ID'], inplace=True)

# Encode categorical features
label_cols = ['Gender', 'Sadness_Level', 'Interest_Loss', 'Fatigue_Level', 'Mood_Swings',
              'Guilt_or_Worthlessness', 'Worry_Level', 'Restlessness', 'Panic_Attacks',
              'Concentration_Difficulty', 'Obsessions', 'Compulsions', 'Trauma_History',
              'Flashbacks', 'Nightmares', 'Avoidance_Behavior', 'Manic_Episodes',
              'Impulsivity', 'Hyperactivity', 'Task_Completion', 'Social_Communication',
              'Eye_Contact', 'Special_Interests', 'Routine_Rigidity', 'Sensory_Issues']

for col in label_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

# Features and targets
X = df.drop(columns=diagnoses)
y = df[diagnoses]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X_train, y_train)

# Save the model and features
joblib.dump(model, 'mental_health_model.pkl')
joblib.dump(X.columns.tolist(), 'features.pkl')

print("✅ Model trained and saved.")
