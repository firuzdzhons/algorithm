
#Граф А
graphA = {}
graphA['A'] = {}
graphA['A']['B'] = 4
graphA['A']['G'] = 8

graphA['B'] = {}
graphA['B']['C'] = 2
graphA['B']['E'] = 12

graphA['C'] = {}
graphA['C']['G'] = 1

graphA['G'] = {}
graphA['G']['F'] = 9

graphA['F'] = {}
graphA['F']['D'] = 18

graphA['E'] = {}
graphA['E']['D'] = 7

print(graphA)

#Граф B

graphB = {}

graphB['A'] = {}
graphB['A']['B'] = 5
graphB['A']['E'] = 7
graphB['A']['K'] = 25

graphB['B'] = {}
graphB['B']['C'] = 4
graphB['B']['G'] = 21

graphB['C'] = {}
graphB['C']['D'] = 4
graphB['C']['H'] = 1
graphB['C']['G'] = 34

graphB['D'] = {}
graphB['D']['H'] = 2

graphB['E'] = {}
graphB['E']['I'] = 9

graphB['I'] = {}
graphB['I']['K'] = 6

graphB['K'] = {}
graphB['K']['F'] = 1
graphB['K']['P'] = 5

graphB['F'] = {}
graphB['F']['G'] = 2

graphB['G'] = {}
graphB['G']['L'] = 16

graphB['P'] = {}
graphB['P']['L'] = 15

print(graphB)