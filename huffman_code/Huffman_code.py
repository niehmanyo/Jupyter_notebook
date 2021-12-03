class node():
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None
        self.huff = ""


def find_symbol_frequency(str):  # This function is to find the frequency of each symbol and create two list,
    # one contains characters which exist in the str and there is no repeated elements
    # one contains frequency of each corresponding symbol
    s = list(set(str))
    frequency = []
    for i in range(len(s)):
        index = 0
        for j in range(len(str)):
            if (s[i] == str[j]):
                index += 1
        frequency.append(index)
    return s, frequency


def exchange(List, i, j):  # This function is to exchange two elements in the list
    temp = List[i]
    List[i] = List[j]
    List[j] = temp


def sort(symbol, frequency):  # Using InsertSort to sort the frequency list and symbol list
    for i in range(0, len(frequency)):
        min = frequency[i]
        index = i
        for j in range(i, len(frequency)):
            if (frequency[j] < min):
                min = frequency[j]
                index = j
        exchange(frequency, i, index)
        exchange(symbol, i, index)


def huffman(symbol, frequency):  # This function create a huffman tree and return the root
    List = []
    for i in range(len(symbol)):  # Create each node and store them in the List
        r = node(symbol[i], frequency[i])
        r.left = None
        r.right = None
        List.append(r)
    for i in range(len(symbol) - 1):  # We should leave the root in the List
        p = List.pop(0)
        q = List.pop(0)
        r = node("", q.frequency + p.frequency)
        r.left = p
        r.right = q
        index = 0
        for j in range(len(List)):
            if (r.frequency > List[j].frequency):
                index = j
        List.insert(index+1, r)  # To insert this node to the List so that we could create huffman tree
    return List.pop(0)


def preOrder(n, index, list1, list3):  # Using preOrder to store the huffman code of each element in list3
    if (n != None):
        if (n.symbol != ""):
            n.huff = index
            for i in range(len(list1)):
                if n.symbol == list1[i]:
                    list3[i] = index
        preOrder(n.left, index + "0", list1, list3)
        preOrder(n.right, index + "1", list1, list3)


def printHuffman(str, list1, list3):  # To print the huffman code of corresponding input string
    for i in range(len(str)):
        for j in range(len(list1)):
            if (str[i] == list1[j]):
                print(list3[j], end="")
    print("")


def code_each_symbol(list1, list3):
    for i in range(len(list1)):
        print(list1[i], ":", list3[i])


str1 = input("Please input the string:")
list1, list2 = find_symbol_frequency(str1)
# list1 is the character list with no repeated elements
# list2 is the list that presents frequency of each element
list3 = list1.copy()
## To create a list3 to save the huffman code with the same length
sort(list1, list2)
print(list1)
print(list2)
node1 = huffman(list1, list2)
preOrder(node1, "", list1, list3)
printHuffman(str1, list1, list3)
code_each_symbol(list1, list3)