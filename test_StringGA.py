from StringGA import StringGA

g1 = StringGA()
g1.evolve()
print(list(g1._ascii_dict.keys())[list(g1._ascii_dict.values()).index('G')])
print((len(g1._ascii_dict)))
for i in g1._ascii_dict:
    if g1._ascii_dict[i] == 'G':
        print(i)
