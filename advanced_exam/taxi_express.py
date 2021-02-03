from collections import deque


def current_element(sequence_deque: deque) -> int:
    return sequence_deque.popleft()


def taxi_can_drive_customer(client, driver) -> bool:
    return driver >= client


def leave_customer_at_the_que_beginning(que: deque, current_customer: int):
    return que.appendleft(current_customer)


customers = deque(int(n) for n in input().split(", "))
taxis = deque(int(n) for n in input().split(", ")[::-1])

total_time = 0
while customers and taxis:
    customer = current_element(customers)
    taxi = current_element(taxis)
    if not taxi_can_drive_customer(customer, taxi):
        leave_customer_at_the_que_beginning(customers, customer)
        continue
    total_time += customer


if not customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(c) for c in customers)}")
