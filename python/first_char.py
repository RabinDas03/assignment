def first_character(text):
  for ch in text:
    print(f"'{ch}' is the first character")
    break

text = str(input("Enter your text:"))

first_character(text)