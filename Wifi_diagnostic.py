# Wifi Diagnostic tree

# Named Constants


# Menu

print('Wifi diagnostics')
print('----------------')
print('Reboot the computer and try to connect')

# User input
question = input('Did this work? ')
print('----------------')

# loop that determines if the user needs ro continue with the wifi troubleshooting 
if question == 'yes':
    print('Wi-fi should be working!')
    

elif question == 'no': 
    print('Make sure all the cables between the router & modem are plugged in firmly')
    question = input('Did this work? ') 
    print('----------------') 
    if question == 'yes': 
        print('Wi-fi should be working!')


    elif question == 'no':
        print('Move the router to a new location.') 
        question = input('Did this work? ')
        print('----------------')
        if question == 'yes': 
            print('Wi-fi should be working!')

        elif question =='no':
            print('Get a new router.')

        else: 
            print('Please enter yes or no') 


           
    