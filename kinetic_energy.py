def Kinetic_Energy(m,v):
    ke=0.5*m*v*v
    return ke
def Display(ke):
    print("The value of Kinetic Energy is",ke)

def main():
    m=float(input("enter mass"))
    v=float(input("enter velocity"))
    ke=Kinetic_Energy(m,v)
    Display(ke)

main()