eren = {

 "name": "Eren",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]

}

mikasa = {

"name": "Mikasa",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]

}

armin = {

"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]

}

students = [eren, mikasa, armin]
for i in students:
    print(i["name"])
    print(i["homework"])
    print(i["quizzes"])
    print(i["tests"])

def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    homework *= 1/10
    quizzes *= 3/10
    tests *= 3/5
    return homework + quizzes + tests

def get_letter_grade(score):
    if score <= 60:
        return "F"
    elif 60 >= score > 70:
        return "D"
    elif 70 <= score < 80:
        return "C"
    elif 80 <= score < 90:
        return "B"
    else:
        return "A"

def get_class_average(students):
    results = []
    for i in students:
        results.append(get_average(i))
    return average(results)

print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))