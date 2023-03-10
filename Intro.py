# Create a set
# Add at least 5 members to the set
# Remove at most 2 members from the set
# Iterate over the set and print its members
# Remove 482 from the set if it is present
# Remove 42 from the set even if it is not present

my_set = set()
for i in range(1, 6):
    my_set.add(i)

my_set.remove(3)
my_set.remove(1)

for i in my_set:
    print(i)

# If the item to remove does not exist, discard() will NOT raise an error.
my_set.discard(482)
my_set.discard(42)