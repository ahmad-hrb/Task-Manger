num_of_tasks = int(input("Enter The Number Of Tasks: "))
my_tasks = []
for i in range(num_of_tasks):
    title = input("Enter The Title Of Task: ")
    duration = duration = int(input("Enter The Duration Of The Task: "))
    priority = int(input("Enter The Priority Of This Task: "))  
    my_tasks.append((priority, title, duration))

# extract the highest priority task
def complete_next_task(p_queue):
    if len(p_queue) == 0:
        return None
    min_index = 0
    min_priority = p_queue[0][0]
    for i, ele in enumerate(p_queue):
        if ele[0] < min_priority:
            min_priority = ele[0]
            min_index = i
    return p_queue.pop(min_index)


# peek function
def peek(p_queue):
    if len(p_queue) == 0:
        return "Nothing To Peek"
    min_index = 0
    min_priority = p_queue[0][0]
    for i, ele in enumerate(p_queue):
        if ele[0] < min_priority:
            min_priority = ele[0]
            min_index = i
    return "task peeked" , p_queue[min_index][1]

# check if empty
def is_empty(p_queue):
    return len(p_queue) == 0

# search by title (linear)
def search_for_task(p_queue, title):
    for i, task in enumerate(p_queue):
        if task[1].lower() == title.lower():
            return i
    return -1

# merge sort (by priority)
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge_list(left, right)

def merge_list(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][2] <= right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    return result

# Call the functions
while len(my_tasks) > 0:
    sorted_tasks = merge_sort(my_tasks)
    print("Sorted tasks:", sorted_tasks)
    print("Search result:", search_for_task(my_tasks, "a"))
    print("Task Completed is :" , complete_next_task(my_tasks))
    print(peek(my_tasks))
