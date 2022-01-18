def interval_intersection(interval_a, interval_b):
    result = []
    i, j, start, end = 0, 0, 0, 1
    
    while i < len(interval_a) and j < len(interval_b):
        a_overlaps_b = interval_a[i][start] >= interval_b[j][start] and \
                       interval_a[i][start] <= interval_b[j][end]
                       
        b_overlaps_a = interval_b[j][start] >= interval_a[i][start] and \
                       interval_b[j][start] <= interval_a[i][end]
                       
        if (a_overlaps_b or b_overlaps_a):
            new_start = max(interval_a[i][start], interval_b[j][start])
            new_end = min(interval_a[i][end], interval_b[j][end])
            result.append([new_start, new_end])
            
        if interval_a[i][end] < interval_b[j][end]:
            i += 1
        else:
            j += 1
            
    return result       
            
print(interval_intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
print(interval_intersection([[1, 3], [5, 7], [9, 12]], [[5, 10]]))