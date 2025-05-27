#create a new file with name of sample.txt
#write some content append some content and read separate execution
# read content from begining



import os
##creating a file 
with open('sample.txt','w') as file:
    file.write("hello BVRIT HYDERABAD\n")


##appending a file 
with open("sample.txt", "a") as file:
    file.write("Welcome to the Capgemini Training.\n")
    file.write("Today's topic is Python.\n")


##reading the content of file from the beginning 
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
if os.path.exists("newfile.txt"):
    print("newfile.txt exists")
