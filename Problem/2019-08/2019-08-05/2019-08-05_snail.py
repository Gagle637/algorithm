# N = 5
# arr = [[1, 2, 3, 4, 5],
# [16, 17, 18, 19, 6],
# [15, 24, 25, 20, 7],
# [14, 23, 22, 21, 8],
# [13, 12, 11, 10, 9]]

N=7
arr = [[1,2,3,4,5,6,7],
[24,25,26,27,28,29,8],
[23,40,41,42,43,30,9],
[22,39,48,49,44,31,10],
[21,38,47,46,45,32,11],
[20,37,36,35,34,33,12],
[19,18,17,16,15,14,13]]

# N=6
# arr = [[1,2,3,4,5,6],
# [20,21,22,23,24,7],
# [19,32,33,34,25,8],
# [18,31,36,35,26,9],
# [17,30,29,28,27,10],
# [16,15,14,13,12,11]]


for idx in range(N-2):    
    for x in range(idx,N-idx):
        print(arr[idx][x], end = ' ')
        
    for y in range(idx+1,N-idx):
        print(arr[y][N-1-idx], end = ' ')

    for x in range(N-2-idx, idx, -1):        
        print(arr[N-1-idx][x], end = ' ')

    for y in range(N-1-idx, idx, -1):            
        print(arr[y][idx], end=' ')









        



