from os import remove


numeros = list(range(1,101))
for x in numeros:
   if x%2 == 0:
       numeros.remove(x)
       

print(sum(numeros))


   
  


