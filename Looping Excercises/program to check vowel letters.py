# program to check vowel letters in any sentences ...........
#..............................................
st = input("Enter your sentences to check vowel letters: ").upper()
vow = ("i, o, a, e, u").upper()

def vowel(sting):
    s = 0
    for i in sting:
      if(i in vow):
         s += 1
    return s

print(vowel(st))