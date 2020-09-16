names = ['Sourabh', 'Gourav', 'Raj', 'Arpit']

l = []
for person in names:
    l.append(person)
print(l)

print([person for person in names])

l = []
for person in names:
    l.append(person + " has good boy")
print(l)

print([person + ' has good boy' for person in names])


movie_and_rating = {"KGF": 10, "Mirzapur": 10, "Avrudh": 8, "Jalebi": 3, "Machine": 4}
l =[]

for movie in movie_and_rating:
    if movie_and_rating[movie]>6:
        l.append(movie)
print(l)

print([movie for movie in movie_and_rating if movie_and_rating[movie]>6])
