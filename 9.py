if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores_b = student_marks[query_name]
    print("{0:.2f}".format(sum(scores_b) / (len(scores_b))))




