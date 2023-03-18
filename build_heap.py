#python3

def heapify(data, i, n, swaps):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and data[l] < data[smallest]:
        smallest = l

    if r < n and data[r] < data[smallest]:
        smallest = r

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        heapify(data, smallest, n, swaps)


def build_heap(data):

    n = len(data)
    swaps = []

    for i in range(n // 2, -1, -1):
        heapify(data, i, n, swaps)

    return swaps





def main():

    input_type = input("Enter I for keyboard input or F for file input: ").strip()

    if input_type.lower() == 'i':
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type.lower() == 'f':
        file_name = input("Enter file name: ").strip()
        try:
            with open(file_name, "r") as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().split()))

        except OSError as e:
            print(e)
            return

    else:
        print("Invalid input type")
        return

    assert len(data) == n, "Data length does not match input size"
    assert len(data) == len(set(data)), "Input data contains duplicates"

    swaps = build_heap(data)


    print(len(swaps))
    assert len(swaps) <= 4 * n, "Number of swaps exceeds 4n"

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()