def remove_vowels(text):
  remove = ""
  for ch in text:
    if ch not in 'aeiou':
      remove = remove + ch
  return remove

text = input("Enter text: ")

print(remove_vowels(text))