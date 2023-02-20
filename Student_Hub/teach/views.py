from django.shortcuts import render
from .forms import Subject_Form, Lesson_Form
# Create your views here.
from .models import Subject, Lesson
from django.views.generic import DetailView








def contents(request):
    return render(request, 'student/contents.html')


def base_nav(request):
    return render(request, 'student/base_nav.html')



# def control_panel(request):
#     return render(request, 'teacher/control_panel.html')
#
#














def contents_teacher(request):
    return render(request, 'teacher/contents_teacher.html')


def index(request):
    return render(request, 'teacher/index.html')


def control_panel(request):
    return render(request, 'teacher/control_panel.html')


# def exam(request):
#     return render(request, 'teacher/exam.html')








def exam_google(request):
    return render(request, 'teacher/exam_google.html')


def subject_form(request):
    form = Subject_Form()

    return render(request, 'teacher/subject_form.html', {'form': form})




def lesson_form(request):
    form = Lesson_Form()

    return render(request, 'teacher/lesson_form.html', {'form': form})



# class subjecte_List(ListView):
#     model = Subject


def subject(request):
    subjects = Subject.objects.all()
    # context = {'subjects': subjects}
    return render(request, 'student/subjecte_List.html', {'subjects': subjects})


class Lesson_Detail(DetailView):
    model = Lesson




# class Lessons_List(ListView):
# model = lesson



class subject_detail(DetailView):
    model = Subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Subject = self.get_object()
        context["subject_lesson"] = Lesson.objects.filter(subject=Subject)
        return context



