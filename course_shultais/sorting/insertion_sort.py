import time

arr = [7,2,8,5,3,6]


def timer(active=True):
    def wrapper(func):
        if active:
            start_timer = time.time()
            func(arr)
            stop = time.time() - start_timer
            print(stop)
        else:
            return func

        return func

    return wrapper



def insertion_sort(arr):
    for i in range(len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and cur < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur


@timer(active=True)
def insertion_sort_v2(arr):
    i = 1
    while i < len(arr):
        j = i - 1

        while arr[j+1] < arr[j] and j >=0:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
        i += 1


# start_timer = time.time()
print(insertion_sort(arr))
# stop = time.time() - start_timer
print(arr)