def longest_words(text):
  words = text.split()
  longest=""
  
  for word in words:
    if len(word)>len(longest):
      longest=word
  return longest

sentence = str(input("Enter Your sentence:"))
print(longest_words(sentence))