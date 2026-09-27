def count_word(text):
  space_count = 0  
  for char in text:
        if char == " ":
            space_count += 1
            
  return space_count + 1

user_sentence = input("Enter a sentence: ")

word_count = count_word(user_sentence)
print(word_count)