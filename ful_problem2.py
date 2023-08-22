import re
import requests

def get_website_details(url):
    # fetching data
    response = requests.get(url)
    
    # Check the request then proceed
    if response.status_code == 200:
        content = response.text
        social_links = re.findall(r'https?://[^\s/$.?#].[^\s]*', content)
        emails = re.findall(r'\S+@\S+', content)
        contacts = re.findall(r'[\+\d\s-]{10,}', content)

        return social_links, emails, contacts
    else:
        print("Sorry we failed to fetch website content.")
        return None, None, None

# User input for the website URL
website_url = input("Enter the website URL: ")

social_links, emails, contacts = get_website_details(website_url)

if social_links:
    print("Social links:")
    for link in social_links:
        print(link)

if emails:
    print("\nEmails:")
    for email in emails:
        print(email)

if contacts:
    print("\nContacts:")
    for contact in contacts:
        print(contact)
