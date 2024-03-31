def minimumBribes(q):
    swaps = 0
    start_ind = 0

    chaos = False
    while start_ind < len(q) and not(chaos):
        ind = start_ind
        sorted = True
        for val in q[start_ind:]:
            if val >= ind + 4:
                print("Too chaotic")
                chaos = True
                break
            if val > ind + 1 and val > q[ind+1]:
                swaps += 1
                q[ind], q[ind+1] = q[ind+1], q[ind] # swap back
            if q[ind] == ind + 1 and sorted:
                start_ind += 1
            else:
                sorted = False
            ind += 1
    if not(chaos):
        print(swaps)


if __name__ == '__main__':
    minimumBribes([2, 1, 5, 3, 4]) # print 3
    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]) # print 7
    
    


