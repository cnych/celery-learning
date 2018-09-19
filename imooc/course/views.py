# -*- coding: utf-8 -*-
from django.http import JsonResponse

from course.tasks import CourseTask


def do(request):
    # 执行异步任务
    print 'start do request'
    # CourseTask.delay()
    CourseTask.apply_async(args=('hello',), queue='work_queue')
    print 'end do request'
    return JsonResponse({'result': 'ok'})
