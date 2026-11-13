def Future_Value(p,i,t):
    f=p*(1+i)**t
    return f
def display(f):
    print("The Future Value is",f)

def main():
   p= float(input("enter Present Value"))
   i=float(input("enter Interest Rate in decimals"))
   t=float(input("enter number of months"))
   f=Future_Value(p,i,t)
   display(f)

   main()