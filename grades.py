grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2
    return variance / len(scores)

def grades_std_deviation(variance):
    return variance ** 0.5

def print_grade_information(grades):
    print "Grades:    ",
    c = 0
    for grade in grades:
        c = c + 1
        if c % 5 == 0 and c != 1:
            print ""
            print "           ",
        print grade,
    print ""
    print "Grade Sum: ", grades_sum(grades)
    print "Grade Avg: ", grades_average(grades)
    print "Grade Var: ", grades_variance(grades)
    print "Std Dev:   ", grades_std_deviation(grades_variance(grades))

print_grade_information(grades)
