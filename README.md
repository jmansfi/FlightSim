# FlightSim.py

This is a project designed for simulating an entire US Quidditch Nationals tournament based on the predicted format for the cancelled 2020 US Quidditch Cup 13. This was used for The Eighth Man's [Quarantine Cup project](http://www.eighthman.com/2020/03/24/the-nationals-that-wasnt/) in 2020.

## Description

This file uses the 48 teams qualified for US Quidditch Cup 13 and their corresponding Elo values to run a simulation of that tournament. These teams are organized into six flights of eight teams, as determined by that year's gameplay. This should be easily convertible to other similar Swiss-style tournaments, and many of the functions used should be generalizeable for similar usage.

This file contains the following functions and their usage:
```scorigami```
Takes numeric margin of victory variable (score) and returns a randomized actual score number for that games victor, using a normal distribution of values based on the most common previous games with that margin of victory.

```game```
Takes two team objects (Team1, Team2) and a "roundnum" object and simulates a game between those two teams in that "round" of gameplay.

```bgame```
Does the same as the game function but includes Elo multipliers for bracket wins

```returnwins```
Takes a team object and sums and returns total amount of wins attributed to a team. Used for sorting teams by wins for determining Swiss matchups.

```returng2```
Takes a team object and returns value for a team's win in their second match. This is used for sorting based on intra-flight Swiss seeding based on USQ's seeding formula.

```roundone, roundtwo, roundthree```
Takes a list of team objects and simulates a "round" of Swiss matchups (rounds 1, 2, & 3, respectively).

```results```
Takes a list of team objects and returns their flight results. Should only be called after a round function is called on that list of team objects.


## Getting Started

### Dependencies

Requires the following libraries
* numpy
* random
* math
* operator

### Executing program

* This file can be run as-is to simulate the US Quidditch Cup 13.
* If simulating another tournament with similar structure (6 flights of 8 teams, Swiss), only the team name and Elo values will need to be changed on lines 351 to 404
* If simulating a different tournament type, functions from this can be easily adapted with minor modifications, but a new formatting file should be made.

## Authors

Joshua Mansfield
josh.mansfield93@gmail.com

## Versions

Version 1, April 2020.
* full project
Version 1.1, January 2024.
* edits for clarity

## Acknowledgments

Thank you to The Eighth Man and their editors for being all onboard this project and giving me the necessary motivation to put this together. Specific thanks to Amanda Dallas for all her hard work on the publication of these results.

Thank you to Raghu Achukola for help with code snippets and concept design.