print("Hello World")

num_candidates = 4
winning_percentage = 73.81
candidate = "Diane"
won_election = True

help("keywords")

counties = ["Arapahoe","Denver","Jefferson"]

counties

print(counties)

print(counties[2])

print(len(counties))

counties[0:2]

counties.append("El Paso")

print(counties)

counties.insert(2,"Boulder")
counties.insert(2,"El Paso")

print(counties)

counties.remove('El Paso')
print(counties)

counties.pop(-1)
print(counties)

counties.remove("Boulder")

counties.insert(1,"El Paso")
counties.remove("Arapahoe")
print(counties)

counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
