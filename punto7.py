
from itertools import count


lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
for x in lista_1:
    for j in lista_2:
     if x == j:
         if x not in lista_3:
             lista_3.append(x)
print(lista_3)








