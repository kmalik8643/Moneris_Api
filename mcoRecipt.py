import requests
import json


url = "https://gatewayt.moneris.com/chktv2/request/request.php"
with open('ticket.txt', 'r') as file:
  ticket = file.read()

print(ticket)
data = {

  "store_id": "monca07619",
  "api_token": "4QRSn8yFXYs0givmVBBo",
  "checkout_id": "chktVR9KV07619",
  "ticket": ticket,
  "environment": "qa",
  "action": "receipt"
}


response = requests.post(url, json=data)

if response.ok:
  json_response = response.json()
  print('POST request successful!')
  reciept = json_response["response"]
  print(reciept)
else:
  print('Error:', response.status_code)

with open("receipt.txt", 'w') as f:
  f.write(json.dumps(reciept))