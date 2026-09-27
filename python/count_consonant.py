def count_vowels(vowel):
  count = 0
  for ch in vowel:
    if ch.lower() not in "aeiou":
      count = count+1
  return count

text = input("Enter a string: ")
print(count_vowels(text))