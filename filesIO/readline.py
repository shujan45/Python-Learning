f= open(f"filesIO/sample.txt")
data= f.readline()
print(data)
data= f.readline() #if readline() code is run twice it will print two lines from the source file provided
print(data)
f.close()