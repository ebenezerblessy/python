#DataFrame modification: insert, delete

import pandas as pd
students = {
    'Name': ['ebi', 'blessy', 'angel', 'ebin'],
    'age': [20, 21, 22, 23],
    'marks': [97, 95, 98, 96]
}
student_df = pd.DataFrame(students)
print("Original DataFrame:")
print(student_df)

student_df.insert(loc=1, column='class', value='A/B',)
print("\nDataFrame after inserting 'class':")
print(student_df)

student_df = student_df.drop(columns='marks')
print("\nDataFrame after dropping 'marks':")
print(student_df)
