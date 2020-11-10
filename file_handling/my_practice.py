with open("08-File-Handling-Lab-Resources/Even Lines/text.txt") as f_handle:
    with open("file_copy.txt", "w") as wf:

        for line in f_handle:
            wf.write(line)
