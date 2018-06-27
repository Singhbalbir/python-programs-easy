'''
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score.
You are given n scores.
Store them in a list and find the score of the runner-up.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
'''
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    max = arr[0]

    for i in range(len(arr)):
        if arr[i] != max and i < len(arr):
            print(arr[i])
            break
        elif arr[i] != max and i == len(arr):
            print(max)
            break
