def appearance(intervals: dict[str, list[int]]) -> int:
    student = intervals['pupil']
    teacher = intervals['tutor']

    summator = 0

    for i in range(len(student)):
        if student[i]<intervals['lesson'][0]:
            student[i] = intervals['lesson'][0]
        elif student[i] > intervals['lesson'][1]:
            student[i] = intervals['lesson'][1]

    for i in range(len(teacher)):
        if teacher[i]<intervals['lesson'][0]:
            teacher[i] = intervals['lesson'][0]
        elif teacher[i]>intervals['lesson'][1]:
            teacher[i] = intervals['lesson'][1]
    i, j = 0, 0
    while i<len(student) or j<len(teacher):
        if student[i]>=student[i+1]:
            i+=2
            continue
        if teacher[j] >= teacher[j+1]:
            j+=2
            continue

        if student[i]>teacher[j]:
            min_stamp = student[i]
        else:
            min_stamp = teacher[j]
        if student[i+1]<min_stamp:
            i+=2
            continue
        elif teacher[j+1]<min_stamp:
            j+=2
            continue
        if student[i+1]>teacher[j+1]:
            max_stamp = teacher[j+1]
            j+=2
        elif student[i+1]<=teacher[j+1]:
            max_stamp = student[i+1]
            i+=2
        summator+=max_stamp-min_stamp

        if i>=len(student) or j>=len(teacher):
            return summator
    return summator
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },

    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    {"intervals":{
        'lesson': [1609459200, 1609462800],
        'pupil': [1609459190, 1609459500, 1609459800, 1609460100],
        'tutor': [1609459300, 1609461000]
    },
        'answer': 500
    },
    {
        "intervals":{
    'lesson': [1609459200, 1609462800],
    'pupil': [1609459200, 1609459201],
    'tutor': [1609459200, 1609462800]
},
        'answer': 1
    }

]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
