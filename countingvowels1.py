name = input("Today you'll get to learn how many vowels are in the a sentence/word you input. Type your word/sentence here: ")
count = len([i for i in name if i in 'aeiouAEIOU'])
print('Number of vowels in your word/sentence: ' + str(count))