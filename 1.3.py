import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# Extract the Occupation from the text
# Your code here

occupation_match = re.findall(r"Occupation: (.+?);", text)
name_match = re.findall(r"Name: (.+?);", text)

print(f"{str(name_match[0])}'s occupation: {str(occupation_match[0])}.")