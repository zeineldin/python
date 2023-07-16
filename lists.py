names = ["Mohamed", "Hend", "Mariam", "Yoused", "Salma"]
print(len(names))
print(names[0:2])

names.append("Ali")
print(names)

print ("salma" in names)
print(len(names))

names.remove("Hend")
print("after removeing hend ", names)

names.clear()
print("after clear hend ", names)
