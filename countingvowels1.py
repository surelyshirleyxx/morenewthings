name = input("Today you'll get to learn how many vowels are in the a sentence/word you input. Type your word/sentence here: ")
name = name.lower()
count_vowel = len([i for i in name if i in 'aeiou'])
count_constant = len([i for i in name if i in 'bcdfghjklmnpqrstvwxyz'])
print('Number of vowels in your word/sentence: ' + str(count_vowel) + '.' + ' The number of constants in your word/sentence: ' +str(count_constant))