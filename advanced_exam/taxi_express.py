from collections import deque


def get_element(que: deque):
    return que.popleft()


def can_taxi_drive_customer(customer, taxi):
    return taxi >= customer


def send_customer_back(customer, customers):
    return customers.appendleft(customer)


def increase_total_time(customer_time, total_time):
    total_time += customer_time
    return total_time


def drive(customers, taxis):
    total_time = 0
    while True:
        if not customers:
            return f"All customers were driven to their destinations\n" \
                   f"Total time: {total_time} minutes"
        if not taxis:
            return f"Not all customers were driven to their destinations\n" \
                   f"Customers left: {', '.join(map(str, customers))}"

        next_customer = get_element(customers)
        next_taxi = get_element(taxis)

        if can_taxi_drive_customer(next_customer, next_taxi):
            total_time = increase_total_time(next_customer, total_time)
        else:
            send_customer_back(next_customer, customers)


customers = deque([int(c) for c in input().split(", ")])
taxis = deque([int(t) for t in input().split(", ")][::-1])

print(drive(customers, taxis))
