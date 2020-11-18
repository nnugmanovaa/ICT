dictionary = {
    1 : 'one',2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight',
    9 : 'nine', 10 : 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 
    50: 'fifty', 60: 'sixty',70: 'seventy',80: 'eighty',90: 'ninety', 0: 'zero'
}

def convert_to_words(n):
    if (n > 99):
        print(dictionary[int(n / 100)] + ' hundred ', end = '')
        n = n - int(n / 100) * 100
    try:
        print(dictionary[n])
    except KeyError:
        try:
            print(dictionary[n - n % 10] + ' ' + dictionary[n % 10])
        except KeyError:
            print('Number out of range')
number = int(input())
convert_to_words(number)
