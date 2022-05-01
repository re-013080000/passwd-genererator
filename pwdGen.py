#passwd generator in Python

import random as r

dico = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", ",;:!?./§*ù$µ%£&=*-+"]
pwd = []
ask = int(input("how many passwd do you want me to generate? "))
lenpw = int(input("how long do you want your password(s)? "))

#generate a passwd with a certain length
def generator(lenpw, mdp):
  if lenpw != 0:
    i = r.randint(0,3)
    mdp = mdp + dico[i][r.randint(0, len(dico[i])-1)]
    return generator(lenpw-1, mdp)
  else:
    return mdp

#compile a list with a certain amount of strings
for i in range(ask):
  pwd.append(generator(lenpw, ""))

#export as txt
with open('pwd.txt', 'a') as f:
    f.writelines('\n'.join(pwd))
