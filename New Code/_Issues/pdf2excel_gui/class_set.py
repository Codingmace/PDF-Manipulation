import pdb
import math


# Function to check
# Log base 2
def Log2(x):
    if x == 0:
        return False

    return (math.log10(x) / math.log10(2))


# Function to check
# if x is power of 2
def isPowerOfTwo(n):
    if n == 0:
        return False
    else:
        return (math.ceil(Log2(n)) == math.floor(Log2(n)))


class entry_setting:
    def __init__(self, tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry):
        self.tax_bill_entry = tax_bill_entry          # bit 0 of entry_combination
        self.decl_form_entry = decl_form_entry        # bit 1 of entry_combination
        self.tax_ID_entry = tax_ID_entry              # bit 2 of entry_combination
        self.tax_amount_entry = tax_amount_entry      # bit 3 of entry_combination
        self.entry_combination = 0

    def set_current_entry(self, tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry):
        #  pdb.set_trace()
        self.tax_bill_entry = tax_bill_entry          # bit 0 of entry_combination
        self.decl_form_entry = decl_form_entry        # bit 1 of entry_combination
        self.tax_ID_entry = tax_ID_entry              # bit 2 of entry_combination
        self.tax_amount_entry = tax_amount_entry      # bit 3 of entry_combination
        self.entry_combination = 0

        if self.tax_bill_entry is True:
            self.entry_combination = self.entry_combination | 1
            # print("tax_bill_entry true & ec = ", self.entry_combination)
        else:
            self.entry_combination = self.entry_combination & 14    # 0b1110
            # print("tax_bill_entry false & ec = ", self.entry_combination)

        if self.decl_form_entry is True:
            self.entry_combination = self.entry_combination | 2
            # print("decl_form_entry true & ec = ", self.entry_combination)
        else:
            self.entry_combination = self.entry_combination & 13    # 0b1101
            # print("decl_form_entry false & ec = ", self.entry_combination)

        if self.tax_ID_entry is True:
            self.entry_combination = self.entry_combination | 4
            # print("tax_ID_entry true & ec = ", self.entry_combination)
        else:
            self.entry_combination &= 11    # 0b1011
            # print("tax_ID_entry false & ec = ", self.entry_combination)

        if self.tax_amount_entry is True:
            self.entry_combination = self.entry_combination | 8
            # print("tax_amount_entry true & ec = ", self.entry_combination)
        else:
            self.entry_combination &= 7     # 0b0111
            # print("tax_amount_entery false & ec = ", self.entry_combination)

        if isPowerOfTwo(self.entry_combination) is True:
            # print("<<<class_set.py>>>[true]self.entry_combination=",
            # self.entry_combination)
            return True
        else:
            # print("<<<class_set.py>>>[false]self.entry_combination=",
            # self.entry_combination)
            return False

    def get_current_setting(self):
        if isPowerOfTwo(self.entry_combination) is True:
            return True, self.tax_bill_entry, self.decl_form_entry, \
                self.tax_ID_entry, self.tax_amount_entry
        else:
            return False, self.tax_bill_entry, self.decl_form_entry, \
                self.tax_ID_entry, self.tax_amount_entry

    def clear_current_setting(self):
        self.tax_bill_entry = False
        self.decl_form_entry = False
        self.tax_ID_entry = False
        self.tax_amount_entry = False
        self.entry_combination = 0
        return self.tax_bill_entry, self.decl_form_entry, self.tax_ID_entry, \
            self.tax_amount_entry

""" for debug purpose only
    #
    # Test cases of this class
    #
    # pdb.set_trace()
    tax_bill_entry = False          # 稅單資料輸入
    decl_form_entry = False          # 報單資料輸入
    tax_ID_entry = False            # 統一編號輸入
    tax_amount_entry = True         # 報單金額輸入
    #    es = class_set.entry_setting(tax_bill_entry, decl_form_entry, tax_ID_entry,
    #                    tax_amount_entry)

    es = entry_setting(tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry)
    #  es.set_current_entry(tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry)
    es.set_current_entry(True, False, True, False)
    # value_es = es.get_current_setting()
    # print("Current entry setting:", value_es)
    valid_entry, tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry = es.get_current_setting()
    print("Valid entry:", valid_entry)
    print("tax_bill_entry:", tax_bill_entry)
    print("decl_form_entry:", decl_form_entry)
    print("tax_ID_entry:", tax_ID_entry)
    print("tax_amount_entry:", tax_amount_entry)

    tax_bill_entry, decl_form_entry, tax_ID_entry, tax_amount_entry = es.clear_current_setting()
    value_es = es.get_current_setting()
    print("Entry setting cleared:", value_es)
    print("tax_bill_entry:", tax_bill_entry)
    print("decl_form_entry:", decl_form_entry)
    print("tax_ID_entry:", tax_ID_entry)
    print("tax_amount_entry:", tax_amount_entry)
"""
