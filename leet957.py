def solution(cells, N):
    if not N:
        return cells
    tmp = []

    while 1:
        if cells in tmp:
            ind = tmp.index(cells)
            break
        cel = cells.copy()
        for i in range(8):
            if i == 0 or i == 7:
                cel[i] = 0
                continue

            if cells[i-1] == cells[i+1]:
                cel[i] = 1
            else:
                cel[i] = 0
        tmp.append(cells)
        cells = cel
        # print(cells)
        # N -= 1
    tmp = tmp[:ind]
    print(tmp)
    x = N % len(tmp)
    return tmp[x]
    # return cells
# solution([0,1,0,1,1,0,0,1], 7)
print(solution([0,1,0,1,1,0,0,1], 7))
