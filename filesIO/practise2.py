# # write a program to mine a log file and find out whether it contains 'python'

# with open("filesIO/log.txt") as f:
#     content=f.read().lower()
# if content.__contains__("python"):   #if "python" in content:
#     print("Python is present")
# else:
#     print("Python is not present")





# 3. write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# place these files in a folder for a 13years old.

for i in range(2,21):
    with open(f"filesIO/13yrsold/multiplication_of_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}")
            if j!=10:
                f.write("\n")
