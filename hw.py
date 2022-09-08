# 6KYU       https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.

#O(1 + n) => O(n)
             #O(1)
def solution(number):
    multiples = [] # O(n)
                    
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)

    return sum(multiples)

print(solution(15))



#8 KYU          https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

#O(n)
string =  "hello world"
              #O(n)
def solution(string):
    rev_string = len(string)
    result = string[rev_string ::-1]#O(n)
    return result

print(solution(string))



# 5 KYU       https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


text =  "hello world"

            #O(n)
def pig_it(text):
    pig = [] #O(n)
    pig_split = text.split(' ')
    for word in pig_split:
        if word.isalpha():
                pig.append(word[1::] + word[0] + 'ay')
        else:
            pig.append(word)
            
    return ' '.join(pig)

print(pig_it(text))





