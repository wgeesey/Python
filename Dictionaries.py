student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

highest_total_points = 0

gradePerAssign = {}
for student, grades in student_grades.items():
    print(student, grades)
    total = sum(grades)
    print(total)
    if total > highest_total_points:
        highest_total_points = total
        name = student
        grade = (highest_total_points/len(grades))
print(f'Student: {name} Grade: {grade}') 

numStudents = len(student_grades)

for i in range(numStudents):
    assignmentScores = 0
    for grades in student_grades.values():
        assignmentScores += grades[i]
    gradePerAssign[i + 1] = assignmentScores / numStudents
    print(gradePerAssign[i + 1])
print(f'Averages: {gradePerAssign}')

print(f'{"Student":8} {"Grades":6} {"Curved-Grades":12}')
curve = 100 - grade
for student, grades in student_grades.items():
    studentTotal = sum(grades)
    normGrades = (studentTotal / len(grades))
    curvedScore = normGrades + curve
    print(f'{student:<8} {normGrades:^6.1f} {curvedScore:^12.1f}')

--------------------------------------------------------------------------------


grades = {
    'John Ponting': {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = input('Enter student name: ')

while user_input != 'exit':
    if user_input in grades:
        # Get values from nested dict
        homeworks = grades[user_input]['Homeworks']
        midterm = grades[user_input]['Midterm']
        final = grades[user_input]['Final']

        # print info
        for hw, score in enumerate(homeworks):
            
            print(f'Homework {hw}: {score}')

        
        print(f'Midterm: {midterm}')
        
        print(f'Final: {final}')

        # Compute student total score
        total_points = sum([i for i in homeworks]) + midterm + final
        
        print(f'Final percentage: {100*(total_points / 500.0):.1f}%')

    user_input = input('Enter student name: ')
    
---------------------------------------------------------------------------------

music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': ['Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': ['Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World': {
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

while True:
    user_input = input("Enter 'artist', 'album', 'song', or 'exit': ")
    if user_input == 'exit':
        break
    elif user_input == 'artist':
        artist_name = input("Enter artist name: ")
        if artist_name not in music:
            music[artist_name] = {}
    elif user_input == 'album':
        artist_name = input("Enter artist name: ")
        if artist_name in music:
            album_name = input("Enter album name: ")
            if album_name not in music[artist_name]:
                music[artist_name][album_name] = {'songs': [], 'year': None, 'platinum': False}
    elif user_input == 'song':
        artist_name = input("Enter artist name: ")
        album_name = input("Enter album name: ")
        if artist_name in music and album_name in music[artist_name]:
            song_name = input("Enter song name: ")
            music[artist_name][album_name]['songs'].append(song_name)

print(music)


--------------------------------------------------------------------------------------