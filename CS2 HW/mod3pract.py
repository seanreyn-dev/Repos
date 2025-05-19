




student_scores = {}


with open("scores.txt") as infile:
    line = infile.readline()
    items = line.split(",")

    score = {}
    className = ''

    for i in range(1, len(items)):
        if i % 2 == 1:
            className = items[i]
        else:
            score[className] = int(items[i])
    
    
    student_scores[items[0]] = score


    while line != '':
        line = infile.readline()
        items = line.split(",")
        if items == ['']:
            break

        score = {}
        className = ''

        for i in range(1, len(items)):
            if i % 2 == 1:
                className = items[i]
            else:
                score[className] = int(items[i])
        student_scores[items[0]] = score
        

infile.close()

name = input("Please enter a student name ")
while name not in student_scores:
    name = input("Please try entering another name that is in student_scores")

scores = student_scores[name]
max_score = -1
best_class = ''

for c, s in scores.items():
    if s > max_score:
        best_class = c
        max_score = s
print("Student's best class was", best_class, "with score", max_score)