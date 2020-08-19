print("Huffman Compression Program")
print("********************************")
my_string = input("Please enter a string to compress>>>")
len_my_string = len(my_string)
print("your message is :")
print(my_string)
print("Your data is", len_my_string*8,"bits long")


#creates a list of characters and their frequency and a list of characters in use
letters = []
only_letters = []
for letter in my_string:
    if letter not in letters:
        freq = my_string.count(letter)
        letters.append(freq)
        letters.append(letter)
        only_letters.append(letter)
#      generates base-level nodes for the huffman tree frequency amd letter

nodes = []
while len(letters)>0:
    nodes.append(letters[0:2])
    letters = letters[2:]

nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)
def combine(nodes):
    pos = 0
    newnode = []
    if len(nodes)>1:
        nodes.sort()
        nodes[pos].append("0")
        nodes[pos + 1].append("0")
        combined_node1 = (nodes[pos][0] + nodes[pos+1][0])
        combined_node2 = (nodes[pos][1] + nodes[pos + 1][1])
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes = []
        newnodes.append(newnode)
        newnodes = newnode + nodes[2:]
        nodes = newnodes
        huffman_tree.append(nodes)
        combine(nodes)
        return huffman_tree


newnodes = combine(nodes)

huffman_tree.sort(reverse= True)
print("Here is the huffman Tree, showing the merged nodes and binary pathways")

check
