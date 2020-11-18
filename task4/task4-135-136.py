def to_dict(text):
    letterDict = {}
    cnt = 0
    for c in text:
        if c.isalpha():
            letterDict[cnt] = c
            cnt+=1
    return sorted(letterDict.values())
    
def main():
    print(to_dict(input().lower()) == to_dict(input().lower()))
    
 
if __name__ == '__main__':
    main()