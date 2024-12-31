from django.shortcuts import render

import requests
from django.conf import settings


def list_repos(request):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {settings.GITHUB_API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    repos = response.json() if response.status_code == 200 else []

    return render(request, 'github_app/list_repos.html', {'repos': repos})
def create_repo(request):
    if request.method == "POST":
        repo_name = request.POST.get("repo_name")
        url = "https://api.github.com/user/repos"
        headers = {
            "Authorization": f"token {settings.GITHUB_API_TOKEN}"
        }
        data = {"name": repo_name, "private": False}
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 201:
            message = "Repository created successfully!"
        else:
            message = f"Failed to create repository: {response.json().get('message', 'Unknown error')}"

        return render(request, 'github_app/create_repo.html', {'message': message})

    return render(request, 'github_app/create_repo.html')
