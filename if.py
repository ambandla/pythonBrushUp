alienColor = "red"
if alienColor == 'green':
    print ("you got 5 points.")
elif alienColor == 'yellow':
    print ("you got 10 points.")
elif alienColor == 'red':
    print ("you got 15 points.")
else: 
    print ("not an alien.")

age = int(40)

if age < 2:
    print ("baby")
elif age < 4:
    print ("toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print ("teenager")
elif age < 65:
    print ("adult")
elif age >65:
    print ("old")