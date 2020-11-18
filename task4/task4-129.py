import random
def two_dice_roll():
    dice_1 = random.randrange(6) +1
    dice_2 = random.randrange(6) +1
    return dice_1 + dice_2
 
def main():
    result = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

    for turn in range(1000):
        answer = two_dice_roll()
        result[answer] += 1

    print("Total".rjust(16),"|", "Simulated %".rjust(16),"|", "Expected %".rjust(16))
    print("-------------------------------------------------------")
    for n in range(2,13):
        sim_result = str("%.2f"%(result[n]/1000*100))
        if n <= 7:
            exp_result = str("%.2f"%((n-1)/36*100))
        else: 
            exp_result = str("%.2f"%((12-n+1)/36*100))
        print(str(n).rjust(16),"|",sim_result.rjust(16),"|",exp_result.rjust(16))
 
if __name__ == '__main__':
    main()