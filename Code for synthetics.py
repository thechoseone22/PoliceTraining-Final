import google.generativeai as genai
import random
import pandas as pd
import unicodedata
import re
import Gemini_api

# API key
genai.configure(api_key=Gemini_api.GEMINI_KEY)

# Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Features and choices
incident_types = ["Domestic Dispute", "Traffic Stop", "Disturbance Call", "Suspicious Person", "Welfare Check"]
officer_actions = [
    "Verbal Commands", "Requested Backup", "Used Calm Tone",
    "Non-threatening Gestures", "Defensive Positioning", "Raised Voice",
    "Physical Restraint", "Pointed Weapon"
]
subject_behaviors = [
    "Aggressive", "Non-compliant", "Cooperative",
    "Hostile", "Attempted to Flee", "Threatened Officer",
    "Armed and Hostile"
]
deescalation_tactics = [
    "Calming Language", "Verbal Warning", "Maintained Distance",
    "Non-threatening Gestures", "Empathy Statements",
    "Requesting Cooperation", "Offering Assistance"
]
weapons_used = ["None", "Firearm", "Knife", "Blunt Object", "Taser"]
incident_outcomes = [
    "Injured", "Not Injured", "Arrested Peacefully",
    "Escalated to Force", "Officer Injured", "Subject Escaped"
]

# fix text 
def normalize_text(text):
    return unicodedata.normalize("NFKD", text)

def clean_special_characters(text):
    text = re.sub(r"Iâ€™m", "I'm", text, flags=re.IGNORECASE)  # "I’m"
    text = re.sub(r"Iâ€™ll", "I'll", text, flags=re.IGNORECASE)  # "I’ll"
    text = re.sub(r"subjectâ€™s", "subject's", text, flags=re.IGNORECASE)  # "subject's"
    text = re.sub(r"youâ€™re", "you're", text, flags=re.IGNORECASE)  # "you're"
    text = re.sub(r"donâ€™t", "don't", text, flags=re.IGNORECASE)  # "don't"
    text = re.sub(r"thatâ€™s", "that's", text, flags=re.IGNORECASE)  # "that's"
    text = re.sub(r"itâ€™s", "it's", text, flags=re.IGNORECASE)  # "i'ts"
    text = re.sub(r"letâ€™s", "let's", text, flags=re.IGNORECASE)  # "let's"
    text = re.sub(r"â€™", "'", text, flags=re.IGNORECASE)  # single quotes
    text = re.sub(r"â€¦", "...", text)  # ellipses
    text = re.sub(r"â€œ", '"', text)  # opening double quotes
    text = re.sub(r"â€\x9d", '"', text)  # closing double quotes
    text = re.sub(r"â€“", "–", text)  # dash
    return text

# synthetic dataset
data = []

for _ in range(5):  # how many rows???
    # randomize values
    features = {
        "Incident Type": random.choice(incident_types),
        "Officer Action": random.choice(officer_actions),
        "Subject Behavior": random.choice(subject_behaviors),
        "De-escalation Tactic": random.choice(deescalation_tactics),
        "Weapon Involved": random.choice(weapons_used),
        "Incident Outcome": None  # outcome based on features for more realistic info
    }

    # outcome based on features
    if "Hostile" in features["Subject Behavior"] or "Threatened Officer" in features["Subject Behavior"]:
        if "Raised Voice" in features["Officer Action"] or "Physical Restraint" in features["Officer Action"]:
            features["Incident Outcome"] = random.choice(["Escalated to Force", "Officer Injured"])
        else:
            features["Incident Outcome"] = random.choice(["Not Injured", "Arrested Peacefully"])
    elif "Cooperative" in features["Subject Behavior"]:
        features["Incident Outcome"] = "Arrested Peacefully"
    else:
        features["Incident Outcome"] = random.choice(["Injured", "Not Injured", "Escalated to Force"])

    # bodycam transcript prompt
    prompt = (
        f"Generate a realistic bodycam transcript for an incident with the following details:\n"
        f"Incident Type: {features['Incident Type']}\n"
        f"Officer Action: {features['Officer Action']}\n"
        f"Subject Behavior: {features['Subject Behavior']}\n"
        f"De-escalation Tactic Used: {features['De-escalation Tactic']}\n"
        f"Weapon Involved: {features['Weapon Involved']}\n"
        f"Outcome: {features['Incident Outcome']}\n"
        f"Transcript should include timestamps, officer dialogue, subject responses, and environmental sounds."
    )

    # API narrative
    try:
        response = model.generate_content(prompt)
        response_text = response.text if hasattr(response, "text") else "No transcript generated"
    except Exception as e:
        response_text = f"Error generating transcript: {str(e)}"

    # clean and normalize text
    normalized_text = normalize_text(response_text)
    cleaned_text = clean_special_characters(normalized_text)

    # features and cleaned transcript for dataset
    features["Bodycam Transcript"] = cleaned_text
    data.append(features)

# dataFrame
df = pd.DataFrame(data)

# save CSV
df.to_csv("test.csv", index=False)

print("It finally fraking worked!!! Thank the gods, never again.")
