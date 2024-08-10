import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetics = {row.letter:row.code for (index, row) in df.iterrows()}
print(phonetics)


def take_name():
    name = input("Enter your Name: ").upper()
    try:
        ur_code = [phonetics[letter] for letter in name]

    except KeyError:
        print("Provide only string values")
        take_name()

    else:
        print(ur_code)


take_name()
