from django.shortcuts import render
from django.http import HttpResponse
from students.models import Studentdetails
from students.models import Courseinfo
from students.models import Enrollment
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    context = {'firstname':'Rakesh', 'lastname':'Ravi'}
    return render(request, 'students/home.html', context)
@login_required
def studentdetails(request):
    students = Studentdetails.objects.all()
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    studentdata = paginator.get_page(page)

    return render(request, 'students/studentdetails.html', {'data':studentdata})
@login_required
def courseinfo(request):
    courses = Courseinfo.objects.all()
    paginator = Paginator(courses, 10)
    page = request.GET.get('page')
    coursedata = paginator.get_page(page)

    return render(request, 'students/courseinfo.html', {'data':coursedata})
def enrollment(request):
    enrollmentcinfo = Courseinfo.objects.all()
    enrollmentsinfo = Studentdetails.objects.all()
    enrollmentdata = ""
    if('studentid' in request.session):
        enrollmentdata = Enrollment.objects.filter(studentid = request.session['studentid'])
    if('idnumber' in request.GET and 'cname' not in request.GET):
        idnumber = request.GET.get('idnumber')
        request.session['studentid'] = idnumber
        return HttpResponse('Success')
    if('idnumber' in request.GET and 'cname' in request.GET):
        idnumber = request.GET.get('idnumber')
        cname = request.GET.get('cname')
        enrollmentcourseinfo = Courseinfo.objects.filter(coursename=cname)
        enrollmentcourseid = enrollmentcourseinfo.values()[0]['courseid']
        enrollmentname = enrollmentcourseinfo.values()[0]['coursename']
        enrollmentselection = enrollmentcourseinfo.values()[0]['courseselectioncode']
        enrollmentdepartment = enrollmentcourseinfo.values()[0]['coursedepartment']
        enrollmentinstructor = enrollmentcourseinfo.values()[0]['instructorname']
        enrollmentdata = Enrollment.objects.filter(studentid= idnumber)
        count = 0
        for row in enrollmentdata:
            count = count+1
            if count >= 3:
                return HttpResponse('E1')
            if row.coursename == cname:
                return HttpResponse('E2')
        newdata= Enrollment(studentid = idnumber, courseid=enrollmentcourseid, coursename=enrollmentname, courseselectioncode=enrollmentselection, coursedepartment= enrollmentdepartment, instructorname= enrollmentinstructor)
        newdata.save()
        return HttpResponse('Success')
    return render(request, 'students/Enrollment.html', {'students': enrollmentsinfo, 'enrollmentcinfo': enrollmentcinfo, 'Enrollment': enrollmentdata})
