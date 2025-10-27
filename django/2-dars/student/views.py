from django.shortcuts import render

# Create your views here.
home = ['about','service','result','course', 'kunuz']
about_data = "Bugun sening kuning"
service_data = "Bugun quyon dam oladi"
result_data = "Bugun dam mehnatga hamdam"
course_data = "Bugun sening kuning emas uka"
kunuz = "https://kun.uz/"

def get_home(request):
    context = {
        'home': home,
    }
    return render(request,'student/home.html',context)

def get_about(request):
    context = {
        'about_data': about_data,
    }
    return render(request,'student/about.html',context)

def get_service(request):
    context = {
        'service_data': service_data,
    }
    return render(request,'student/service.html',context)

def get_result(request):
    context = {
        'result_data': result_data,
    }
    return render(request,'student/result.html',context)

def get_course(request):
    context = {
        'course_data': course_data,
    }
    return render(request,'student/course.html',context)

def get_kunuz(request):
    context = {
        'kunuz': kunuz,
    }
    return render(request,'student/kunuz.html',context)