
def sort(arr):
    n = len(arr)
    for i in range(n):
        min_ = i
        for j in range(i+1, n):
            if a[j] < a[min_]:
                min_ = j

        a[min_], a[i] = a[i], a[min_]
