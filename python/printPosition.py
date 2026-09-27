# def display_position(text):
#   for index, value in enumerate(text,1):
#     print(index,value)
# text = input("Enter text: ")
# display_position(text)
#--------------------------------------
def display_position(text):
  for i in range(len(text)):
    print(i,text[i])

user_input = str(input("enter your string:"))
display_position(user_input)