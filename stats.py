def words_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    
    count = {}

    for char in text.lower():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count

def dict_to_sorted_list(dictionary):

    def sort_on(item):
        return item["num"]

    sorted_list = []

    for pair in dictionary:
        sorted_list.append({"char": pair, "num": dictionary[pair]})
    sorted_list.sort(key=sort_on, reverse=True)
    
    return sorted_list