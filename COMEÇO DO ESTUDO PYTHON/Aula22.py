# add (adicional), update (atualizou), clear, discard
# union | (une)
# intersection & (todos os elemntos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
l1 = ['Will', 'Cinthia', 'Sophia']
l2 = ['Will', 'Cinthia', 'Sophia','Will', 'Cinthia', 'Sophia']



if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')