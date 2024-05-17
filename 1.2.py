import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)
emails_filter = []
filtered = []
for email in emails:
    if "@exclude.com" in email:
        filtered.append(email)
    else:
        emails_filter.append(email)
    
print(emails_filter)   
i=0
print("\nEmails found, excluding '@exclude.com':")
for email in emails_filter:
    i+=1
    print(f"{i}. {email}")
print("\nFiltered emails by '@exclude.com':")
i=0
for email in filtered:
    i+=1
    print(f"{i}. {email}")

