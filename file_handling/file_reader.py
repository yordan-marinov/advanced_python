f_handle = open("08-File-Handling-Lab-Resources/File Reader/numbers.txt", "r")


print(sum([int(b) for b in f_handle]))
