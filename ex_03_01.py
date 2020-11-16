hour=input("Enter hour:")
money=input("Enter money:")

h=(float)(hour)
m=(float)(money)
if h<=40 :
     print(h*m)
else:
    print(40*m+(h-40)*1.5*m)
