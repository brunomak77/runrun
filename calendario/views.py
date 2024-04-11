from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .engine import tasks_data, tempo, prazoHoje, backlog, user_data, prazoHojeAtraso, tc

@login_required
def creative_tasks(request):
    tasks_criacao = tc()
    backl = backlog(tasks_data())
    dias = tempo()
    dt = prazoHoje()
    dy = prazoHojeAtraso()

    return render(request, 'tasks.html', {'dy': dy,
                                          'dt': dt,
                                          'dias': dias,
                                          'tasks': tasks_criacao,
                                          'backlog': backl,})

@login_required
def creative_backlog(request):
    backl = backlog(tasks_data())
    return render(request, 'backlog.html', {'backlog': backl})



def creative_users(request):
    colaboradores = user_data()
    return render(request, 'colaboradores.html', {'colaboradores': colaboradores})

@login_required
def users_tasks(request):
    u_tasks = tc()
    backl = backlog(tasks_data())

    return render(request, 'u_tasks.html', {'utasks': u_tasks,
                                            'backlog': backl,})

def teste(request):
    tasks_criacao = tasks_data()
    dias = tempo()
    return render(request, 'teste.html', {'tasks': tasks_criacao,
                                          'dias': dias,})