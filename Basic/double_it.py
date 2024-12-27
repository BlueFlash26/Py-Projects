array = []

def double_it(value):
    while value < 100:
        output = "2 x " + str(value) + " = "
        #array.append(value)
        value = value * 2
        #print(value, end=" ")
        print(output, value)
    


double_it(int(input("Enter your value: ")))