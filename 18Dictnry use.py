if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    for _ in range(n):
        query_name = input()
        scores = student_marks[query_name]
        print("{0:.2f}".format(sum(scores) / (len(scores))))




