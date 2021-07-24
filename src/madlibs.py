# String concatenation

adj = input("adjective: ")
verb = input("verb: ")
verb2 = input("verb2: ")
famous_person = input("famous_person: ")

# madlib="Computer programming is so {adj}! It makes me so excited all the time because \
# I love to {verb}. Stay hydrated and {verb2} like you are {famous_person}!"\
# .format(adj = adj, verb=verb, verb2=verb2, famous_person=famous_person)

madlib=f"Computer programming is so {adj}! It makes me so excited all the time because \
        I love to {verb}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)
