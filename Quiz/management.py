from datetime import datetime
from .models import Quiz, Participation

class QuizManagementSystem:
    def create_quiz(self, title):
        return Quiz.objects.create(title=title)

    def invite_participants(self, quiz, students):
        quiz.participants.add(*students)

    def add_participant(self, quiz, student):
        Participation.objects.create(quiz=quiz, student=student, submission_time=datetime.now())

    def enable_quiz_submissions(self, quiz):
        quiz_submissions_enabled = True
        quiz.save()

    def retrieve_quiz_results(self, quiz):
        results = []
        for participant in quiz.participation_set.all():
            # Gather participant's results and append to results list
            results.append({
                'student': participant.student.name,
                'submission_time': participant.submission_time,
                # Include more result details as needed
            })
        return results
