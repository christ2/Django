from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from .models import Choice, Question, TableAll
# import cx_Oracle

def login_view(request):
    if request.method == 'POST':         
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            guest = User.objects.get(username=username)
            role = guest.role
            user = authenticate(username=username, password=password)  
            if user is not None: 
                if role == 'Business Analyst':
                    login(request, user)
                    return redirect('/home/')
                elif role == 'Admin':
                    login(request, user)
                    return redirect('/manageuser/')
            else:
                messages.error(request, "Invalid username or password!")
        else:
            messages.error(request, "Invalid username or password!")
    form = AuthenticationForm()
    return render(request,"login.html",{"form":form})
    # dsn_tns = cx_Oracle.makedsn('10.20.214.198', '1527', sid='dicb') 
    # conn = cx_Oracle.connect(user=r'icb', password='devicb', dsn=dsn_tns) 
    # c = conn.cursor() 
    # c.execute("select role from auth_user where username = '"+username+"'")
      
def list_all_table(request):    
    obj = TableAll.objects.all()
    context = {
        'obj' : obj
    }
    return render(request,'define_segment.html',context)
    # dsn_tns = cx_Oracle.makedsn('10.20.214.198', '1527', sid='dicb') 
    # conn = cx_Oracle.connect(user=r'icb', password='devicb', dsn=dsn_tns) 
    # c = conn.cursor()
    # c.execute('select table_name from (select alt.*, rownum r from all_tables alt) where r > 19 and r < 32') 
    # for row in c:
    #     objectlist = row[0]
    #     obj = objectlist.split(',')
    #     objek = '['+ obj + ']' + row[2].split("delimiter")      
    #     context = {
    #         'tablename':objectlist[]
    #     }
    # return render(request,'define_segment.html',context)
        # obj = repr(objectlist)
        # # objek = dict.fromkeys(objectlist)
        # context = obj        
    # obj = TableAll.objects.all()
    # context = {
    #     'datatable' : obj.table_name
    # }
    # return render(request,'define_segment.html',context)

def index_view(request):
    return render(request, 'index.html')

def profile_view(request):
    return render(request, 'profile.html')

def chatroom(request):
    return render(request, 'chat_room.html')

def lockscreen(request):
    return render(request, 'lock_screen.html')

def createsegment(request):
    return render(request, 'create_segment.html')

def manageuser(request):
    return render(request, 'manage_user.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'index.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]


# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'detail.html'
#
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'
