dictionary = {
    '.,?!:' : '1',
    'ABC' : '2',
    'DEF' : '3',
    'GHI' : '4',
    'JKL' : '5',
    'MNO' : '6',
    'PQRS' : '7',
    'TUV' : '8',
    'WXYZ' : '9',
    ' ' : '0'
}

result = ''
data = input().upper()
for i in data:
    for j in dictionary:
        if i in j:
            result += dictionary[j] * (j.find(i) + 1)
print(result)



