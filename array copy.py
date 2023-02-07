# if __name__ == '__main__':
n = int(input("number of student "))
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input()
marks=student_marks[query_name];
    
print('Marks for', query_name,' are ', marks,' whose average is  %0.2f' % (sum(student_marks[query_name])/len(student_marks[query_name])))