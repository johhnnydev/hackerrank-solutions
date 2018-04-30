#!/bin/python3

import sys

def viralAdvertising(number_of_days):
    number_of_friends = 3
    initial_target = 5
    current_target = initial_target
    people = []
    for _ in range(number_of_days):
        # get the half of the target people
        half_people = current_target // 2
        # add the result to the people array
        people.append(half_people)
        # update the current target
        current_target = half_people * number_of_friends
    return sum(people)
if __name__ == "__main__":
    number_of_days = int(input().strip())
    result = viralAdvertising(number_of_days)
    print(result)