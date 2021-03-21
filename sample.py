#3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
sample = [1,2,3,4,5,6,7,8,9]
for x in range(len(sample)-2):
    print(sample[2])
    sample.remove(sample[2])
    print(sample)
    print("Adding extra line")
    if len(sample)<2 :
        print(sample)
        print("Adding extra line 2")
