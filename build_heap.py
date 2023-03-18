#python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    for i in range(n // 2, -1, -1):
        j = 1
        while True:
            left_child = 2*j+1
            right_child = 2*j+2
            if left_child < n and data[left_child] > data [j]:
                j = left_child
            if right_child < n and data[right_child] > data[j]:
                j = right_child
            if i != j:
                data[i], data[j] = data[j], data[i]
                swaps.append((i, j))
                i = j
            else:
                break

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

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    assert len(data) == len(set(data))

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    print(len(swaps))
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4*n, "Number of swaps exceeds 4n"


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()