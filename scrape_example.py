import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.atibadulla.edu.lk/"

# Fetch HTML content of the page
response = requests.get(url)
if response.status_code == 200:
    html_content = response.content

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Example: Extracting all headings (h1, h2, h3, etc.)
    print("Page Headings:\n")
    for heading in soup.find_all(["h1", "h2", "h3"]):
        print(heading.get_text(strip=True))

    # Example: Extracting all paragraph text
    print("\nPage Paragraphs:\n")
    for para in soup.find_all("p"):
        print(para.get_text(strip=True))

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
