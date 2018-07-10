
def rectangle(f, a, b, n):
    somme = 0
    pas = (b - a) / n
    x = a 
    for i in range(0, n): # On calcule la somme des f(x_i)
        somme += f(x)
        x += pas
    return somme * pas    # On retourne cette somme fois le pas
    

def trapèze(f, a, b, n):
    somme = (f(a) + f(b)) / 2   # On initialise la somme à (f(a) + f(b)) / 2
    pas = (b - a) / n
    x = a + pas                 # La somme commence à x_1 
    for i in range(1, n):       # On calcule la somme des f(x_i)
        somme += f(x)
        x += pas
    return somme * pas          # On retourne cette somme fois le pas


def simpson(f, a, b, n):
    pas = (b - a) / n
    somme = (f(a) + f(b)) / 2 + 2 * f(a + pas / 2)  # On initialise la somme
    x = a + pas           # La somme commence à x_1 
    for i in range(1, n): # On calcule la somme 
        somme += f(x) + 2 * f(x + pas / 2)
        x += pas
    return somme * pas / 3   # On retourne cette somme fois le pas / 3
