import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

# Define success/failure conditions
success_conditions = ["Not Injured", "Arrested Peacefully"]
df["Success/Failure"] = df["Incident Outcome"].apply(lambda x: 0 if x in success_conditions else 1)

# Save the updated dataset
df.to_csv("training_dataset.csv", index=False)

print("success")
