f1 = open('cezar.txt', 'r')
f2 = open('tlumaczenie.txt', 'w')

### definicje uzytecznych parametrow
nr_a = ord('a')
nr_z = ord('z')
ile_liter = nr_z - nr_a + 1
#print(nr_a, nr_z, ileznakow)
nr_A = ord('A')
nr_Z = ord('Z')


N = 2  ### przesuniecie; widze, ze jest 2, ale mozna by szukac jakas petla; ja to znalazlam tak:

# for N in range(1, 26):
    # print(chr( ord('V') - N ), chr( ord('j') - N ), chr( ord('g') - N ))
    # print(N)


znak = 'c'
#print('znak = ', c)


while znak:
    znak = f1.read(1) ###czyta po 1 znaku z pliku f1
    #print('znak = ', znak)
    if znak.isalpha():
        nr_znaku = ord(znak)
        
        if (znak.islower() and (nr_znaku - N) < nr_a) or (znak.isupper() and (nr_znaku - N) < nr_A) :
            znak = chr(nr_znaku - N + 26)
        else:
            znak = chr(nr_znaku - N)
    f2.write(znak)


