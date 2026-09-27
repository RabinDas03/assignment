def count_characters(char):
    count = 0

    for ch in char:
        count = count + 1

    return count

char = input("Enter a string: ")

print("Characters =", count_characters(char))