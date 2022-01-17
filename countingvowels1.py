nname = input("Today you'll get to learn how many vowels are in the a sentence/word you input. Type your word/sentence here: ")
name = name.lower()
count = len([i for i in name if i in 'aeiou'])
print('Number of vowels in your word/sentence: ' + str(count))