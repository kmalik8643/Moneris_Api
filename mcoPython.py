import requests
from bs4 import BeautifulSoup
import re
import webbrowser
import os 

url = 'https://gatewayt.moneris.com/chktv2/request/request.php'
data = {

  "store_id":"monca07619",
  "api_token": "4QRSn8yFXYs0givmVBBo",
  "checkout_id":"chktVR9KV07619",
  "txn_total":"2.00",
  "environment":"qa",
  "action":"preload"

}

response = requests.post(url, json=data)

if response.ok:
  json_response = response.json()
  #print('POST request successful!')
  ticket = json_response["response"]["ticket"]
  #print(ticket)
else:
  print('Error:', response.status_code)

file_path = r'C:\Users\Kamal.Maurya\OneDrive - Moneris\Desktop\web templates\mco.html'

with open(file_path, 'r') as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, 'html.parser')
#print(soup)

script_tags = soup.find_all('script')
if len(script_tags) >= 2:
    script_tag = script_tags[1]
#print(script_tag)
if script_tag is not None:  # Check if <script> tag exists
    script_code = script_tag.string
    #print(script_code)

    if script_code is not None:
      script_code = script_tag.string
      variable_name = "ticketNumber"
      new_value = ticket

      pattern = rf'({variable_name}\s*=\s*)[^;]+'

      modified_code = re.sub(pattern, fr'\g<1>"{new_value}"', script_tag.string)
      script_tag.string = modified_code  

      with open(file_path, 'w') as file:
          file.write(soup.prettify())

else:
  print("no script tag found")

with open('ticket.txt', 'w') as f:
   f.write(ticket)


webbrowser.open_new_tab(file_path)