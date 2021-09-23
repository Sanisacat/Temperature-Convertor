celsius = float(input("Please enter the temperature in celsius: "))

fahrenheit = (celsius * 1.8) + 32

print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

temp = fahrenheit

if(temp >= 104):
    print("Too hot")
elif(temp <= 50):
    print("Too cold")
else:
    print("Moderate")

    