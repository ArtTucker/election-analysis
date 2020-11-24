print("Hello World")

num_candidates = 4
winning_percentage = 73.81
candidate = "Diane"
won_election = True

help("keywords")

counties = ["Arapahoe","Denver","Jefferson"]

print(counties)

print(counties[2])

print(len(counties))

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

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
len(counties_dict)

counties_dict.items()
counties_dict.keys()

sum(counties_dict.values())

counties_dict.get("Denver")
counties_dict('Denver')

voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})

len(voting_data)

voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
voting_data.remove("Arapahoe")