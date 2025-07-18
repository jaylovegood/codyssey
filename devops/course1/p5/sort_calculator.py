def merge(arr1, arr2):
    pass

def mergesort(arr):
    pass


def main():
    try:
        arr = list(map(float, input().split()))
    except:
        print("Invalid input.")
        return

    if not arr:
        print("Invalid input.")
        return
    
    sorted_arr = mergesort(arr)

    print(f"Sorted: {" ".join(sorted_arr)}")


if __name__=="__main__":
    main()