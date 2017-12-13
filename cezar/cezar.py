f1 = open('cezar.txt', 'r')
f2 = open('tlumaczenie.txt', 'w')

### definicje uzytecznych parametrow
nr_a = ord('a')
nr_z = ord('z')
ile_liter = nr_z - nr_a + 1
nr_A = ord('A')
nr_Z = ord('Z')

przesuniecie = 2
# widze, ze jest 2, ale mozna by szukac jakas petla; ja to znalazlam tak:
# for przesuniecie in range(1, 26):
    # print(chr(ord('V') - przesuniecie), chr(ord('j') - przesuniecie), chr(ord('g') - przesuniecie))
    # print(przesuniecie)

znak = 'c'

while znak:
    znak = f1.read(1) # czyta po 1 znaku z pliku f1
    if znak.isalpha():
        nr_znaku = ord(znak)
        if (znak.islower() and (nr_znaku - przesuniecie) < nr_a) or (znak.isupper() and (nr_znaku - przesuniecie) < nr_A):
            znak = chr(nr_znaku - przesuniecie + 26)
        else:
            znak = chr(nr_znaku - przesuniecie)
    f2.write(znak)
