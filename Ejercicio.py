

def learYear():

    year = int(input("Enter the year:"))
    if(year % 4 ==0 or year % 100 == 0 or year % 400 == 0 ):
        print('It is')
    else:
        print("It isn't")


learYear()
