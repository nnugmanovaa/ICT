def main():
    letterDict = {}
    text = input()
    for c in text:
        if c.isalpha():
            letterDict[c] = 1
    print("unique = ", len(letterDict))
 
if __name__ == '__main__':
    main()