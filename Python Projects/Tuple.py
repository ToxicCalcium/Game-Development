T = ("Apple", 3, 789, True, "Spanish")
#Tuples can not be modified while the code is running
#Tuples also use indexes
#Tuples CAN have duplicate values
print(T)
print(len(T))
print(T[2])
for i in T:
    print(i)

print("Apple" in T)
#del T

V1, V2, V3, V4, V5 = T # Unpacking

print(V1)
T1 = ("Orange", T)
print(T1[0][1])
print(T[0:4:1])