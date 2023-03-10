# We are going to represent bags using sets.
# Oliver's bag contains the following items
oliversBag = {'Laptop', 'Notebook', 'Pen', 'Sunglasses', 'Hand sanitizer'}

# Ethan's bag contains the following items
ethansBag = {'Sunglasses', 'Notebook', 'Phone'}

# Mia's bag contains the following items
miasBag = {'Laptop', 'Sunglasses', 'Hand sanitizer'}

# What are the common items in Oliver's and Ethan's bag?
# What are the items that in Oliver's bag but not in Mia's bag?
# What are the common items in Oliver's, Ethan's and Mia's bag?
print(oliversBag.intersection(ethansBag))
print(oliversBag - miasBag)
print((oliversBag.intersection(ethansBag)).intersection(miasBag))