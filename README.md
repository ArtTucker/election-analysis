# Election Analysis
An analysis of election data with Python 3

## Project & Challenge Overview
In this exercise a Colorado Board of Elections employee requested an election audit of a recent local congressional election. The raw data was provided as a CSV (comma separated values) file, consisting of a list of unique ballot IDs, the counties in which the votes were cast, and the names of the candidates for who the votes were cast.

![Raw Election Data in CSV format](analysis/election_results_csv.png)

Our job was to take the information provided and perform the following tasks:
- Calculate the total number of votes cast in the election.
- Analyze data about the candidates, including:
    - building a complete list of candidates who received votes;
    - calculate the number of votes for each candidate, and their percentage of total votes cast;
    - determine the winner of the election based on popular vote;
- Analyze data about the counties, including:
    - building a complete list of counties in which votes were cast;
    - calculate the number of votes cast in each county, and their percentage of total votes cast;
    - determine which county had the largest voter turnout.

Once all this information was calculated, it needed to be output to both the terminal and saved to a text file.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.0, Visual Studio Code 1.51.1

## Audit Results
The analysis of the election data showed the following information:
![Election Results as printed to the Terminal](analysis/election_results_terminal.png)

As indicated in the screenshot shown above, of the results printed to the terminal:
- There were 369,711 votes cast in the election.
- The county turnout numbers were:
    - Denver had the most voters, with 82.8% of total turnout, at 306,055 votes.
    - Jefferson had the second-most voters, with 10.5% of turnout, at 38,855 votes.
    - Arapahoe had the least voters, with 6.7% of turnout, at 24,801 votes.
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote, at 85,213 votes.
    - Diana DeGette received 73.8% of the vote, at 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote, at 11,606 votes.
- The winner of the election was:
    - Diana DeGette

## Election Audit Summary
This analysis program is basic enough that it should be usable on any future (or past) election results, as long as the data is presented in a similarly formatted CSV file. The number of voting ballots, different candidate names, or different counties listed should not prove to be limiting factors. However, performance may be hindered or slowed by significantly larger datasets (perhaps at multiple millions of entries or more).

If the source data also included municipalities or voting districts in the CSV file, a potential easy improvement on this code could also allow for ranking of those districts by turnout. The only needed additions would be:
- the declaration of new variables (related to the metrics in question),
- a new "decision statement" to run through the values by row,
- a new for loop to calculate totals, percentages, and highest values,
- a new print statement to declare largest values.

Another alteration to consider would be to have the program send out summary emails (to the Board of Elections or other officials) once the analysis was finished. A thorough guide can be found [here](https://thepythonguru.com/sending-emails-in-python-tutorial-with-code-examples/), but the basic process would be to:
- `import smtplib`,
- setup your SMTP mail server, with login credentials,
- provide a list of email recipients, either hardcoded into the script or via an external txt file,
- hardcoded the message to send -- in this case, the analysis summary,
- script some feedback statements so you know if the messages were successfully sent or not.

Once these changes are made, all you should need to do is run the script... and the power of democracy is at your fingertips.