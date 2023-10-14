tab=[]
for i in range (0,6) :
   n=int(input("taper un nombre :"))
   tab.append(n)
for b in range (0,5) :
  for i in range (b+1,6) :
    if tab[b]<tab[i] :
       m=tab[b]
       tab[b]=tab[i]
       tab[i]=m
print(tab)