blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
layers = 1
while layers <= blocks:
    height += 1
    blocks -= layers
    layers += 1

print("The height of the pyramid:", height)
