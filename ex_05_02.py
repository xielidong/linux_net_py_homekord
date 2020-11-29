list=[]
total = 0
while True:
    inp = input('Enter a number : ')
    try:
        num = (int)(inp)
        list.append(num)
    except:
        if inp=='done':
            break
        else:
            print('Invalid input')
for i in range(0,len(list)):
    total=total+list[i]
print(total,len(list),max(list),min(list))            
