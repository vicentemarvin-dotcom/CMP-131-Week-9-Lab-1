def Celsius(f):
    c=0.55556*(f-32)
    return c
def display(c):
    print("Fahrenhiet to Celsius is",c)

def main():
    for f in range (21):
        c=Celsius(f)
        display(c)     
main()
