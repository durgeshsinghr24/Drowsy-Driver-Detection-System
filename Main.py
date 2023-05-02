from twilio.rest import Client 
import Keys 
from Geo import latitude
from Geo import longitude 

Client = Client(Keys.account_sid, Keys.auth_token)

message = Client.messages.create(
    body = "**ALERT THE DRIVER IS DETECTED DROWSY OVER THE LIMIT** "+"\n"+"Live location link: "+"https://www.google.com/maps/place/"+str(latitude)+','+str(longitude),
    from_=Keys.twilio_number,
    to = Keys.my_phone_number
)

print(message.body)
