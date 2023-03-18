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
        try:
            with open(file_name, "r") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))

        except:
            print("Error reading or parsing file")
            return

    else:
        print("Invalid input type")
        return

    # checks if lenght of data is the same as the said lenght
    if len(data) != n:
        print("Number of elements does not match stated lenght")
        return
    if len(data) != len(set(data)):
        print("Duplicate elements found in data")
        return

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    print(f"Number of swaps made: {len(swaps)}")

    # this number should be less than 4n (less than 4*len(data))
    if len(swaps) > 4*n:
        print("Number of swaps exceeds 4n")
        return

    # output all swaps

    for i, j in swaps:
        print(f"Swaps {i} with {j}")

if __name__ == "__main__":
    main()