def parent(i):
    return (i - 1) // 2

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def sift_down(i, n, a, swaps):
    min_index = i
    l = left_child(i)
    if l < n and a[l] < a[min_index]:
        min_index = l
    r = right_child(i)
    if r < n and a[r] < a[min_index]:
        min_index = r
    if i != min_index:
        a[i], a[min_index] = a[min_index], a[i]
        swaps.append((i, min_index))
        sift_down(min_index, n, a, swaps)

def build_heap(a):
    swaps = []
    n = len(a)
    for i in range(parent(n-1), -1, -1):
        sift_down(i, n, a, swaps)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input_type = input("Enter I for keyboard input or F for file input: ")

    # input from keyboard
    if input_type == 'I':
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type == 'F':
        file_name = input("Enter file name: ")

        with open(file_name, "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    else:
        print("Invalid input type")
        return

    # checks if length of data is the same as the said length
    assert len(data) == n
    assert len(data) == len(set(data))

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made
    print(len(swaps))

    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4*n, "Number of swaps exceeds 4n"

    # output all swaps

    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()