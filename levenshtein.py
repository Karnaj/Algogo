def levenshtein(str1, str2):
    (l1, l2) = (len(str1), len(str2)) 
    T = [ [0 for i in range(l2 + 1)] for i in range(l1 + 1)]
    for i in range(l1 + 1):
        T[i][0] = i
    for j in range(l2 + 1):
        T[0][j] = j
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            c = int(str1[i - 1] != str2[j - 1])
            T[i][j] = min([T[i - 1][j - 1] + c, T[i][j - 1] + 1, T[i - 1][j] + 1])
    return T[l1][l2]
    
str1 = input("first word: ")
str2 = input("second word: ")
print(levenshtein(str1, str2))
