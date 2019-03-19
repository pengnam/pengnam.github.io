---
title: Tutorial 6 Reference (Answers)
geometry: "left=2.5cm,right=2.5cm,top=2cm,bottom=2cm"
---

```
# Question 3
def at_least_n(lst, n):
    reference_lst = lst.copy()
    for element in reference_lst:
        if element < n:
            lst.remove(element)
    return lst
```

```
# Question 4
def at_least_n(lst, n):
    new_list = []
    for element in lst:
        if element >= n:
            new_list.append(element)
    return new_list
```

```
# Question 5
def col_sum(matrix):
    result = [0] * len(matrix[0])
    for row in matrix:
        for index, value in enumerate(row):
            result[index] += value
    return result
```

```
# Question 6
def row_sum(matrix):
    result = []
    for row in matrix:
        result.append(sum(row))
    return result

def row_sum(matrix):
    return list(map(sum, matrix))
```

```
# Question 7
def transpose(matrix):
    result = []
    num_columns = len(matrix[0])
    for i in range(num_columns):
        result.append(list(map(lambda x: x[i], matrix)))
    return result
```

```
# Question 9
def mode_score(students):
    # We only care about the scores, so ignore everything else
    scores = list(map(lambda student: student[2], students))

    # Count the number of occurrences of each score
    freqs = []  # freq is tuple(score, num_occurrence)
    for score in scores:
        previous_freqs = list(filter(lambda freq: freq[0] == score, freqs))
        if previous_freqs == []:
            freqs.append((score, 1))
        else:
            previous_freq = previous_freqs[0]
            freqs.remove(previous_freq)
            freqs.append((score, previous_freq[1] + 1))

    # Sort the scores by their number of occurrences
    sorted_freqs = sorted(freqs, key=lambda freq: freq[1])

    # Pick the top appearing score(s)
    max_occurrences = sorted_freqs[-1][1]
    max_freqs = list(filter(lambda freq: freq[1] == max_occurrences, sorted_freqs))
    return list(map(lambda freq: freq[0], max_freqs))
```

```
# Question 10
def top_k(students, k):
    # omit the first line first
    sorted_students = sorted(students, key=lambda student: student[0])
    sorted_students = sorted(sorted_students, key=lambda student: student[2], reverse=True)
    top_k_students = sorted_students[:k]
    k_th_score = top_k_students[-1][2]
    for student in students:
        if student[2] == k_th_score and not student in top_k_students:
            top_k_students.append(student)
    return top_k_students
```
