import re

text = "Contact emails are: 2983JDHKGsjdnns823`!@#$%^&*().doe@example.com and jane.doe@example.com and codingtempler@yahoo.com and helloWORLD!`@gmail.org and jason.bourne@federalgovernmentjobs.unitedstates" #modified first email with special characters
emails = re.findall(r"[A-Za-z0-9._%+-`!@#$%^&*()]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text) 
#added a-z to search in bracket before '@', after '@', and after '.'
#added ~!@#$%^&*() to email search ability

print(emails)
i=0
print("Emails found:")
for email in emails:
    i+=1
    print(f"{i}. {email}")