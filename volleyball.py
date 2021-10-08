import itertools

data = {'John':93, 'Cam':96, 'Owen':81, 'Blake':71, 'Courtney':83, 'Hailey':90, 'Todd':91, 'Heidi':60}

combine = itertools.permutations(data.keys(),8)
all_combinations = list(combine)

all_teams_dict = {}
for i in all_combinations:
    team_overall = 0
    smteam_overall = 0
    st = 0
    fi = 3
    while fi <= 7:
        for j in i[st:fi+1]:
            person_score = data.get(j)
            smteam_overall += person_score
        smteam_overall = smteam_overall/4
        team_overall += smteam_overall
        smteam_overall = 0
        st += 1
        fi += 1

    for j in i[5], i[6], i[7], i[0]:
        person_score = data.get(j)
        smteam_overall += person_score
    smteam_overall = smteam_overall/4
    team_overall += smteam_overall
    smteam_overall = 0

    for j in i[6], i[7], i[0], i[1]:
        person_score = data.get(j)
        smteam_overall += person_score
    smteam_overall = smteam_overall/4
    team_overall += smteam_overall
    smteam_overall = 0

    for j in i[7], i[0], i[1], i[2]:
        person_score = data.get(j)
        smteam_overall += person_score
    smteam_overall = smteam_overall/4
    team_overall += smteam_overall
    smteam_overall = 0

    all_teams_dict[i] = team_overall/8

max_key = max(all_teams_dict)

print(max_key, all_teams_dict[max_key],"% Success")

