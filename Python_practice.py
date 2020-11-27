counties = ["Arapahoe","Denver","Jefferson"]

if counties[1] == 'Denver':
    print(counties[1])

if 'El Paso' in counties:
    print('El Paso is in the list of counties.')
else:
    print('El Paso is not in the list of counties.')

if 'Arapahoe' in counties or 'El Paso' in counties:
    print('Either Arapahoe or El Paso are in the list of counties.')
else:
    print('Either Arapahoe or El Paso are not in the list of counties.')

if 'Arapahoe' in counties and 'El Paso' not in counties:
    print('Only Arapahoe is in the list of counties.')
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list.')

print("     ")

for county in counties:
    print(county)

print("        ")

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(counties_dict[county])