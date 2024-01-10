from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render



def welcome(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    programs_data = {
        'Python': [
            {'name': 'Bambilici', 'github_url': 'https://github.com/pybm/projects/blob/main/%231%20bambilici_electronic'},
            {'name': 'Loto', 'github_url': 'https://github.com/pybm/projects/blob/main/%232%20loto%206.49'},
            {'name': 'Intervals', 'github_url': 'https://github.com/pybm/projects/blob/main/%233%20intervals'},
        ],
        'NumPy': [
            {'name': 'Galaxies', 'github_url': 'https://github.com/pybm/projects/blob/main/%235%20Galaxies'},
        ],
        'Django': [
            {'name': 'Project X', 'github_url': 'https://github.com/your_username/projectX'},
            {'name': 'Project Y', 'github_url': 'https://github.com/your_username/projectY'},
        ],
    }

    context = {'programs_data': programs_data}
    return render(request, 'template.html', context)

def resume(request):
    template = loader.get_template('resume.html')
    return HttpResponse(template.render())

def kyo(request):
    template = loader.get_template('underconstruction.html')
    return HttpResponse(template.render())



def projects(request):
    template = loader.get_template('projects.html')

    context = {
        'programs': ['Python', 'NumPy', 'Django'],
        'projects_data': {
            'Python': [
                {'name': 'Bambilici', 'github_url': 'https://github.com/pybm/projects/blob/main/%231%20bambilici_electronic'},
                {'name': 'Loto', 'github_url': 'https://github.com/pybm/projects/blob/main/%232%20loto%206.49'},
                {'name': 'Intervals', 'github_url': 'https://github.com/pybm/projects/blob/main/%233%20intervals'},
            ],
            'NumPy': [
                {'name': 'Galaxies', 'github_url': 'https://github.com/pybm/projects/blob/main/%235%20Galaxies'},
            ],
            'Django': [
                {'name': 'Blog', 'github_url': 'https://github.com/your_username/projectX'},
            ],
        }
    }

    return HttpResponse(template.render(context, request))

def detailsp(request, program='Python'):
    projects_data = {
        'Python': [
            {'name': 'Bambilici', 'github_url': 'https://github.com/pybm/projects/blob/main/%231%20bambilici_electronic'},
            {'name': 'Loto', 'github_url': 'https://github.com/pybm/projects/blob/main/%232%20loto%206.49'},
            {'name': 'Intervals', 'github_url': 'https://github.com/pybm/projects/blob/main/%233%20intervals'},
            {'name': 'Task-Manager', 'github_url': 'https://github.com/pybm/projects/blob/main/%234%20Task%20Manager'},
        ],
        'NumPy': [
            {'name': 'Galaxies', 'github_url': 'https://github.com/pybm/projects/blob/main/%235%20Galaxies'},
        ],
        'Django': [
            {'name': 'Blog', 'github_url': 'https://github.com/your_username/projectX'},
         ],
    }

    if program in projects_data:
        projects = projects_data[program]
        context = {'program': program, 'projects': projects}
        return render(request, 'detailsp.html', context)
