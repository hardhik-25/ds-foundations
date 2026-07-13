def main(string):
    return first_last(string)
def first_last(word):
    first_char = word[0]
    last_char = word[len(word)-1]
    
    if first_char == last_char:
        return True
    else:
        return False
print(main("level"))

