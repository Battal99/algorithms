#
# arr = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
#
# def swap(arr, i, j):
#     tmp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = tmp
#
# def threeWayPartition(arr):
#
#     pivot = 1
#     start = 0
#     end = len(arr) - 1
#     mid = 0
#
#     while mid <= end:
#         if arr[mid] < pivot:
#             swap(arr, end, mid)
#             end -= 1
#         elif arr[mid] > pivot:
#             swap(arr, start, mid)
#             start += 1
#             mid += 1
#         else:
#             mid += 1
#
#
#
# threeWayPartition(arr)
# print(arr)
nums = [1, 3, 5, 4, 8, 2, 4, 3, 6, 5]

def find_min_diff(nums, x, y):
    index_x = len(nums)
    index_y = len(nums)
    min_diff = 2000000
    for i in range(len(nums)):
        if nums[i] == x:
            index_x = i
            if index_x != len(nums):
                min_diff = min(min_diff, abs(index_x - index_y))
        if nums[i] == y:
            index_y = i
            if index_y != len(nums):
                min_diff = min(min_diff, abs(index_x - index_y))


    return min_diff

print(find_min_diff(nums, 3, 2))
