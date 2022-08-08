import phonenumbers  
from phonenumbers import timezone,geocoder,carrier

phoneNumber= (input("Enter a phone Number"))
phoneNumber = phonenumbers.parse (phoneNumber)


timeZone = timezone.time_zones_for_number(phoneNumber)

carrier = carrier . name_for_number(phoneNumber , 'en')

Region = geocoder . description_for_number(phoneNumber, 'en')
#name = ("enter the name   from phonenumber")
 #import datetime
 #import pytz
 #current_time = datetime.datetime.
# import datetime
# datetime.datetime.now()
#datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

# print(datetime.datetime.now())

print (phoneNumber)
print (timeZone)
print (carrier)
print (Region)
#print (name)
#print ("The current time in india")
 #print (current_time)