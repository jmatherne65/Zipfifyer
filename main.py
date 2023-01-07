import matplotlib.pyplot as plt
import numpy as np

print("Enter your statement:") #Ask the user for a statement
frequencies = [] #Create a list to store frequency of each word
x = (input()) #Obtain input from the user
result = x.split(" ") #Split the input into individual words
result.sort() #Sort words alphabetically
for i in range(len(result) - len(frequencies)): #Loop through the words
   if len(frequencies) == len(result) - 1: #When the amount of unique words is equal to the amount of words in the input, break 
    break
   else:
    count =  1 #Otherwise initialize count to 1
    for j in range(i+1, len(result)): #Loop through all subsequent words
      if j >= len(result): #If j is greater than the amount of words in the input, decrement j by 1
        j-=1
      if result[i] == result[j]: #If the two words are equal, increment count by 1 and remove one instance of the word.
        count+=1
        result.remove(result[j])
      else:  #Else, append the frequency to the list and break
        frequencies.append(count)
        break
frequencies.append(count) #Append the last frequency to the list
zr = [result for frequencies,result in sorted(zip(frequencies,result))] #Zip frequencies and result together and sort by frequency
frequencies.sort(reverse = True) #Sort frequencies in descending order
zr.reverse() #Reverse the sorted list of result
t = np.asarray(zr) #Convert the list of result into a numpy array
e = np.asarray(frequencies) #Convert the list of frequencies into a numpy array
plt.plot(t, e) #Plot the frequencies and the result
plt.show() #Show the plot
