def create_rhombus(num: int):
    increasing = 1
    decreasing = -1

    def print_rhombus_line(n:int, direction: int):
        if n == 0:
            return

        line = ' ' * (num - n) + "* " * n
        print(line.rstrip())

        if n == num:
            direction = decreasing

        print_rhombus_line(n + direction, direction)

    print_rhombus_line(1, increasing)


create_rhombus(int(input()))