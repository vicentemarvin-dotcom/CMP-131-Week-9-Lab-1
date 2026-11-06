def Celsius(f):
    c=5/9*(f-32)
    return c
def display(c):
    print("Fahrenhiet to Celsius is",c)

def main():
    f=float(input("Enter Fahrenhiet"))
    for f in range(21):
        c= Celsius(f)
        print("")
