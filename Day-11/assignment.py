#Write a python code to get the list of Commits from Docker github account
import requests

response = requests.get("https://api.github.com/repos/docker/docker/commits")
get_docker_commits = response.json()

#Sample response
#print("All Commits: " , get_docker_commits)

#To get the list of authors who made the commits
for i in range(len(get_docker_commits)):
    print("Committed by Author: " , get_docker_commits[i]["commit"]["author"]["name"])