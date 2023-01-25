import re

# patterns = ['#include "..\\WMarkPlcLFI174\\CWMarkTabPlcLfi174.h"\n','#include "..\\WMarkPlcLFI174\\CWMarkPlcLfi174.h"\n']
# text = "LFI174"

def ignore_case(looking_for, looking_in):
    for element in looking_in:
        z = re.findall(looking_for, element , re.I)
        if z:
            return z
        else:
            print('no match')



# ignore_case(text,patterns)