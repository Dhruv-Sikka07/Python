print("byte example")
b=bytes([65,66,67,68])
print(b)
print(b[0])
print(b[1])
for byte in b:
    print(byte,end='')
print("\n")
print("bytearray example")
ba=bytearray([65,66,67,68])
print(ba)
ba.append(69)
print(ba)
print("\n")
print("memory view")
b_mv=bytes([65,66,67,68,69])
mv=memoryview(b_mv)
print(mv)
print(mv[0])
mv_slice = mv[1:4]
ba_mv =bytearray([65,66,67,68,69])
mv_ba=memoryview(ba_mv)
mv_ba[0]=97
print(ba_mv)
print("\n")
print("Program by Dhruv Sikka")
