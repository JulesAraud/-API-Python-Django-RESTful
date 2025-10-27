for i in range(1, 51):
    print("fizz"*(i%3==0) + "buzz"*(i%5==0) or i)
