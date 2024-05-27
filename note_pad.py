print("*************Welcome To Oge's Notepad*************")
print("Select your command, press 1 to write, press 2 to save and end.")
command = input(">")
if command == "1":
    file_content = input("Start Typing: | ")
    file_name = input("Save As: ")
    target = open(file_name, 'w')
    target.write(file_content)
    target.close()

if command == "2":
    file_name= input("Enter file name")
    target = open(file_name, 'r')
    file_content = target.read()
    print(file_content)
    target.close()