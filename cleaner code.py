import re
import unicodedata
import pandas as pd

# read 
combined_df = pd.read_csv(r"C:\Users\jasmi\Projects\Final Project\combined_dataset.csv")

# define cleaning
def clean_text(text):
    if not isinstance(text, str):
        return text
    text = unicodedata.normalize("NFKD", text)
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
    return text.strip()

# apply cleaning
combined_df["Bodycam Transcript"] = combined_df["Bodycam Transcript"].apply(clean_text)

# save new dataset
combined_df.to_csv("cleaned_dataset.csv", index=False)
print("Cleaned")
