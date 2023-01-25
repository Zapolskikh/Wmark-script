import re

def ignore_case(looking_for, looking_in):
    for element in looking_in:
        z = re.findall(looking_for, element , re.I)
        if z:
            return z
        else:
            print('no match')
