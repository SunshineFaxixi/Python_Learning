# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {name: random.randint(1, 100) for name in names}
# print(student_scores)
#
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# weather = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# new_weather = {date:temp * 9 / 5 + 32 for (date, temp) in weather.items()}
# print(new_weather)

student_dict = {
    "Student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Loop through dictionaries:
# for (key, value) in student_dict.items():
    # print(key)
    # print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame
# for (key, value) in student_data_frame.items():
    # print(key)
    # print(value)

# loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(type(row))
    # if row.student == "Angela":
    #     print(row.score)