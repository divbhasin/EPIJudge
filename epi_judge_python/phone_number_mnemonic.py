from test_framework import generic_test, test_utils

mappings = {"2": ['A', 'B', 'C'], \
        "3": ['D', 'E', 'F'], \
        "4": ['G', 'H', 'I'], \
        "5": ['J', 'K', 'L'], \
        "6": ['M', 'N', 'O'], \
        "7": ['P', 'Q', 'R', 'S'], \
        "8": ['T', 'U', 'V'], \
        "9": ['W', 'X', 'Y', 'Z']}

def permute(phone, pos, i, curr):
    if i == len(phone):
        pos.append(curr)
        return

    num = phone[i]
    if num != '0' and num != '1':
        for char in mappings[num]:
            permute(phone, pos, i+1, curr+char)
    else:
        permute(phone, pos, i+1, curr+num)

def phone_mnemonic(phone_number):
    pos = []
    permute(phone_number, pos, 0, "")
    return pos 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
