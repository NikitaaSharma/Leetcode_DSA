def countOverlappingIntervals(intervals):
    #sort the lists inside based on the end time
    intervals.sort(key= lambda x:x[1])
    prev_interval = 0
    count_overlapping = 0

    for interval in range(1, len(intervals)):
        # if end time of prev meeting is greater than the current's start time, it is there is an overlap
        if intervals[prev_interval][1] > intervals[interval][0]:
            count_overlapping +=1
        else:
            # else move the prev interval forward
            prev_interval = interval
    return count_overlapping

intervals = [[1,2],[2,3],[3,4],[1,3],[1,4]]
res = countOverlappingIntervals(intervals)
print(f'No. of overlapping intervals -> {res}')

