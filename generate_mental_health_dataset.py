import pandas as pd
import random

# Set seed for reproducibility
random.seed(42)

# Define options
genders = ['Male', 'Female', 'Other']
sadness_levels = ['Low', 'Medium', 'High']
binary = ['Yes', 'No']
diagnoses = ['Depression', 'Anxiety', 'OCD', 'PTSD', 'Bipolar', 'Insomnia', 'ADHD', 'Autism']

# Function to randomly assign multi-label diagnosis
def random_diagnosis():
    return {disease: random.choice([0, 1]) for disease in diagnoses}

# Generate 500 rows
data = []
for i in range(1, 501):
    diagnosis = random_diagnosis()
    row = {
        'ID': i,
        'Age': random.randint(18, 65),
        'Gender': random.choice(genders),
        'Sadness_Level': random.choice(sadness_levels),
        'Interest_Loss': random.choice(binary),
        'Fatigue_Level': random.choice(sadness_levels),
        'Sleep_Hours': round(random.uniform(2, 10), 1),
        'Mood_Swings': random.choice(binary),
        'Guilt_or_Worthlessness': random.choice(binary),
        'Worry_Level': random.choice(sadness_levels),
        'Restlessness': random.choice(binary),
        'Panic_Attacks': random.choice(binary),
        'Concentration_Difficulty': random.choice(binary),
        'Obsessions': random.choice(binary),
        'Compulsions': random.choice(binary),
        'Trauma_History': random.choice(binary),
        'Flashbacks': random.choice(binary),
        'Nightmares': random.choice(binary),
        'Avoidance_Behavior': random.choice(binary),
        'Manic_Episodes': random.choice(binary),
        'Attention_Span': random.randint(1, 10),
        'Impulsivity': random.choice(binary),
        'Hyperactivity': random.choice(binary),
        'Task_Completion': random.choice(['Low', 'Medium', 'High']),
        'Social_Communication': random.choice(['Low', 'Medium', 'High']),
        'Eye_Contact': random.choice(binary),
        'Special_Interests': random.choice(binary),
        'Routine_Rigidity': random.choice(binary),
        'Sensory_Issues': random.choice(binary),
    }
    row.update(diagnosis)
    data.append(row)

# Create and save dataset
df = pd.DataFrame(data)
df.to_csv("mental_health_dataset.csv", index=False)

print("✅ Dataset with 500 rows created and saved as 'mental_health_dataset.csv'")
