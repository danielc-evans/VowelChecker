#vowel checker

#define the vowels
vowels = set("aeiou")

#create an empty set for those vowels found
collected_vowels = set({})

#input and reformat user string
my_sentence = input("Enter your string:")
my_sentence = my_sentence.lower()

#walk along the string
for char in my_sentence:
    
    #is it in the list?
    if char in vowels:
        #add it
        collected_vowels.add(char)
        
#if our two sets have the same count
if len(collected_vowels) == len(vowels):
    print("String contains all vowels")
else:
    print("String only contains", "".join(collected_vowels))
                                    
