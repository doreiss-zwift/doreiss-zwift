# Deduction process:
#
# 1. Fixed number of chars.
# 
# set(1) is the unique set containing (2 chars)
# set(4) is the unique set containing (4 chars)
# set(7) is the unique set containing (3 chars)
# set(8) is the unique set containing (7 chars) 
#
# set(2), set(3), set(5) each contain 5 chars
# set(0), set(6), set(9) each contain 6 chars
#
# 2. Deductions.
# 
# set(6) is the set X containing 6 chars for which set(7) intersect X != set(7)
# set(9) is the set X containing 6 chars for which set(4) intersect X == set(4)
# set(0) is the other set containing 6 chars
#
# Then of the remaining sets of 5 characters:
# set(3) is the set X containing 5 characters for which X intersect set(1) == set(1)
# set(2) is the set X containing 5 characters which is not set(3) for which X intersect set(9)  == X
# set(5) is the other set containing 5 characters.

def deduce_digits(digit_option, digits_output):
    set0, set1, set2, set3, set4, set5, set6, set7, set8, set9 = set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
    fiveCharSets = []
    sixCharSets = []

    for digit in digit_option:
        if len(digit) == 2 :
            set1 = digit
        elif len(digit) == 3 :
            set7 = digit
        elif len(digit) == 4 :
            set4 = digit
        elif len(digit) == 5 :
            fiveCharSets.append(digit)
        elif len(digit) == 6 :
            sixCharSets.append(digit)
        elif len(digit) == 7 :
            set8 = digit

    for sixCharSet in sixCharSets:
        if sixCharSet & set4 == set4:
            set9 = sixCharSet
        elif sixCharSet & set7 != set7:
            set6 = sixCharSet
        else:
            set0 = sixCharSet

    for fiveCharSet in fiveCharSets:
        if fiveCharSet & set1 == set1:
            set3 = fiveCharSet
        elif fiveCharSet & set9 == fiveCharSet:
            set2 = fiveCharSet
        else:
            set5 = fiveCharSet
                
    deduced_digits = [set0, set1, set2, set3, set4, set5, set6, set7, set8, set9]
    number_str = ""
    for output_digit in digits_output:
        for idx, digit in enumerate(deduced_digits):
            if digit == output_digit:
                number_str += str(idx)
                break
    return int(number_str)

def process_input(file_path):
    f = open(file_path)
    lines = f.readlines()
    digit_options = []
    digits_outputs = []
    for line in lines:
        tmp = [s.rstrip().lstrip() for s in line.split('|')]
        digit_options.append([set(s.strip()) for s in tmp[0].split(' ')])
        digits_outputs.append([set(s.strip()) for s in tmp[1].split(' ')])
    f.close()
    return digit_options, digits_outputs

if __name__ == '__main__':
    digit_options, digits_outputs = process_input('input.txt')
    sum = 0
    for i in range(len(digit_options)):
        sum += deduce_digits(digit_options[i], digits_outputs[i])
    print(sum)
