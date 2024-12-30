array = []

def double_it(value):
    value = round(value)
    while value < 100:
        output = "2 x " + str(value) + " = "
        #array.append(value)
        value = value * 2
        #print(value, end=" ")
        print(output, value)
    


double_it(float(input("Enter your value: ")))
