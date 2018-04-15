if __name__ == '__main__':
    students = []
    scores = []
    secondStudents = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])
        scores.append(score)

    # get the lowest in the scores
    lowest = min(scores)
    # remove the lowest score until there's none left
    # by removing the lowest value
    # the only thing that will be
    # left in the scores list
    # is the 2nd to lowest value upwards
    while min(scores) == lowest:
        scores.remove(min(scores))

    # get the 2nd to lowest score
    secondToLowest = min(scores)

    # get all the students that has the 2nd to lowest scores
    # and append that to the secondStudents list
    for i in students:
        if i[1] == secondToLowest:
            secondStudents.append(i[0])

    # print the result
    for i in sorted(secondStudents):
        print(i)