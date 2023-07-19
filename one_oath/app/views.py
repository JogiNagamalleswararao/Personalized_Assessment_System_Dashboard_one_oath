from django.shortcuts import render
import requests
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.

def base(request):
    return render(request,'base.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        username=username.upper()
        password = request.POST['password']
        # print(username,password)
        # Check if user exists
        try:
            user = Login.objects.get(uid=username)
        except:
            messages.error(request, 'Username does not exist')
            return redirect('login')
        # Check if password is correct
        if user.password == password:
            # Login user
            if user.teacher==True:
                request.session['user_id'] = user.uid
                return redirect('teacher_dashboard')
                pass
            else:
                request.session['user_id'] = user.uid
                #return render(request,'student_d.html')
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Incorrect password')
            return redirect('login')
        
    return render(request, 'login.html')
def student_r(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        uid=uid.upper()
        my_queryset = Student.objects.all()
        my_dict =  list(my_queryset.values())
        f=0
        for x in range(len(my_queryset)):
            if (my_dict[x]['uid']) == uid:
                f=1
                break
        if f!=1:
            email = request.POST['email']
            password = request.POST['password']
            fname = request.POST['fname']
            lname = request.POST['lname']
            sec = request.POST['sec']
            mobile_num = request.POST['mobile_num']
            address = request.POST['address']
            image_file = request.FILES.get('image')
            # create a new student object with the provided information
            student = Student(
                uid=uid,
                email=email,
                password=password,
                fname=fname,
                lname=lname,
                sec=sec,
                mobile_num=mobile_num,
                address=address,
                image=image_file
            )
            student.save()
            try:
                login=Login(
                    uid=uid,
                    password=password,
                    student='True'
                )
                login.save()
            except:
                pass
                # print("error")
            

            return render(request, 'reg_success.html')
        else:
            messages.error(request, "User alredy exit")


    return render(request, 'student_r.html')
def teacher_r(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        uid=uid.upper()
        my_queryset = Teacher.objects.all()
        my_dict =  list(my_queryset.values())
        f=0
        for x in range(len(my_queryset)):
            if (my_dict[x]['uid']) == uid:
                f=1
                break
        if f!=1:
            email = request.POST['email']
            password = request.POST['password']
            name = request.POST['name']
            mobile_num = request.POST['mobile_num']
            image_file = request.FILES.get('image')
            des = request.POST['des']
            
            # create a new teacher object with the provided information
            teacher = Teacher(
                uid=uid,
                Email=email,
                password=password,
                name=name,
                mobile_num=mobile_num,
                image=image_file,
                des=des
            )
            instance = Teacher(image=image_file)
            instance.save()
            teacher.save()
            try:
                login=Login(
                    uid=uid,
                    password=password,
                    teacher='True'
                )
                login.save()
            except:
                pass
                # print("error")

            return render(request, 'reg_success.html')
        else:
            messages.error(request, "User alredy exit")

    return render(request, 'teacher_r.html')


def teacher_dashboard(request):
    # Check if user is logged in
    if 'user_id' not in request.session:
        return redirect('login')
    
    # Get the teacher object using the stored user_id
    try:
        teacher = Teacher.objects.get(uid=request.session['user_id'])
    except Teacher.DoesNotExist:
        return redirect('login')
    
    # Get the submissions associated with the teacher's assessments
    submissions = Submission.objects.filter(assessment__teacher=teacher)
    
    context = {
        'teacher': teacher,
        'submissions': submissions,
    }
        
    return render(request, 'teacher_d.html', context)


def create_assessment(request):
    if request.method == 'POST':
        assessment_name = request.POST.get('assessment_name')
        
        # Get the teacher associated with the logged-in user
        try:
            teacher = Teacher.objects.get(uid=request.session['user_id'])
        except Teacher.DoesNotExist:
            return redirect('login')
        
        # Create the assessment with the associated teacher
        assessment = Assessment.objects.create(name=assessment_name, teacher=teacher)
        
        # Loop through the question data from the form and create the questions
        for key, value in request.POST.items():
            if key.startswith('question'):
                question = Question.objects.create(
                    assessment=assessment,
                    question=value,
                    option_a=request.POST.get(f'optionA{key[-1]}'),
                    option_b=request.POST.get(f'optionB{key[-1]}'),
                    option_c=request.POST.get(f'optionC{key[-1]}'),
                    option_d=request.POST.get(f'optionD{key[-1]}'),
                    correct_answer=request.POST.get(f'correctAnswer{key[-1]}')
                )
    
    return redirect('teacher_dashboard')


def student_dashboard(request):
    # Check if user is logged in
    if 'user_id' not in request.session:
        return redirect('login')
    
    # Get the student object using the stored user_id
    try:
        student = Student.objects.get(uid=request.session['user_id'])
    except Student.DoesNotExist:
        return redirect('login')


    
    # Get the submissions associated with the student
    submissions = Submission.objects.all()
    
        
    submissions = Submission.objects.filter(student=student)
    #for submission in submissions:
    temp=0
    flag=[]
    for submission in submissions:
            flag.append(submission.assessment.id)
    print(flag)
    assessment = Assessment.objects.filter()
    context = {
        'student': student,
        'submissions': submissions,
        'assessment': assessment,
        'temp': temp,
        'flag':flag,
    }
        
    return render(request, 'student_d.html', context)
    # submissions = Submission.objects.filter(student=student)
    # marks = 0

    # if submissions.exists():
    #     marks = submissions.marks

    # assessment = Assessment.objects.all()

    # context = {
    #     'student': student,
    #     'submissions': submissions,
    #     'assessment': assessment,
    #     'marks': marks,
    # }

    # return render(request, 'student_d.html', context)

# def student_dashboard(request):
#     assessment = Assessment.objects.filter()
#     context = {'assessment': assessment}
#     return render(request, 'student_d.html', context)

def start_assignment(request, assignment_id):
    assignment = Assessment.objects.get(pk=assignment_id)
    questions = assignment.question_set.all()  # Access questions using the reverse relation
    context = {'assignment': assignment, 'questions': questions}
    return render(request, 'assessment.html', context)


# from django.shortcuts import get_object_or_404

# def submit_assessment(request, assignment_id):
#     if request.method == 'POST':
#         assignment = get_object_or_404(Assessment, pk=assignment_id)
#         questions = Question.objects.filter(assessment=assignment)
#         marks = 0
        
#         for question in questions:
#             selected_option = request.POST.get(f'question_{question.id}')
            
#             if selected_option == question.correct_answer:
#                 marks += 1
        
#         # Retrieve the student object
#         try:
#             student = Student.objects.get(uid=request.session['user_id'])
#         except Student.DoesNotExist:
#             # Redirect or handle the case when the student does not exist
#             return redirect('student_dashboard')
        
#         # Store the student's marks
#         submission = Submission.objects.create(
#             student=student,
#             assessment=assignment,
#             marks=marks
#         )
        
#         return redirect('student_dashboard')

#     return redirect('student_dashboard')
from django.shortcuts import get_object_or_404

def submit_assessment(request, assignment_id):
    if request.method == 'POST':
        assignment = get_object_or_404(Assessment, pk=assignment_id)
        questions = Question.objects.filter(assessment=assignment)
        total_marks = 0
        obtained_marks = 0
        
        for question in questions:
            selected_options = request.POST.getlist(f'question_{question.id}')
            correct_options = question.correct_answer.split(',')
            
            if set(selected_options) == set(correct_options):
                obtained_marks += 1
            
            total_marks += 1
            print(total_marks)
        
        # Retrieve the student object
        try:
            student = Student.objects.get(uid=request.session['user_id'])
        except Student.DoesNotExist:
            # Redirect or handle the case when the student does not exist
            return redirect('student_dashboard')
        
        # Calculate the percentage of marks
        percentage = (obtained_marks / total_marks) * 100

        try:
            submission = Submission.objects.get(student=student, assessment=assignment)
            submission.marks = percentage
            submission.save()
        except Submission.DoesNotExist:
    # Create a new submission
            submission = Submission.objects.create(student=student, assessment=assignment, marks=percentage)

        
        # # Store the student's marks
        # submission = Submission.objects.create(
        #     student=student,
        #     assessment=assignment,
        #     marks=percentage
        # )
        
        return redirect('student_dashboard')

    return redirect('student_dashboard')



#---------------------Log out -----------------------------
def logout(request):
    return render(request, 'base.html')
#--------------------- -------- -----------------------------
