def sort(arr):
    pass


def show(arr):
    for i in a:
        print(i, end=" ")
    print()

def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]  < arr[i-1]:
            return False

    return True

def main(*args):
    a = input()
    a.split(' ')

    sort(a)
    assert is_sorted(a)
    show(a)

if __name__ == "__main__":
    main(*args)
