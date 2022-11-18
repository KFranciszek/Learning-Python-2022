from dicBMI import team


def writeBMI(team):
    w = open("BMI_TEAM.txt", 'w')
    for i in team:
        w.write(str(i) + '\n')
    w.close()


writeBMI (team)

import json
def writeJSON():
    filename = ('D:\Python\Projekt\dane.json')
    users=team
    with open(filename, 'w') as outfile:
        json.dump(users,outfile)

writeJSON()
