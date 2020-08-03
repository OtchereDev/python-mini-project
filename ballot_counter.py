polls=["oliver","ellen","rich","pat","pat","rich","ellen","oliver","ellen","rich","pat"]

candidates=[]
votes=[]

for person in polls:
    if person not in candidates:
        candidates.append(person)
        votes.append(1)
    else:
        candidates_index=candidates.index(person)
        votes[candidates_index]+=1

max_vote=0
max_candidate= []

for i in range(len(votes)):
    if votes[i] > max_vote:
        max_vote=votes[i]
        candidate=candidates[i]
        max_candidate=[]
        max_candidate.append(candidate)
    elif votes[i] == max_vote:
        candidate=candidates[i]
        max_candidate.append(candidate)
print("the highest vote is "+ str(max_vote))
print("It goes to : " )
print(*max_candidate,sep="\n")