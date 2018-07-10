# Problème algorithmique 
#
# https://openclassrooms.com/forum/sujet/probleme-algorithmique

# Entrée  : deux entiers X et n
# Sortie  : nombre de manières de décomposer X en sommes de puissances
#           de n
#
# Exemple : X = 100
#           n = 2 
#           Sortie : 3 car 100 = 10^2
#                              = 6^2 + 8^2
#                              = 1^2 + 3^2 + 4^2 + 5^2 + 7^2

def f(X, n):
    T = [0 for i in range(X + 1)]
    T[0] = 0
    T[1] = 1
    j = 2
    for i in range(2, X + 1):
        r = 0
        for k in range(1, (i // 2) + 1):
            r += T[k]*T[i - k]
        if i == j**n:
            r += 1
            j += 1
        T[i] = r
    return T


def func(X, T):
    if X == 0:
        return 1
    if T == []:
        return 0
    if T[0] == X:
        return 1 + func(X, T[1::])
    return func(X - T[0], T[1::]) + func(X, T[1::])

def g(X, n):
    T = [1]
    i = 2
    result = 0
    while i**n <= X:
        T.append(i**n)
        i += 1
    for i in range(0, len(T)):
        result += func(X - T[i], T[i+1:])
    return result
    
print(g(400, 2))
