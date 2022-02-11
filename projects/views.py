from django.shortcuts import render


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    context = {'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = None

    for project in projectsList:
        if project['id'] == pk:
            project_obj = project

    context = {'project': project_obj}
    return render(request, 'projects/single_project.html', context)
