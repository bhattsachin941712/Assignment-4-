a = int(input("Enter your marks:")) 
if a>80:
    print("A") 
elif 60<a<=80:
    print("B")
elif 50<a<=60: 
    print("C")
elif 45<a<=50:
    print("D")
elif 25<=a<=45:
    print("E")
elif 0<=a<25: 
    print("F")
else :
    print("Input is invalid")

