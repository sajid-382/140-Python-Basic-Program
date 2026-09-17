'''
Please write a program to generate all sentences where subject is in ["I", "You"] and
verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
'''

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey","Football"]

sentences = []

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{sub} {verb} {obj}."
            sentences.append(sentence)

for sentence in sentences:
    print(sentence)