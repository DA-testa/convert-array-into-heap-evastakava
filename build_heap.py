#python3

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        sift_down(i, data, swaps)
    
    return swaps


def sift_down(i, data, swaps):

    left_child = 2 * i + 1
    right_child = 2 * i + 2
    min_index = i
    if left_child < len(data) and data[left_child] < data[min_index]:
        min_index = left_child
    if right_child < len(data) and data[right_child] < data[min_index]:
        min_index = right_child

    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(min_index, data, swaps)


def main():
    input_type = input().strip()

    if input_type == 'I':
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        assert len(data) == len(set(data))
        swaps = build_heap(data)

    elif input_type == 'F':
        with open('input.txt', 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.realine().strip().split()))
            assert len(data) == n
            assert len(data) == len(set(data))
            swaps = build_heap(data)
            with open('output.txt', 'w') as out_f:
                out_f.write(str(len(swaps)) + '\n')
                for i, j in swaps:
                    out_f.write(str(i) + ' ' + str(j) + '\n')
    
    
if __name__ == "__main__":
    main()
