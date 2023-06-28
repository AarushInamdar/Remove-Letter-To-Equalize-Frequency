'''Remove Letter To Equalize Frequency'''
import copy
def frequencyList(word):
     myDict={}
     for letters_index in range(len(word)):
        myDict[word[letters_index]] = word.count(word[letters_index])
     valuesFrequencyList = [x for x in myDict.values()]
     return valuesFrequencyList
def equalFrequency(word):
        """
        :type word: str
        :rtype: bool
        """            
        Flag = False
        for index in range(len(word)):
                newWord = word
                newWord = word.replace(word[index], '', 1)
                list_a = frequencyList(newWord)
                if all(ele == list_a[0] for ele in list_a):
                        Flag = True

        return Flag

print(equalFrequency('aazz'))
print(equalFrequency('abcc'))
print(equalFrequency('abcd'))
print(equalFrequency("cccd"))
print(equalFrequency("zz"))
