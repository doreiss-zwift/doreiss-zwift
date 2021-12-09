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
# {e} is set(8) less set(9)
# {a} is set(7) less set(1)
# {g} is set(8) less set(4) less {a} less {e} 
# {f} is set(6) intersect set(1)
# {c} is set(1) less {f}
# So we know all the signal maps except for {b} and {d}.
#
# From the digits containing 5 characters we can identify:
# set(2) and set(3) contains {d} but not {b}
# set(5)            contains {b}     and {d}
#
# If we query these sets for the first unknown char and we get 2 hits, then we know its a {d}.
# On the other hand if we get 1 hits, we know its a {b}.
# We can then construct the remaining sets explictly.
# set(2) = {a, c, d, e, g}
# set(3) = {a, c, d, f, g}
# set(5) = {a, b, d, f, g}

def deduce_digits(digit_option, digits_output):
    sigA, sigB, sigC, sigD, sigE, sigF, sigG = set(), set(), set(), set(), set(), set(), set()
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
        if sixCharSet.intersection(set4) == set4:
            set9 = sixCharSet
        elif sixCharSet.intersection(set7) != set7:
            set6 = sixCharSet
        else:
            set0 = sixCharSet

    sigE = set8 - set9
    sigA = set7 - set1
    sigG = set8 - set4 - sigA - sigE
    sigF = set6 & set1
    sigC = set1 - sigF
    knownChars = sigA | sigC | sigE | sigF | sigG
    unknownChars = set8 - knownChars
    for char in unknownChars:
        hits = 0
        for fiveCharSet in fiveCharSets:
            if char in fiveCharSet:
                hits += 1
        if hits == 1:
            sigB = set(char)
        else:
            sigD = set(char)
    
    set2 = sigA | sigC | sigD | sigE | sigG
    set3 = sigA | sigC | sigD | sigF | sigG
    set5 = sigA | sigB | sigD | sigF | sigG

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
