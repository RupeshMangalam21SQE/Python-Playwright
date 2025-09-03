# 3. Lambda for Sorting
people = [{'name': 'A', 'age': 30}, {'name': 'B', 'age': 25}]
people.sort(key=lambda person: person['age'])
print(people)

