
person = {
    'name':'alice',
    'scale': {
        '1': -1,
        '2': 1,
        '3': 0.5,
        '4': 0.5,
        '5': -0.3
    }
}
person1 = {
    'name': 'emma',
    'scale': {
        '1' : 1,
        '2' : -1,
        '3' : -0.5,
        '4' : -0.5,
        '5' : 0.3
    }
}
person2 = {
    'name': 'nils',
    'scale': {
        '1' : 0.6,
        '2' : -0.3,
        '3' : -0.1,
        '4' : -0.7,
        '5' : 0.4
    }

}
person3 = {
    'name': 'kalle',
    'scale': {
        '1' : -0.6,
        '2' : 0.3,
        '3' : 1,
        '4' : 0.7,
        '5' : -0.4
    }
}

plist = [person,person1,person2,person3]

def score(p1,p2,p3):
    if p3 is None:
        return score2(p1,p2)
    else:
        return score3(p1,p2,p3)

def score2 (per1, per2):
    p1 = per1['scale']
    p2 = per2['scale']
    spread = 0
    for scale in p1:
        spread += abs(p1.get(scale) - p2.get(scale))
    return spread

def score3 (per1, per2, per3):
    p1 = per1['scale']
    p2 = per2['scale']
    p3 = per3['scale']
    spread = 0
    for scale in p1:
        l = [p1.get(scale),p2.get(scale),p3.get(scale)]
        l.sort()
        spread += abs(l[0] - l[2])
    return spread

i = 0
print("unsorted spreads")
while(i < len(plist)):
    scores = score(plist[i],plist[(i+1)%len(plist)],plist[(i+2)%len(plist)])
    print("Spread: " + plist[i]['name'] +", "+ plist[(i+1)%len(plist)]['name']+", "+ plist[(i+2)%len(plist)]['name']+ " ==> " + str(scores))
    i = i+1
