dictionary = dict([('A',"Newfoundland"), ('B', "Nova Scotia"), ('C', "PEI"), ('E',"New Brun"),
('G',"Quebec"), ('H',"Quebec"), ('J',"Quebec"), ('N',"Ontario"), ('K',"Ontario"), 
('M',"Ontario"), ('P',"Ontario"), ('R',"Manitoba"), ('S',"Saskatchewan"), ('T',"Alberta"),
('V',"British Columbia"), ('X',"Nothwest Terr"), ('Y',"Yukon")])

def find_postal(value, data):
    result = dictionary[value]
    if data == '0':
        print("rural " + str(result))
    else:
        print("urban " + str(result))

def main():
    text = input()
    text.upper()
    find_postal(text[0], text[1])

if __name__ == '__main__':
    main()