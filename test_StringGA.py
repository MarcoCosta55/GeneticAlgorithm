from StringGA import StringGA

g1 = StringGA()
g1.evolve()
print((len(g1._ascii_dict)))
for i in g1._ascii_dict:
    if g1._ascii_dict[i] == 'G':
        print(i)
