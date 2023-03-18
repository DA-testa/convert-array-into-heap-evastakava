#python3

def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        while True:
            left_child = 2*i+1
            right_child = 2*i+2
            if left_child < len(data) and data[left_child] < data[i]:
                min_inx = left_child
            else:
                min_inx = i
            if right_child < len(data) and data[right_child] < data[min_inx]:
                min_inx = right_child
            if min_inx == i:
                break
            swaps.append((i, min_inx))
            data[i], data[min_inx] = data[min_inx], data[i]
            i = min_inx

    return swaps





def main():
    
    input_type = input("Enter I for keyboard input or F for file input: ").strip()
    if input_type.lower() == 'f':
        file_name = input("Enter file name: ").strip()
        try:
            with open(file_name, "r") as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().split()))
                swaps = build_heap(data)
                print(len(swaps))
                for i, j in swaps:
                    print(i, j)
        except OSError as e:
            print(e)

    if input_type.lower() == 'i':
        n = int(input())
        data = list(map(int, input().split()))
        
    assert len(data) == n



    swaps = build_heap(data)


    print(len(swaps))



    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()