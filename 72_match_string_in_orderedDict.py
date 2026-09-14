from collections import OrderedDict

def check_order(string,refrence):
    string_dict = OrderedDict.fromkeys(string)
    refrence_dict = OrderedDict.fromkeys(refrence)
    
    return string_dict == refrence_dict

input_str = "hello world"
refrence = "helo wrld"

if check_order(input_str,refrence):
    print("The order of characters in the input string matches the reference string.")
else:
    print("The order of characters in the input string does not match the reference string.")