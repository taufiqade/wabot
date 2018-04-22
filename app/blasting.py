import time , json
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
from pprint import pprint

driver = WhatsAPIDriver()
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

with open('data/nomer_pm.json') as data_file:    
    numbers = json.load(data_file)

message = "test test test"

i = 0
for number in numbers:
    print('sending to', number)
    driver.send_message_to_id(number, message)
    i += 1

print("============================")
print("=====BLASTING COMPLETE======")
print("============================")
