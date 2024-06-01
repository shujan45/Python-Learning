
# we can write files name as ;
# -----> open('file_name','w/r/a')
# -----> open(f"folder_name/file_name",'w/r/a') #if you are not using any variable with ccertain values in the file name you don't have to use 'f' in  'f"..."'


# f = open(f'filesIO/sample.txt','r') #use open function to read the conten of the file!  here,'r' is mode of opening r=read mode
f= open(f"filesIO/sample.txt",'r') #by default the mode is 'r'  
data =f.read()
# data=f.read(5) # read(5) means it will only read/display first 5 character 
print(data)
f.close()