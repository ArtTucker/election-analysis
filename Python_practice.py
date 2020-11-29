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

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

print("      ")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_data in voting_data:
    print(f"{county_data.get('county')} county has {county_data.get('registered_voters'):,} registered voters.")

print("        ")

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

