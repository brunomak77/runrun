import requests
import datetime
from decouple import config

# Create your models here.

ApK = config('APK')
UsT = config('UST')
url = config('URL')

    
def tasks_data():
    try:
        res_tasks = requests.get('https://secure.runrun.it/api/v1.0/tasks', headers={'App-Key': ApK, 'User-Token': UsT})
        tasks = res_tasks.json()

            
        for task in tasks:

            s = task['desired_date']
            if task['desired_date'] is None:
                task['ordenar'] = 30000000
            else:
                j = task['desired_date'].split('-')
                task['ordenar'] = int(j[0] + j[1] + j[2])

            if task['desired_date'] is not None:
                
                datetime_object = datetime.datetime.strptime(s, "%Y-%m-%d").date()
                task['desired_date'] = datetime_object
        
        tasks2 = sorted(tasks, key=lambda x: x['ordenar'])

        # for t in tasks2:
        #     print(t)
        #     print(t['desired_date'],'\n',
        #           t['ordenar'],'\n')
        
        
        return tasks2
    except:
        return '\nNão foi possível acessar o API\n'

# tasks_data()

def user_data():
    try:
        res_users = requests.get('https://secure.runrun.it/api/v1.0/users', headers={'App-Key': ApK, 'User-Token': UsT})
        users = res_users.json()
        time_criativo = []
        for user in users:
            time_criativo.append(user)

        time_criativo_org = sorted(time_criativo, key=lambda time: time['name'])
        return time_criativo_org

    except:
        return '\nNão foi possível acessar o API\n'


def colaborador(entrada, name):
    colaborador = []
    for a in entrada:
        for b in a['assignments']:
            if b['assignee_name'] == name:
                colaborador.append(a)
    return colaborador


def tempo():
    today = datetime.date.today()
    dum = today + datetime.timedelta(days=1)
    ddum = today + datetime.timedelta(days=-1)
    ddois = today + datetime.timedelta(days=2)
    dddois = today + datetime.timedelta(days=-2)
    dtres = today + datetime.timedelta(days=3)
    ddtres = today + datetime.timedelta(days=-3)
    dquatro = today + datetime.timedelta(days=4)
    ddquatro = today + datetime.timedelta(days=-4)
    dcinco = today + datetime.timedelta(days=5)
    ddcinco = today + datetime.timedelta(days=-5)

    dias = [today, dum, ddois, dtres, dquatro, dcinco, ddum, dddois, ddtres, ddquatro, ddcinco]

    return dias


def creative_data(tasks):
    tasks = tasks
    tasks_criacao = []

    for task in tasks:
        if task['team_name'] == 'Criação' and task['desired_date'] is not None:
            tasks_criacao.append(task)
    return tasks_criacao


def tc():
    tasks_criacao = creative_data(tasks_data())

    team_id_list = ["Alana Castello", "André Restrepo ",
                    "Arnaldo Colón", "Bruno Makhohl",
                    "Giovanna Esteves", "Luca de Oliveira", "Luis Meira"]
    creative_team = []
    pessoa = 0

    while pessoa < len(team_id_list):
        func = colaborador(tasks_criacao, team_id_list[pessoa])
        creative_team.append(func)
        pessoa += 1

    return creative_team


def prazoHoje():
    hj = []
    for dia in tempo():
        d = []
        for item in creative_data(tasks_data()):
            s = item['desired_date']
            if s == dia:
                d.append(item)
        hj.append(d)

    return hj


def backlog(tasks):
    tasks = tasks
    tasks_backl = []

    for task in tasks:
        if task['team_name'] == 'Criação' and task['is_assigned'] is False:
            tasks_backl.append(task)
    return tasks_backl


def prazoHojeAtraso():
    hjeatraso = []
    for dia in tempo():
        d = []
        for item in creative_data(tasks_data()):
            s = item['desired_date']
            if s <= dia:
                d.append(item)
        hjeatraso.append(d)

    return hjeatraso

