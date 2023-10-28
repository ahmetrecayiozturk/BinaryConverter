girdi = list(input("bir binary sayı dizisi giriniz"))
seçim = input("bir seçim yapınız: decimal, hexadecimal, octal")
#print(girdi)
binaries = []
for i in girdi:
    i = int(i)
    binaries.append(i)
#print(binaries)

def decimal_convert(girilen):
    üs = len(girilen)-1
    sum = 0
    while üs >= 0:
        for i in girilen:
            i = i*(2**üs)
            sum = sum + i
            üs = üs-1
    print(sum)

def hexadecimal_convert(girilen):
    reverse = reversed(girilen)
    reversebinary = list(reverse)
    #if len(reversebinary)%3!=0:
    while (len(reversebinary)%3!=0):
        reversebinary.append(0)
        added_zero = list(reversed(reversebinary))
        üs = len(reversebinary)-1
        sum = 0
        while üs >= 0:
           for i in added_zero:
            i = i * (8 ** üs)
            sum = sum + i
            üs = üs - 1
        print(sum)
    if len(reversebinary)%3==0:
        no_added_zero=list(reversed(reversebinary))
        üs = len(reversebinary)-1
        sum = 0
        while üs >= 0:
           for i in no_added_zero:
            i = i * (8 ** üs)
            sum = sum + i
            üs = üs - 1
        print(sum)



def octal_convert(girilen):
    reverse = reversed(girilen)
    reversebinary = list(reverse)
    # if len(reversebinary)%3!=0:
    while (len(reversebinary) % 4 != 0):
        reversebinary.append(0)
        added_zero = list(reversed(reversebinary))
        üs = len(reversebinary) - 1
        sum = 0
        while üs >= 0:
            for i in added_zero:
                i = i * (16 ** üs)
                sum = sum + i
                üs = üs - 1
        print(sum)
    if len(reversebinary) % 4 == 0:
        no_added_zero = list(reversed(reversebinary))
        üs = len(reversebinary) - 1
        sum = 0
        while üs >= 0:
            for i in no_added_zero:
                i = i * (16 ** üs)
                sum = sum + i
                üs = üs - 1
        print(sum)

if seçim == "decimal":
    decimal_convert(binaries)
if seçim == "hexadecimal":
    hexadecimal_convert(binaries)
if seçim == "octal":
    octal_convert(binaries)