
# Huffman Encoding using Greedy Method

import heapq

def huffman(characters, frequencies):
    heap = []

    for i in range(len(characters)):
        heapq.heappush(heap, (frequencies[i], characters[i]))

    while len(heap) > 1:
        f1, left = heapq.heappop(heap)
        f2, right = heapq.heappop(heap)

        new_node = (left, right)
        heapq.heappush(heap, (f1 + f2, new_node))

    def generate_codes(node, code=""):
        if isinstance(node, str):
            print(node, ":", code)
            return

        generate_codes(node[0], code + "0")
        generate_codes(node[1], code + "1")

    print("Huffman Codes:")
    generate_codes(heap[0][1])


# Main Program
characters = ['A', 'B', 'C', 'D', 'E', 'F']
frequencies = [5, 9, 12, 13, 16, 45]

huffman(characters, frequencies)
