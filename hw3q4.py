__author__ = "Ian Seal"

# list of all of the fusses
Book_O_Fuss = []
# number of edges connecting fusses
edges = 0


# Contains name of the Fuss, as well as number of friends
class Fuss(object):
    name = 0
    friends = 0

    def __init__(self, name):
        self.name = name
        self.friends = 0


# creates a new fuss, adds it to the book
def make_fuss(name):
    fuss = Fuss(name)
    Book_O_Fuss.append(fuss)


# increases the friend count of both fusses
def add_friend(fu, ff):
    fu.friends += 1
    ff.friends += 1


# checks to see if the fuss already exists
def check_doesnt_exists(name):
    for fl in Book_O_Fuss:
        if fl.name == name:
            return False
    return True


# finds a fuss given a name
def find_fuss(name):
    for ch in Book_O_Fuss:
        if ch.name == name:
            return ch


fussbook = open("network_instaface.txt", "r")

for line in fussbook:
    # separates the two fusses from the rest of the string, converts their name to int
    a = int(line.rstrip().split("is friends with")[0])
    b = int(line.rstrip().split("is friends with")[1])

    # check to see if the first fuss already exists
    if check_doesnt_exists(a):
        make_fuss(a)

    # check to see if the second fuss already exists
    if check_doesnt_exists(b):
        make_fuss(b)

    # increases friend count of both fusses by 1
    add_friend(find_fuss(a), find_fuss(b))

    # increases the number of edges
    edges += 1

# name of fuss with the most friends
max_friend = 0
# number of most friends for fuss
max_count = 0

# finds the fuss with the most friends
for f in Book_O_Fuss:
    if f.friends > max_count:
        max_friend = f.name
        max_count = f.friends

print("Number of nodes: " + str(len(Book_O_Fuss)) + "\n" + "Number of edges: " + str(edges) + "\n")
print("Most well connected person is " + str(max_friend) + " with " + str(max_count) + " friends\n")
