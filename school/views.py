from django.views.generic import ListView
from django.shortcuts import render
import operator

from .models import Teacher


class TeacherList(ListView):
    model = Teacher


def students_list(request):
    template = 'school/students_list.html'

    teacher = Teacher.objects.all().all().prefetch_related('students').defer('id')

    object_list = []

    for th in teacher:
        for i in th.students.all():
            obj = {'name': i.name,
                   'group': i.group,
                   'teacher': {'name': th.name,
                               'subject': th.subject
                               }
                   }

            object_list.append(obj)

    object_list.sort(key=operator.itemgetter('group'))

    context = {
        'object_list': object_list
    }

    return render(request, template, context)
