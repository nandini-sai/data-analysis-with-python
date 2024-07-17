import requests
from bs4 import BeautifulSoup

# Replace with your target URL
url = "https://www.vedantu.com/english/essay-on-tourism"

response = requests.get(url)

# Check for successful response
if response.status_code == 200:
 # Parse the HTML content
 soup = BeautifulSoup(response.text, 'html.parser')

 page_text=soup.get_text()

 links= [a['href']for a in soup.find_all('a',href=True)]

 images= [img['src']for img in soup.find_all('img',src=True)]
 
 print("Page_Text:")
 print(page_text)

 print ("\nLinks:")
 for link in links:
  print (link)

  print("\nImages:")
  for image in images:
   print(image)
   
else:
 print(f"Faild to retrieve the web page,Status code: {response.status_code}")