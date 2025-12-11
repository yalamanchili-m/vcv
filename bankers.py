def bankers_algorithm(processes, resources, available, max_needs, allocation):
    work = list(available)
    finish = [False] * processes
    safe_sequence = []

    need = [[0 for _ in range(resources)] for _ in range(processes)]
    for i in range(processes):
        for j in range(resources):
            need[i][j] = max_needs[i][j] - allocation[i][j]

    count = 0
    while count < processes:
        found_process = False
        for i in range(processes):
            if not finish[i]:
                can_execute = True
                for j in range(resources):
                    if need[i][j] > work[j]:
                        can_execute = False
                        break

                if can_execute:
                    for j in range(resources):
                        work[j] += allocation[i][j]
                    safe_sequence.append(i)
                    finish[i] = True
                    found_process = True
                    count += 1

        if not found_process:
            return False, []
    return True, safe_sequence


if __name__ == "__main__":
    num_processes = 5
    num_resources = 3
    available_resources = [3, 3, 2]
    max_resources_needed = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    current_allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    is_safe, sequence = bankers_algorithm(
        num_processes,
        num_resources,
        available_resources,
        max_resources_needed,
        current_allocation
    )

    if is_safe:
        print("System is in a safe state.")
        print("Safe sequence:", ["P" + str(i) for i in sequence])
    else:
        print("System is in an unsafe state (deadlock might occur).")
