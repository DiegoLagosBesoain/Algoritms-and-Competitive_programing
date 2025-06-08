import sys

def kadane_1d_min(arr):
    min_sum = current_sum = arr[0]
    start = end = s = 0
    for i in range(1, len(arr)):
        if current_sum > 0:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]

        if current_sum < min_sum:
            min_sum = current_sum
            start = s
            end = i
    return min_sum, start, end
def kadane_1d(arr):
    max_sum = current_sum = arr[0]
    start = end = s = 0
    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            s = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i
    return max_sum, start, end

def max_sum_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    final_left = final_right = final_top = final_bottom = 0

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]

            current_sum, top, bottom = kadane_1d(temp)
            if current_sum > max_sum or (
                current_sum == max_sum and 
                (bottom - top + 1) * (right - left + 1) > (final_bottom - final_top + 1) * (final_right - final_left + 1)#lo dejompara obtner el rectangulo mas grande posible
                ):
                max_sum = current_sum
                final_left = left
                final_right = right
                final_top = top
                final_bottom = bottom
    return {
        "max_sum": max_sum,
        "top": final_top,
        "bottom": final_bottom,
        "left": final_left,
        "right": final_right
    }
n=sys.stdin.readline().strip()
while n!="":
    n=int(n)
    matriz=[]
    for linea in range(n):
        matriz.append(list(map(int,sys.stdin.readline().strip().split())))  
    print(max_sum_rectangle(matriz)["max_sum"])
    n=sys.stdin.readline().strip()