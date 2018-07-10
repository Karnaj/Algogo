import matplotlib.pyplot as plt

def zplot(f, a, b, n, style = '-', lw = '1', color = 'b'):
    x = []
    y = []
    abscisse = a
    pas  = (b - a)/ n
    for k in range(0, n + 1):
        x.append(abscisse)
        y.append(f(abscisse))
        abscisse += pas
    plt.plot(x, y, style, lw = lw, color = color)
