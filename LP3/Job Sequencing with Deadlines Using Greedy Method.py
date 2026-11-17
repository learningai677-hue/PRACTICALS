
# Job Sequencing with Deadlines using Greedy Method

def job_sequencing(jobs):
    # Sort jobs according to decreasing profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    slots = [False] * n
    result = ['-1'] * n
    total_profit = 0

    for job in jobs:
        job_id, deadline, profit = job

        # Find an empty slot before the deadline
        for j in range(min(deadline, n) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                result[j] = job_id
                total_profit += profit
                break

    print("Scheduled Jobs:", result)
    print("Maximum Profit:", total_profit)


# Main Program
jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

job_sequencing(jobs)
