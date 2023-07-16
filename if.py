#number = 3
#if number > 30:
#    print("more money taken")

#elif number > 20:
#    print ("the number > 20")

#else:
#    print("kokowawa")


#=====
w = input("please enter your wight : ")
g = input( "your wight in k or b" )
if g == "k":
    print("your wight in kg = " + w )
    converted = float(w) * 2.20462
    print("your wight in b = " , str(converted))
elif g == "b":
    print ("your wight in b ="+  w)
    converted = float(w) / 2.205
    print ("your wight in kg =" ,  str(converted) )