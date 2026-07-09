def stringreverse(str):
    result = ""
    for i in range(len(str)-1,-1,-1):
        result = result + str[i]
    return result
print(stringreverse("LetsFUckingGO"))