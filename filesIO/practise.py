# # 1. write a program to read the text from a given file 'poems.txt' and find out whether it contains the word twinkle

# # this part is not asked in the question . it is for write mode
# f=open('files/poems.txt','w')
# f.write('''Twinkle, twinkle, little star
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky
# Twinkle, twinkle, little star
# How I wonder what you are
# When the blazing sun is gone
# When he nothing shines upon
# Then you show your little light
# Twinkle, twinkle, all the night
# Twinkle, twinkle, little star
# How I wonder what you are
# Good night, baby''')
# f.close()

# f=open('files/poems.txt','r')
# data=f.read()
# print(data)
# if 'twinkle' in data:
#     print("\nTwinkle is present ")
# else:
#     print("Twinkle is not present ")

# f.close()



# 2.the game() function in a program lets a user play a game and returns the score as an integer. 
# you need to read a file 'hiscore.txt' which is either blank or contains the previous hi-score.
# you need to write a program to update the hi-score whenever game() breaks the hi-score

# def game():
#     return 64

# score=game()
# with open('files/hiscore.txt') as f :
#     hiscore= int(f.read())
# if hiscore<score:
#     with open('hiscore.txt','w') as f:
#         f.write(str(score))



# 3. write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# place these files in a folder for a 13years old.

# for i in range(2,21):
#     with open(f"filesIO/13yrs_old/multiplication_of_{i}.txt",'w') as f: #here f"files_I\O/13yrs_old/multiplication_of_{i}" indicates the file 'multiplication_of_{i}' is created in folder '13yrs_old' of folder files_I\O
#         for j in range(1,11):
#             f.write(f"{i}x{j}={i*j}")
#             if j!=10: #this is done since we had one extra line '11', to remove that it is done
#                     f.write("\n")




# 4. A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with #### by updating the same file


# with open(f"filesIO/ques4.txt",'w') as f:
#     f.write("You are a donkey who don't know anything. Even it is disrespect to the donkey if I call you that. You are wrost than anything present.")
#     f.close()

# with open("filesIO/ques4.txt",'r') as f:
#     content=f.read()
# content=content.replace("donkey", "##$%^%$")


# with open("filesIO/ques4.txt",'w') as f:
#     f.write(content)



# 5. repeat program 4 for a list of such words to be censored

# words = ["donkey","gadha","kutta","kamchor"]

# with open('filesIO/ques4.txt') as f:
#     content=f.read()

# for word in words:
#     content=content.replace(word, "@#$%!")
#     with open("filesIO/ques4.txt",'w') as f:
#         f.write(content)


# 6. write a program to mine a log file and find out whether it contains 'python'

# with open("filesIO/log.txt") as f:
#     content=f.read().lower() #here .lower() is used so that every character is read in small letter due to which not error is thrown afterward if file has character in uppercase
# if "python" in content:
#     print("Yes, python is present")
# else:
#     print("python is not present")


# # 7. write a program to find out the line number where python is present from ques 6

# content=True
# i=1 # i chai yesma line read/print garna ko lagi ho
# with open("filesIO/log.txt") as f:
#     while content:
#         content=f.readline().lower() # while loop ma enter vayepaxi f.readline le every time auta single line lae read garxa
#         if "python" in content:
#             print(content)
#             print(f"Yes, python is present on line no. {i}")
#         i+=1    




# # 8. write a program to make copy of text file "this.text"
# with open("filesIO/this.text") as f:
#     content=f.read()
# with open("filesIO/duplicate_this.text",'w') as g:
#     g.write(content)




# # 9.  write a program to find out whether a file is identical and matches the content of another file.

# with open("filesIO/duplicate_this.text") as f:
#     content1=f.read()
# with open("filesIO/this.text") as g:
#     content2=g.read()

# if content1 == content2:
#     print("-------->this two files are identical and contents are same<---------------")
# else:
#     print("-------->this two files arenot identical and contents are not same<--------")




# # 10. write a program to wipe out the contents of a file using pyhton
# with open("filesIO/duplicate_this.text","w") as f:
#     f.write(" ")


# 11. write a program to rename a file to "renamed_by_python.txt"

import os
oldname="filesIO/sample2.txt"
newname="filesIO/renamed_by_python.txt"
with open(oldname,'r') as f:
    content=f.read()

with open(newname,'w') as g:
    g.write(content)
os.remove(oldname)
