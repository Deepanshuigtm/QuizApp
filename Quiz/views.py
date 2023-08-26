from django.shortcuts import render
from .models import Student, Teacher, Parent
from .management import QuizManagementSystem
from .models import Question
from .forms import QuestionForm

# Create your views here.

def index(request):
    return render(request,"index.html")

def quiz(request):
    questions = Question.objects.all()
    form = QuestionForm()
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Process user's answers here
            return render(request, 'quiz.html', {'questions': questions, 'form': form})

def quiz_system(request):
    # Instantiate instances of classes
    student = Student.objects.create(name='Student 1')
    teacher = Teacher.objects.create(name='Teacher 1')
    parent = Parent.objects.create(name='Parent 1')

    # Instantiate the QuizManagementSystem
    qms = QuizManagementSystem()

    # Create a quiz and invite participants
    quiz = qms.create_quiz(title='Sample Quiz')
    qms.invite_participants(quiz, [student, teacher, parent])

    # Add a participant and enable submissions
    qms.add_participant(quiz, student)
    qms.enable_quiz_submissions(quiz)

    # Retrieve and display quiz results
    results = qms.retrieve_quiz_results(quiz)

    return render(request, 'result.html', {'results': results})