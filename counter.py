word_1 = 'Mississipi'
count_1 = {}

for letter in word_1:
    if letter not in count_1:
        count_1[letter] = 1
    else:
        count_1[letter] += 1

print(count_1)


print('Another way')

word_2 = 'Ananas'

count_2 = dict()

for letter in word_2:
    if letter not in count_2:
        count_2[letter] = 0
    count_2[letter] += 1

print(count_2)

print('Usando get')
word_3 = "mississippi"
counter_3 = {}

for letter in word_3:
    counter_3[letter] = counter_3.get(letter, 0) + 1

print(counter_3)
