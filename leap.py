n=int(input('enter your number'))
if(n%100==0 and n%400==0):
    print('leep year')
elif(n%100!=0 and n%4==0):
    print('leap year')
else:
    print('not a leap year')
