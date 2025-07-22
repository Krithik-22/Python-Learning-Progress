
#'r' - reads the file
with open("sample.txt","r") as file:
    content = file.read()
    print(content)

#'w' - writes the file completely
with open('output.txt','w') as file:
    file.write("We are gonna rock with our python journey\n")
    file.write("We are gonna rock with whatever we do\n")

#'a' - appends more to the existing file or a new file
with open('output.txt','a') as file:
    file.write("Let's rock!!!!\n")

