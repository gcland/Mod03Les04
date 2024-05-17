import re

text = "Name: fhsiudhfuskdn23423; Age: 30; Occupation: 8wa7dasdzzzskjn!; Location: New York"
# Extract the Occupation from the text
# Your code here

occupation_match = re.findall(r"Occupation: (.+?);", text)
name_match = re.findall(r"Name: (.+?);", text)

print(f"{str(name_match[0])}'s occupation: {str(occupation_match[0])}.")