#dictionary = dict([(1, 5), (2, 4), (3, 7), (4, 5)])
#print(dictionary)
#dictionary[1] = 5
#print(dictionary)

#for d in dictionary:
#    print(d)

#for d in dictionary.values():
#    print("values: " + str(d))

#def func(d): 
      
#    for key in d: 
#        print("key:", key, "Value:", d[key]) 
#func(dictionary)

##################################################### 128
def reverse_lookup(dict, value):
    result = []
    for d in dict:
        if dict[d] == value:
            result.append(d)
    print(result)


def main():
    dictionary = dict([(1, 5), (2, 4), (3, 7), (4, 5)])
    reverse_lookup(dictionary, 5)
    reverse_lookup(dictionary, "nargiza")
    reverse_lookup(dictionary, 7)

if __name__ == '__main__':
    main()





