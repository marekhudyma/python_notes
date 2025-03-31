text = "The agent's phone number is 408-555-1234. Call soon!"
print('phone' in text)

import re
pattern = 'phone'
print(re.search(pattern, text))

pattern = 'NOT IN TEXT'
print(re.search(pattern, text))

pattern = 'phone'
match = re.search(pattern, text)
print(match)
print(match.span())
print(match.start())
print(match.end())

text = 'my phone once, my phone twice'
print(match)
print(match.span())
print(match.start())
print(match.end())

matches = re.findall('phone', text)
for match in re.finditer('phone', text):
    print(match)
    print(match.start())
import re

#\d - a digit
#\w - alphanumeric
#\s - white space
#\D - a non digit
#\W - non-alphanumeric
#\S - non-whitespace

text = 'My phone number is 408-555-1234'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text) # r - for regular expression
print(phone.group())

# + occurs one or more times
# {3} occurs exactly 3 times
# {2,4} occurs 2 to 4 times
# {3,} occurs 3 or more
# * occurs zero or more times
# ? once or none

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(phone_pattern, text)
print(result.group())
print(result.group(1)) # first index not from 0!
print(result.group(2))
print(result.group(3))

re.search(r'cat|dog', 'Thr cat is here')
result = re.findall(r'...at', 'The cat in the hat sat there.') # . is a wildcard here
print(result) # ['e cat', 'e hat']

result = re.findall(r'^\d', '1 is a number') # starts
print(result) # ['1']

result = re.findall(r'\d$', '1 is a number. 2') # ends
print(result) # ['2']

phase = 'There are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]'
result = re.findall(pattern, phase)
print(result)

phase = 'There are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
result = re.findall(pattern, phase)
print(result)

test_phrase = 'This is a string. But it has punctuation. How can we remove it?'
result = re.findall(r'[^!.? ]+', test_phrase)
print(result)

print(' '.join(result))