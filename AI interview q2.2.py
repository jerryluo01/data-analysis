def to_grade_point(grade):
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

for grade in [0, 99, 80, 85, 84, 60, 59, 74]:   # **add 101 or sum to set to raise the error**
  print("{} -> {}".format(grade, to_grade_point(grade)))