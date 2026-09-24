'''
A group of friends have decided to start a secret society. The name will be the first
letter of each of their names, sorted in alphabetical order. Create a function that takes
in a list of names and returns the name of the secret society.
Examples
society_name(["Adam", "Sarah", "Malcolm"]) 
➞ "AMS"
society_name(["Harry", "Newt", "Luna", "Cho"]) 
➞ "CHLN"
society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) --> 'CJMPRR'
'''

def secret_society(names):
    secret_name = [name[0] for name in names]
    return ''.join(sorted(secret_name))

print(secret_society(["Adam", "Sarah", "Malcolm"]))
print(secret_society(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))
