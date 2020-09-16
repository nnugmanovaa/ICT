import math
from datetime import datetime
#Exercise1: 
#print('Nargiza, nnugmanovaa@gmail.com')

#Exercise2:
#name = input('What is your name ? ')
#print('Hello, ', name)

#Exercise3:
#width = float(input('Please, enter the width(m) of the room '))
#length = float(input('Please, enter the length(m) of the room '))
#print(str(width*length) + " m^2")

#Exercise4:
#width = float(input('Please, enter the width(feet) of the farm.. '))
#length = float(input('Please, enter the length(feet) of the farm.. '))
#area = width*length*43.560 
#print('Area of the farm in acre is ' + str(area) + ' acre')

#Exercise5:
#liter_or_less = int(input("Please, enter the number of bottles with container less or equal to one liter "))
#more_than_one = int(input("Please, enter the number of bottles with container more than one liter "))
#print("The sum is " + str(liter_or_less*0.10 + more_than_one*0.25) + "$")

#Exercise6:
#cost = float(input("Please, enter the cost of meal "))
#tip = 0.18
#tax = 0.2
#tipA = cost * tip
#taxA = cost * tax
#print("Tip: " + str(tipA) + "\n" + "Tax: " + str(taxA) + "\n" + "Total amount: " + "{:.2f}".format(cost + tipA + taxA))

#Exercise7:
#number = int(input("Please, enter a positive integer n "))
#print(number * (number + 1) / 2)

#Exercise8:
#widgets = int(input("Please, enter the number of widgets.. "))
#gizmos = int(input("Please, enter the number of gizmos.. "))
#print("Total weight of the order " + str(widgets * 75 + gizmos * 112))

#Exercise9:
#money = float(input("Please, enter the amount of money deposited into the account.. "))
#after_one_year = money*0.04 + money
#after_two_years = after_one_year*0.04 + after_one_year
#after_three_years = after_two_years*0.04 + after_two_years
#print("Deposite after one year: " + "{:.2f}".format(after_one_year) + "\n" + "Deposite after two years: " 
#+ "{:.2f}".format(after_two_years) + "\n"
#+ "Deposite after three years: " + "{:.2f}".format(after_three_years))

#Exercise10:
#a = int(input("Please, enter first number"))
#b = int(input("Please, enter second number"))
#print(a + b)
#print(a - b)
#print(a * b)
#print(a // b)
#print(a % b)
#print(math.log10(a))

#Exercise11:
#mpg = float(input("Please, enter the x MPG "))
#print("Formula for converting MPG to L/100km: \n L/100km = 282.48/xmpg")
#answer = 282.48/mpg
#print("{:.2f}".format(answer))

#Exercise12:
#t1 = float(input("Please, enter t1 "))
#g1 = float(input("Please, enter g1 "))
#t2 = float(input("Please, enter t2 "))
#g2 = float(input("Please, enter g2 "))

#t1Rad = math.radians(t1)
#t2Rad = math.radians(t2)
#g1Rad = math.radians(g1)
#g2Rad = math.radians(g2)

#result = 6371.01 * math.acos(math.sin(t1Rad)*math.sin(t2Rad) + math.cos(t1Rad)*math.cos(t2Rad) - math.cos(g1Rad - g2Rad))
#print("Result: " + "{:.2f}".format(result))

#Exercise13:


#Exercise14:
#feet = float(input("Feet: "))
#inch = float(input("Inch: "))

#feet_to_inch = feet*12
#print("Result: " + "{:.2f}".format((feet_to_inch + inch) * 2.54))

#Exercise15:
#feet = float(input("Feet: "))
#feet_to_inch = feet * 12
#feet_to_yards = feet / 3
#feet_to_miles = feet / 5280
#print("Feet in: \n" + "inch: " + str(feet_to_inch) + "\n" + "yards: " + str(feet_to_yards) +
#"\n" + "miles: " + str(feet_to_miles) )

#Exercise16:
#r = float(input("Please, enter the radius "))
#area = math.pi * r**2
#volume = 4/3*math.pi*r**3
#print("Area: " + "{:.2f}".format(area) + "\n" + "Volume: " + "{:.2f}".format(volume)) 

#Exercise17:
#m = float(input("Mass: "))
#T = float(input("T: "))
#c = 4200
#Q = m*c*T*2.7*10**-7
#price = Q * 8.9
#print("Q = " + str(Q) + "\n" + "Price: " + str(int(price)))


#Exercise18:
#r = float(input("Please, enter the radius "))
#h = float(input("Please, enter the height "))
#v = math.pi*r**2*h
#print("Volume: " + "{:.2f}".format(v))

#Exercise19:
#h = float(input("Height: "))
#g = 9.8
#v = math.sqrt(2*g*h)
#print("Speed: " + str(v))

#Exercise20:
#R = 8.3144598
#v = 0.012
#p = 20000000
#t = 48 + 273.15
#pv = p*v
#rt = R*t
#n = pv/rt
#print("{:.2f}".format(n))

#Exercise21:
#b = float(input("Please, enter the length of the base "))
#h = float(input("Please, enter the height of the base "))
#area = b*h/2
#print("Length of the base: " + str(b) + "\n" + "Height: " +str(h) + "\n" + "Area: " + str(area) )

#Exercise22:
#s1 = float(input("Please, enter s1 "))
#s2 = float(input("Please, enter s2 "))
#s3 = float(input("Please, enter s3 "))
#s = (s1 + s2 + s3)/2
#area = math.sqrt(s*(s - s1)*(s - s2)*(s - s3))

#Exercise23:
#s = float(input("Please, enter s "))
#n = float(input("Please, enter n "))
#area = n*s**2/4*math.tan(math.pi/n)
#print("Area of the polygon " + str(area))

#Exercise24:
#d = float(input("Please, enter days "))
#h = float(input("Please, enter hours "))
#m = float(input("Please, enter minutes "))
#s = float(input("Please, enter seconds "))
#day_to_seconds = d * 86400
#hours_to_seconds = h * 3600
#minutes_to_seconds = m * 60
#print("Total seconds: " + str(day_to_seconds+hours_to_seconds+minutes_to_seconds+s))

#Exercise25:
#n = 1
#h = 0
#m = 0
#s = int(input())
#if(s<3600):
#    h = 0
#    if(s > 60):
#        m = int(s/60)
#        s -= m*60 
#if(s > 3600):
#    h = int(s/3600)
#    m = int((s-3600*h)/60)
#    s -= h*3600 + m * 60
#print(str(h) + "HH:" + str(m) + "MM:" + str(s) + "SS")


#Exercise26:
#now = datetime.now() 
#dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("Current date and time =", dt_string) 

#Exercise27:
#weight = float(input("Hi, please enter your weight:.."))
#height = float(input("Please enter your height:.."))
#num = int(input("If you prefer to calculate BMI in inches and pounds enter 1, else 2"))
#if(num == 1):
#    print(weight*703/height**2)
#else:
#    print(weight/height**2)

#Exercise28:
#Ta = float(input("Temperature:"))
#V = float(input("Wind speed:"))
#if(Ta <= 10.0 & V > 4.8):
#    WCL = 13.12 + 0.6215*Ta - 11.37*V**0.16 + 0.3965*Ta*V**0.16
#    print("WCL: " + str(int(WCL)))
#else:
#    print("Invalid data!")

#Exercise29:
#tempC = float(input("Please,enter the temp in Celsius: "))
#print("Fahrenheit: " + str((tempC*9/5)+32) + "\n" + "Kelvin: " + str(tempC + 273))

#Exercise30:
#press = float(input("Please,enter the pressure in kPa: "))
#psi = press* 0.14503773773022
#print("kPa: " + str((press)) + "\n" + "psi: " + str(psi))

#Exercise31:
#num = int(input("Please,enter an integer: "))
#sum = 0 
#while(num > 0):
#    sum += num % 10
#    num = num / 10
#print(sum)

#Exercise32:
#a = int(input("Please, enter the first number: .."))
#b = int(input("Please, enter second number: .."))
#c = int(input("Please, enter third number: .."))
#maxi = max(a,b,c)
#mini = min(a,b,c)
#av = a + b + c - maxi - mini
#print("Max: " + str(maxi) + " Min: " + str(mini) + " Avg: " + str(av))

#Exercise33:
#dBred = float(input("Please, enter the number of day-old bread: "))
#total = 3.49 * dBred
#count = total * 0.4
#withCount = total - count
#print("Total: " + "{:.2f}".format(total) + " Count: " + "{:.2f}".format(count) + " With count: " + "{:.2f}".format(withCount) )