from mton.models import Student, Lecture, Enrolment


# Student.objects.create(name='aaa') # 밑에랑 같은 의미
# create_student = Student.objects.create
# s1 = create_student(name='짱두님')
# s2 = create_student(name='유튜버')
# s3 = create_student(name='넴띤이형님')
#
#
# l1 = Lecture.objects.create(title='컴개')
# l2 = Lecture.objects.create(title='자료구조')
# l3 = Lecture.objects.create(title='알고리즘')
#
#
# Enrolment.objects.create(lecture=l1, student=s1)
# Enrolment.objects.create(lecture=l1, student=s2)
# Enrolment.objects.create(lecture=l1, student=s3)

이종화 = Student.objects.get(id=1)
이종화.enrolment_set.get(id=1) # id = 1, lecture_id = 1, student_id = 1

이종화의_수강신청_목록.enrolment_set.all()
# id = 1, lecture_id = 1, id = 1,
# id = 1, lecture_id = 2, id = 1,
# .....

for 수강신청 in 이종화의_수강신청_목록:
    print(수강신청.lecture.title)