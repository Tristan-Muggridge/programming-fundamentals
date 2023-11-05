
# In the previous lesson, we learned about variables and how they can be used to store data.

number_box_1 = 5
number_box_2 = number_box_1

print(number_box_1) # 5

number_box_2 = 10

print(number_box_1) # 5
print(number_box_2) # 10

# In the above example, we created two boxes.
# We put the number 5 in the first box.
# Then, we put the contents of the first box into the second box.

# However, when we changed the contents of the second box, the first box remained unchanged.
# This is because the second box contains a copy of the contents of the first box, and not the contents of the first box itself.

# This is because numbers are a "value" type of data.

# Let's try the same thing with text.

text_box_1 = "Hello"
text_box_2 = text_box_1

print(text_box_2) # Hello

text_box_2 = "Goodbye"

print(text_box_1) # Hello
print(text_box_2) # Goodbye

# In the above example, we created two boxes.
# We put the text "Hello" in the first box.
# Then, we copied the contents of the first box into the second box.

# However, when we changed the contents of the second box, the first box remained unchanged.
# This is because the second box contains a copy of the contents of the first box, and not the contents of the first box itself.

# This is because text is a "value" type of data.

# These are all examples of "value" types of data.
# Value types include: numbers, text, and True/False (boolean) data.

# Reference types of data are different.
# Reference types include: lists, dictionaries, and objects. We'll talk about these later.