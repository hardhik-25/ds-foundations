def main(lis):
    list_dict(lis)
      
def list_dict(words):
    """
    Takes a list of words and returns a dictionary
    mapping each word to its length.
    
    Example:
        Input: ["cat", "elephant", "dog"]
        Output: {"cat": 3, "elephant": 8, "dog": 3}
    """  
    result={}
    for word in words:
        result[word]=len(word)
    print(result)

main(["cat", "elephant", "dog"])
