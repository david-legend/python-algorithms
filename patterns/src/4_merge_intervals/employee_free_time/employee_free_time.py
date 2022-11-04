def find_employee_free_time(schedules):
    result, merge = [], []

    for schedule in schedules:
        for interval in schedule:
            merge.append(interval)

    merge.sort(key=lambda x : x[0])
    start, end  = 0, 1
    for i in range(1, len(merge)):
        prev = i - 1
        if merge[i][start] > merge[prev][end]:
            result.append([merge[prev][end], merge[i][start]])
    
    return result


print(find_employee_free_time([[[1,3], [5,6]], [[2,3], [6,8]]]))
print(find_employee_free_time([[[1,3], [9,12]], [[2,4]], [[6,8]]]))
print(find_employee_free_time([[[1,3]], [[2,4]], [[3,5], [7,9]]]))