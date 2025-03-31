from collections import Counter
my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3,3]

print(Counter(my_list))
#Counter({1: 5, 3: 5, 2: 4})

my_list = ['a', 'a', 10, 10, 10]
print(Counter(my_list))


print(Counter('aaaaabbbbbbcccccdddd'))
# Counter({'b': 6, 'a': 5, 'c': 5, 'd': 4})

sentence = "How many times does each word show up iun this sentence with a word"
print(sentence.lower().split())

letters = 'aaabbbbccccdddd'
c = Counter(letters)
print(c.most_common(2))

elements_list = list(c)

from collections import defaultdict
d = {'a': 10}
print(d)
print(d['a'])

#d['WRONG'] #KeyError: 'WRONG'
d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
print(d['WRONG'])

mytupple = (10, 20, 30)
print(mytupple[0])

from collections import namedtuple
Dog = namedtuple('Dog', ['age', 'bread', 'name'])
sammy = Dog(age=5, bread='Husky', name='Sam')
print(type(sammy)) #<class '__main__.Dog'>

print(sammy.age)
print(sammy.bread)
print(sammy.name)
print(sammy[0])