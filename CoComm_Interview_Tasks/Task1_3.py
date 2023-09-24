#Task 1.3
encoded_lists = [
    [1, 2, 3, 4, 6],
    [5, 7, 8, 9, 15],
    [12, 14, 16, 18],
    [10, 11, 12, 13, 16, 17, 18, 20]
]

def explode_chains(encoded_lists):
    list_of_exploded_chains=[]
    def find_consecutive_sequence(chain):
        for i in range(len(chain) - 2):
            if chain[i] + 1 == chain[i + 1] and chain[i + 1] + 1 == chain[i + 2]:
                return i
        return -1
    
    def explode_chain(chain, index):
        return chain[:index] + chain[index + 3:]
    
    for encoded_chain in encoded_lists:
        exploded_chain = encoded_chain

        index = find_consecutive_sequence(exploded_chain)
        while index != -1:
            exploded_chain = explode_chain(exploded_chain, index)
            index = find_consecutive_sequence(exploded_chain)
        list_of_exploded_chains.append(exploded_chain)

    return list_of_exploded_chains
result = explode_chains(encoded_lists)
print(result)
