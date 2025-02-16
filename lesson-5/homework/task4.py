universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats():
    return [[student,fee] for univ, student, fee in universities]

def mean():
    return (sum(student for student, fee in enrollment_stats()),\
            sum(fee for student, fee in enrollment_stats()))
#print(sum(student for student, fee in enrollment_stats()))  

print(enrollment_stats()[:][0])
print("Total students: ",sum(enrollment_stats()[i][0] for i in range(len(universities))))
print("Total tuition: ",sum(enrollment_stats()[i][1] for i in range(len(universities))))
print("____")
print("Student mean: ", mean()[0]/len(universities))

print("Tuition mean: ", mean()[1]/len(universities))