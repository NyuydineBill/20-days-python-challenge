def replace_word():
    word = 'This is python programming language'
    word_to_replace=str(input('which word do you want to replace'))
    replacement=str(input('enter the replacement'))
    print(word.replace(word_to_replace, replacement))
word = 'This is python programming language'
print('The sentence: ',word,'\n')
replace_word(word)