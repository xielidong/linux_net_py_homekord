count = 0
total = 0
while True:
    inp = input('Enter a number : ')
    try:
        num = (int)(inp)
        count+=1
        total+=num
    except:
        if inp=='done':
            break
        else:
            print('Invalid input')
print(total,count,total/count)         
