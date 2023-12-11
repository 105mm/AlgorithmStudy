import sys

selected = []

solted_score = [int(sys.stdin.readline().strip()) for _ in range(8)]

score = solted_score[:]

solted_score.sort(reverse=True)

print(sum(solted_score[:5]))

for i in score:
    for j in solted_score[:5]:
        if i==j:
            selected.append(str(score.index(i)+1))

result = ' '.join(selected)
print(result)