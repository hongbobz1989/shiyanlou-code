for i in range(1,101):
    x= i//10
    y=(i-10*x)
    if i%7 and x!=7 and y!=7:
        print(i)


