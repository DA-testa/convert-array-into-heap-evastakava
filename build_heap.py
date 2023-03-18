#python3

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        sift_down(i, n, data, swaps)

    return swaps


def sift_down(i, n, data, swaps):
    min_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(min_index, n, data, swaps)


def main():
    input_type = input().strip()
    #
    input_type = input("Enter I for keyboard input or F for file input: ")
    #
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
    

    assert len(data) == n
    assert len(data) == len(set(data))


    swaps = build_heap(data)


    print(len(swaps))
    assert len(swaps) <= 4 * n, "Number of swaps exceeds 4n"

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()