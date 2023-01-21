#!./venv/bin/python
import random

people = ["Liam", "Olivia", "Noah", "Ava",
          "James", "Amelia", "William", "Emma"]

skills = ["coding", "art", "testing", "management", "marketing"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


"""
1. Randomly assign two skills to each person. Store this information in a suitable data structure
2. Write a program which prints the list of days four times, and for each day prints the names of three people who will work on that day. Also print the total set of skills from all people combined for each day.

The people should be chosen for each day in the order they are found in the people list, with no one person being chosen to work more often than any other.

"""

person_index = 0

def choose_person():
    global person_index
    person = people[person_index % len(people)]
    person_index += 1
    return person

def create_people_skills():

    people_skills = dict()

    for person in people:

        skillset = set()

        while len(skillset) < 2:
            skill = random.choice(skills)
            skillset.add(skill)

        people_skills[person] = skillset
    return people_skills


def main():
    people_skills = create_people_skills()

    for i in range(4):

        skills = set()

        for day in days:
            people = [choose_person() for x in range(3)]

            for person in people:
                skills.update(people_skills[person])

            print(day, end=": ")
            print(", ".join(people), end=" -- ")
            print(", ".join(skills))

main()