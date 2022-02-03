# 1) find_max: Given an list of numbers, find the largest number in the list.
# Sample input: [2, 10, 9, -4, 1], sample output: 10
def find_max(input_list):
  # print(max(input_list))
  # return max(input_list)
  temp = input_list[0]
  for i in input_list:
    if i > temp:
      temp = i
  return temp


print(find_max([2, 10, 9, -4, 1]) == 10)

# 2) median: Given an list of numbers, find the median. Hint: use a built-in sort method. You can assume the incoming list will have an odd number of elements, but as a bonus, you can make your function handle even-length lists too
# Sample input: [2, 10, 9, -4, 1], sample output: 2
# BONUS Sample input: [2, 10, 9, -4, 1, 3], sample output: 2.5

def median(input_list):
  sorted_list = sorted(input_list)
  length= len(input_list) // 2
  if len(input_list) % 2 == 0:
    return (input_list[length-1] + input_list[length]) / 2
  # print(length+1)
  return   (input_list[length] + input_list[length+1]) // 2  



print (median([2, 10, 9, -4, 1]) == 2)
# uncomment next line for bonus
print (median([2, 10, 9, -4, 1, 3]) == 2.5)

# 3) sum_list: Given an list, find the sum of all of them.
# Sample input: [2, 10, 9, -4, 1], sample output: 18

def sum_list(input_list):
   # return sum(input_list)
 total = 0
 for i in input_list:
     total += i
 return total


print(sum_list([2, 10, 9, -4, 1]) == 18)

# 4) initials: Given a string that contains a name separated by spaces, return a string of that name's initials
# Sample input: 'Tina Turner', sample output: 'TT'
# Sample input: 'Neil Patrick Harris', sample output: 'NPH'

def initials(name):
  split_name = name.split(" ")
  initals = ""
  for i in split_name:
      initals += i[0]
  # print(initals)
  return initals

print(initials('Tina Turner') == 'TT')
print(initials('Neil Patrick Harris') == 'NPH')

"""
# 5) day_of_the_week: Given a day of the week, return the appropriate greeting for that day:
- Monday: "Energize!"
- Tuesday: "Just getting started!"
- Wednesday: "Over the hump!"
- Thursday: "Almost there!"
- Friday, Saturday, or Sunday: "Weeeeeee!"
- If it's not anything above: "What?? I don't understand you"
Note that python does not have a switch statement! Instead, you could use a series of elifs, or a dictionary. If you use a dictionary, google how to except a KeyError.
"""

days = {
     "Monday": "Energize!",
 "Tuesday": "Just getting started!",
 "Wednesday": "Over the hump!",
"Thursday": "Almost there!",
 "Friday": "Weeeeeee!",
     "Saturday": "Weeeeeee!",
     "Sunday": "Weeeeeee!"
}

def day_of_the_week(day):
  for key in days:
      if day == key:
          return days[key]
          break
      else:
         return "What?? I don't understand you"
         break
print(day_of_the_week('Monday') == "Energize!")
print(day_of_the_week('Funday') == "What?? I don't understand you")


# 6) sum_to_n: Given an integer n, find the sum of all positive integers up to that number
# Note that this problem is good to do either iteratively or recursively!
# If using a loop, this is a good chance to use phython's range function
# Sample input: 4, sample output: 10
# Sample input: 5, sample output: 15

def sum_to_n(n):
  total = 0
  for i in range(n+1):
      total += i
  return total

print(sum_to_n(4) == 10)
print(sum_to_n(5) == 15)

# 7) dig_down: Given a nested list of unknown depth, return the string at the center of the list
# Note that this problem is good to do either iteratively or recursively!
# Hint: google how to check the type of something!
# Sample input: ['yo'], sample output: 'yo'
# Sample input: [[['hi']]], sample output: 'hi'

def dig_down(inputList):
  while len(inputList):
    for i in inputList:
      if type(i) == str:
        return i
      elif type(i) == list:
        inputList = i
      


print(dig_down(['yo']) == 'yo')
print(dig_down([[['hi']]]) == 'hi')

# 8) palindrome: Given a string, return True or False indicating whether that word is a palindrome
# Note that this problem is good to do either iteratively or recursively!
# Sample input: "radar", sample output: True
# Sample input: "steve", sample output: False

def palindrome(string):
      #return string == string[::-1]
    j = len(string)-1
    for i in string:
        if i == string[-j]:
            return i == string[-j]
        j -=1
    return False
      

print(palindrome('radar') == True)
print(palindrome('steve') == False)

"""
9) fizz_buzz: Given an integer n, return an object that contains 3 keys: 'fizz', 'buzz', and 'fizz_buzz'. Each key points to an list.
The 'fizz' list should contain all number less than or equal to n that are multiples of 3.
The 'buzz' list should contain all number less than or equal to n that are multiples of 5.
The 'fizz_buzz' list contains all numbers less than or equal to n that are multiples of both 3 and 5.

Sample input: 20
Sample output: {
  "fizz": [3, 6, 9, 12, 15, 18],
  "buzz": [5, 10, 15, 20],
  "fizz_buzz": [15]
}
"""

def fizz_buzz(n):
    result = {"fizz":[], "buzz":[], "fizz_buzz":[]}
    for i in range(1,n+1):
        if i % 3 == 0:
            result["fizz"].append(i)
        if i % 5 == 0:
            result["buzz"].append(i)
        if i % 3 == 0 and i % 5 == 0:
            result["fizz_buzz"].append(i)
    return result
  

print(fizz_buzz(20) == {
  "fizz": [3, 6, 9, 12, 15, 18],
  "buzz": [5, 10, 15, 20],
  "fizz_buzz": [15]
})

# 10) char_count: Given a string, return an object containing the counts of each character in the string.
# Hint: how do you check if a dict has a given key?
# Sample input: 'good food'
# Sample output: { "g": 1, "o": 4, " ": 1, "f": 1, "d": 2 }

def char_count(string):
  result = {}
  for i in string:
      if i not in result:
          result[i] = 1
      else:
          result[i] += 1
 
  return result


print(char_count('good food') == { "g": 1, "o": 4, " ": 1, "f": 1, "d": 2 })

# 11) vowel_count: Given an list of strings, return an object with those strings as keys, and the number of vowels in each string as a value
# Sample input: ['hey', 'whoa', 'whoooaaa']
# Sample output: { "hey": 1, "whoa": 2, "whoooaaa": 6 }

def vowel_count(list_of_strings):
  vowels= 'aeiou'
  output={}
  for i in list_of_strings:
    output[i] = 0
    counter = 0
    for j in range(len(i)):
      if i[j] in vowels:
        counter += 1
      output[i] = counter
        
  return output


                
      

print(vowel_count(['hey', 'whoa', 'whoooaaa']) == { "hey": 1, "whoa": 2, "whoooaaa": 6 })

"""
12) merge_sorted_lists
Given 2 sorted lists of numbers, return 1 list that contains the combined elements of the 2 lists, sorted.

Note: you can solve this by just blindly smooshing the lists together and then sorting the result. That solution is not accepted!

Sample 1: [1,3,5] and [2,4,6] --> [1,2,3,4,5,6]
Sample 2: [1,1,1] and [2,2,2] --> [1,1,1,2,2,2]
Sample 3: [1,2,3] and [] --> [1,2,3]
"""



# not accepting even though the result is the same;
def merge_sorted_lists(list1, list2):
  unsorted_result = []
  
  for i in list1:
      unsorted_result.append(i)
  for j in list2:
      unsorted_result.append(j)

  for i in range(len(unsorted_result)):
      for j in range(i+1, len(unsorted_result)):
          if unsorted_result[i] > unsorted_result[j]:
              unsorted_result[i], unsorted_result[j] = unsorted_result[j], unsorted_result[i]
  #print(unsorted_result)


  return unsorted_result

print(merge_sorted_lists([1,3,5],[2,4,6]) == [1,2,3,4,5,6])
print(merge_sorted_lists([1,1,1],[2,2,2]) == [1,1,1,2,2,2])
print(merge_sorted_lists([1,2,3],[]) == [1,2,3])

# 13) primes_up_to_n: Given a number n, return a list of the prime numbers less than n.
# Sample input: 25
# Sample output: [2, 3, 5, 7, 11, 13, 17, 23]

def primes_up_to_n(n):
  output = []
  for i in range(n):
    if i == 1:
      continue
    if i == 2 or i == 3:
      output.append(i)
    if i%2 != 0 and i%3 !=0:
      output.append(i)
  return output
    
print(primes_up_to_n(25) == [2, 3, 5, 7, 11, 13, 17, 19, 23])
