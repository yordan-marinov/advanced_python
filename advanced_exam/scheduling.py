def scheduling(lst: [int], searched_index: int) -> int:
    clock_cycles = 0
    jobs_integers_dict = {key_index: number for key_index, number in enumerate(lst)}
    for key, value in sorted(jobs_integers_dict.items(), key=lambda pair: (pair[1], pair[0])):
        clock_cycles += value
        if key == searched_index:
            return clock_cycles


jobs_integers = [int(n) for n in input().split(", ")]
job_index = int(input())

print(scheduling(jobs_integers, job_index))
