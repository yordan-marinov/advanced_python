import os

"""
Create a program that will receive commands until the command "End". 
The commands can be:
    
    • "Create-{file_name}" - Creates the given file with an empty content. 
    If the file already exists, remove the existing text in it 
    (as if the file is created again)
    
    • "Add-{file_name}-{content}" - Append the content and a new line after it. 
    If the file does not exist, create it and add the content
    
    • "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace 
    all the occurrences of the old string with the new string. 
    If the file does not exist, print: "An error occurred"
    
    • "Delete-{file_name}" - Delete the file. 
    If the file does not exist, print: "An error occurred"
"""


def create_file(file_name):
    with open(file_name, "w") as wf:
        wf.write("")


def add_contend(file_name, content):
    with open(file_name, "a") as wf:
        wf.write(content + "\n")


def replace(file_name, old_string, new_string):
    try:
        with open(file_name, "r") as rf:
            content = rf.read()
            if old_string in content:
                content = content.replace(old_string, new_string)
        with open(file_name, "w") as wf:
            wf.write(content)

    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        return
    print("An error occurred")


COMMANDS = {
    "Create": create_file,
    "Add": add_contend,
    "Replace": replace,
    "Delete": delete_file,
}

while True:
    data = input()
    if data == "End":
        break

    data = data.split("-")
    command = data.pop(0)
    COMMANDS[command](*data)


""""
=========== This is example input ==================

Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End

"""
