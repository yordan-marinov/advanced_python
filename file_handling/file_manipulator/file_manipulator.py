import os


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
