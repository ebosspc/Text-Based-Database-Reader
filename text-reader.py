# Open a file called numbers.txt to be read from and associate it with inFile.
inFile = open('numbers_list.txt')
#Read the first number from the file and store it in the variable numString
numString = inFile.readline(1)
#Create an empty list. Call the list numList
numList = []
 
#Ensures that the read nteger is infact an integer and not a string
 
while (numString != ""): #Explain what this line of code does
    #Write the line of code that adds the value stored in numString to the list
    numString = int(numString)
    numList.append(numString)
    #after converting it to an integer
 
    #Read the next number from the file
    next_index = numList.index(numString + 1)
    numList.readline(next_index)
#Close the input file
inFile.close()
#Print the numbers in the list
print(numList)
#Sort the numbers
numList.sort()
#Print the numbers again
print(numList)
#Open a file called numbers.txt to be written to and associate it with outFile
outFile = open('numbers_list.txt')
outFile.write(numList, 'w')
#What does this code do?
#
for x in range(len((numList))):
    outFile.write(str(numList[x]) + '\n')
 
#Close the output file
outFile.close()
