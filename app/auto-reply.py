import time , json
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
from pprint import pprint

driver = WhatsAPIDriver()
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

with open('data/products.json') as data_file:    
    products = json.load(data_file)

txt = '''
*PAKET %s*

*Harga* : %s

*FUP* : %s
'''

"""
match message with products data
"""
while True:
    time.sleep(3)
    print('Checking for more messages')
    for contact in driver.get_unread():
        for message in contact.messages:
            if isinstance(message, Message):
                chat_id = message.id
                sender_id = message.chat_id
                sender = str(message.sender)
                content = message.content.lower()

                if any(reg in content for reg in products):
                    for reg in products:
                        if reg in content:
                            reply_msg = txt % (reg.upper(), products[reg]['price'], products[reg]['fup'])
                            contact.chat.send_message(reply_msg)

                else:
                    reply_msg = 'maaf data yang Anda cari tidak tersedia saat ini.'
                    contact.chat.send_message(reply_msg)
                    
                # contact.chat.send_message(reply_msg)