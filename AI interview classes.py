class GradeRecords:
    def __init__(self, term):
        self.term = term
        self.grades = []
        self.num_courses = 0

    def to_grade_point(self, grade):
        if 85 <= grade <= 100:
            return ("A", 4.0)
        
        elif 80 <= grade < 85:
            return ("A-", 3.7)
        
        elif 75 <= grade < 80:
            return ("B+", 3.3)
        
        elif 70 <= grade < 75:
            return ("B", 3.0)
        
        elif 65 <= grade < 70:
            return ("B-", 2,7)
        
        elif 60 <= grade <65:
            return ("C+", 2.3)
        
        elif 0 <= grade < 60:
            return ("F", 0.0)
        
        else:
            raise Exception("Only numbers between 0 and 100 are accepted.")

    def add_course(self, code, grades, creds):
        grades = int(grades)
        self.creds = creds
        course = (code, grades, creds)
        self.grades.append(course)
        self.num_courses += 1

    def get_best_courses(self):
        list_of_score = {}

        for courses in self.grades:
            score = self.to_grade_point(courses[1])[1]
            list_of_score[courses[0]] = score
        
        best_score = max(list_of_score.values())
        best_classes = [key for key, value in list_of_score.items() if value == best_score]

        return best_classes

    def get_GPA(self):
        grade_point = 0
        total_creds = 0

        for courses in self.grades:
            score = self.to_grade_point(courses[1])[1]
            weight = score * self.creds
            grade_point += weight
            total_creds += self.creds

        gpa = round(grade_point / total_creds, 1)

        return gpa


    def to_dict(self):
        list_of_score = {}

        for courses in self.grades:
            score = self.to_grade_point(courses[1])[0]
            list_of_score[courses[0]] = score

        return list_of_score


gr = GradeRecords("Fall 2019")
print("First batch")
print("Term: {}".format(gr.term))

gr.add_course("COMP 202", 83, 3)
gr.add_course("CLAS 203", 75, 3)
gr.add_course("LING 360", 81, 3)

print("Number of courses: {}".format(gr.num_courses))
print("Best courses: {}".format(gr.get_best_courses()))
print("GPA: {}".format(gr.get_GPA()))
print("Dictionary: {}".format(gr.to_dict()))

print()

print("Second batch")
print("Term: {}".format(gr.term))

gr.add_course("COMP 551", 67, 4)
gr.add_course("HIST 318", 88, 3)

print("Number of courses: {}".format(gr.num_courses))
print("Best courses: {}".format(gr.get_best_courses()))
print("GPA: {}".format(gr.get_GPA()))
print("Dictionary: {}".format(gr.to_dict()))