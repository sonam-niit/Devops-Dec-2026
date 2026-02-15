from datetime import datetime,date

now= datetime.now()
print("Date & Time: ",now)
print("Date: ",now.date()) # only date
print("Year: ",now.year) # only year
print("Month: ",now.month) 
print("Day: ",now.day)
print("Hour: ",now.hour)
print("Minute: ",now.minute)

myday=date.today() # just date it will provide
print(myday)

print(f"Default Date and Time: {now}")
# Formating
print(f"Format: {now.strftime("%d/%m/%Y %H:%M:%S")}")
# convert Date into String

# Convert String to Date object
# use Parse: strptime
date_str="2025-05-03" # this is string
date_ob=datetime.strptime(date_str,"%Y-%m-%d")
print(date_ob)