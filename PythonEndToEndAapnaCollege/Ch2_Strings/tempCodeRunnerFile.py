import pandas as pd

# Function to validate quiz marks
def get_quiz_mark(quiz_num):
    while True:
        mark = float(input(f"Enter mark for Quiz {quiz_num}: "))
        if 0 <= mark <= 10:
            return mark
        else:
            print("Invalid input. Please enter a mark between 0 and 10.")

# Function to validate and convert midterm and final marks
def get_converted_mark(exam_type, full_mark):
    mark = float(input(f"Enter mark for {exam_type}: "))
    return (mark / full_mark) * 100

# Get student data
roll_num = input("Enter roll number: ")
quiz_marks = [get_quiz_mark(i) for i in range(1, 4)]
avg_quiz_mark = sum(quiz_marks) / len(quiz_marks)
mid_marks = [get_converted_mark(f"Mid {i}", 100) for i in range(1, 3)]
final_mark = get_converted_mark("Final", 150)

# Save data to Excel
df = pd.DataFrame({
    'Roll Number': [roll_num],
    'Quiz 1': [quiz_marks[0]],
    'Quiz 2': [quiz_marks[1]],
    'Quiz 3': [quiz_marks[2]],
    'Average Quiz Mark': [avg_quiz_mark],
    'Mid 1': [mid_marks[0]],
    'Mid 2': [mid_marks[1]],
    'Final': [final_mark]
})
df.to_excel('resultsheet.xlsx', index=False)