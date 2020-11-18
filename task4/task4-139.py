
def is_bingo(directory):
    diag_one = 0
    diag_two = 0
    cnt = 0
    row = 0
    for i in directory.values():
        if i.count(0) == 5:
            return True
        diag_one += i[cnt]
        diag_two += i[4-cnt]
        row += i[len(directory.values())-1]
        cnt+=1
    if diag_one == 0 or diag_two== 0 or row == 0:
            return True
    return False

directory = {
        'B' : [0, 0, 5, 0, 0],
        'I' : [2, 1, 3, 0, 5],
        'N' : [3, 2, 0, 4, 5],
        'G' : [0, 0, 3, 3, 5],
        'O' : [0, 2, 3, 4, 0]
}
print(is_bingo(directory))

directory = {
        'B' : [0, 0, 0, 0, 0],
        'I' : [2, 1, 3, 6, 5],
        'N' : [3, 2, 5, 4, 5],
        'G' : [0, 0, 3, 3, 5],
        'O' : [0, 2, 3, 4, 0]
}
print(is_bingo(directory))

directory = {
        'B' : [0, 0, 5, 0, 0],
        'I' : [2, 1, 3, 0, 0],
        'N' : [3, 2, 7, 4, 0],
        'G' : [0, 1, 3, 3, 0],
        'O' : [0, 2, 3, 4, 0]
}
print(is_bingo(directory))

directory = {
        'B' : [0, 0, 5, 0, 0],
        'I' : [2, 1, 3, 0, 3],
        'N' : [3, 2, 7, 4, 0],
        'G' : [0, 1, 3, 3, 2],
        'O' : [0, 0, 0, 0, 0]
}
print(is_bingo(directory))

