#Round Robin Scheduling Algorithm Implementation
def round_robin(n, p, at, bt, tq):
    rt = bt[:]
    ct = [0] * n
    time = 0
    q = []
    completed = 0
    visited = [False] * n
    for i in range(n):
        if at[i] == 0:
            q.append(i)
            visited[i] = True
    while completed != n:
        if not q:
            time += 1
            for i in range(n):
                if at[i] <= time and not visited[i]:
                    q.append(i)
                    visited[i] = True
            continue
        idx = q.pop(0)
        exec_time = min(tq, rt[idx])
        rt[idx] -= exec_time
        time += exec_time
        for i in range(n):
            if at[i] <= time and not visited[i]:
                q.append(i)
                visited[i] = True
        if rt[idx] == 0:
            ct[idx] = time
            completed += 1
        else:
            q.append(idx)
    return ct

n = int(input("Enter the number of processes: "))
p = [0] * n
bt = [0] * n
at = [0] * n

for i in range(n):
    p[i] = i + 1
    bt[i] = int(input(f"Enter burst time of process {p[i]}: "))
    at[i] = int(input(f"Enter arrival time of process {p[i]}: "))

tq = int(input("Enter Time Quantum: "))
ct = round_robin(n, p, at, bt, tq)
tat = [0] * n
wt = [0] * n

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
    print(f"P{p[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_tat = sum(tat) / n
print(f"Average Turnaround Time: {avg_tat:.2f}")
avg_wt = sum(wt) / n
print(f"Average Waiting Time: {avg_wt:.2f}")

#Shortest Job First (SJF) Scheduling Algorithm Implementation
def sjf(n, p, at, bt):
    completed = 0
    time = 0
    ct = [0] * n
    is_completed = [False] * n
    while completed != n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if at[i] <= time and not is_completed[i]:
                if bt[i] < min_bt:
                    min_bt = bt[i]
                    idx = i
                elif bt[i] == min_bt:
                    if at[i] < at[idx]:
                        idx = i
        if idx == -1:
            time += 1
        else:
            time += bt[idx]
            ct[idx] = time
            is_completed[idx] = True
            completed += 1
    return ct
n = int(input("Enter the number of processes: "))
p = [0] * n
bt = [0] * n
at = [0] * n
for i in range(n):
    p[i] = i + 1
    bt[i] = int(input(f"Enter burst time of process {p[i]}: "))
    at[i] = int(input(f"Enter arrival time of process {p[i]}: "))
ct = sjf(n, p, at, bt)
tat=[0]*n
wt=[0]*n
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i]=tat[i]-bt[i]
    print(f"P{p[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")
avg_tat = sum(tat)/n
print(f"Average Turnaround Time: {avg_tat:.2f}")
avg_wt=sum(wt)/n
print(f"Average Waiting Time: {avg_wt:.2f}")


#First Come First Serve (FCFS) Scheduling Algorithm Implementation
def fcfs(n, p, at, bt):
    processes = list(zip(p, at, bt))
    processes.sort(key=lambda x: x[1])
    ct = [0] * n
    start_time = 0
    for pid, arrival, burst in processes:
        if start_time < arrival:
            start_time = arrival
        start_time += burst
        original_index = p.index(pid)
        ct[original_index] = start_time
    return ct

n = int(input("Enter the number of processes: "))
p = [0] * n
bt = [0] * n
at = [0] * n

for i in range(n):
    p[i] = i + 1
    bt[i] = int(input(f"Enter burst time of process {p[i]}: "))
    at[i] = int(input(f"Enter arrival time of process {p[i]}: "))

ct = fcfs(n, p, at, bt)
tat = [0] * n
wt = [0] * n

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
    print(f"P{p[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_tat = sum(tat) / n
print(f"Average Turnaround Time: {avg_tat:.2f}")
avg_wt = sum(wt) / n
print(f"Average Waiting Time: {avg_wt:.2f}")
