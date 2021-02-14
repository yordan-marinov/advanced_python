def deliver(lst, *args):
    return lst + list(args)


def removing(lst, *args):
    if not args:
        return lst[1:]
    if isinstance(args[0], int):
        return lst[args[0]:]
    for item in args:
        if item not in lst:
            return lst
        while item in lst:
            lst.remove(item)
    return lst


def stock_availability(*args):
    inventory_list, command, *elements = args
    commands = {"delivery": deliver, "sell": removing}
    result = commands[command](inventory_list, *elements)
    if not result:
        return []
    else:
        return result


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
