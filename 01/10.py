from dataclasses import dataclass

print(10, 50)
print("answer:", 10, 50, sep = "!!!")

print("answer:", 10, 50, end = " ")
print(777)

f = open("test.txt" , "w")
print( 10, 50, file = f )
f.close()





