import argparse
import requests
from gitEmails.helpers.utils import print_error, request_api, write_json

def main_find_emails(session: requests.Session, args: argparse.Namespace):
    emails_found = set() # ensemble des emails -> pas de doublons
    USER_NAME = ""

    if not args.url and not args.user:
        print_error("No URL provided or user", args)

    if args.url:
        USER_NAME = args.url.split('/')[-1]
        if args.url.replace('https://github.com/', '') != USER_NAME:
            print_error("URL is not valid", args)
    else:
        USER_NAME = args.user


    url = f"https://api.github.com/users/{USER_NAME}"
    info_user = request_api(url, session, args)
    NAME = info_user['name']


    url = f"https://api.github.com/users/{USER_NAME}/repos"
    repos = request_api(url, session, args)
    for repo in repos:
        if repo['owner']['login'] == USER_NAME: # If the repo is owned by the user
            url = f"https://api.github.com/repos/{repo['full_name']}/commits"
            commit = request_api(url, session, args)
            for c in range(0,len(commit),args.accuracy): # jump 5 commits

                if commit[c]['commit']['author']['name'] == NAME:
                    emails_found.add(commit[c]['commit']['author']['email'])
                if commit[c]['commit']['committer']['name'] == NAME:
                    emails_found.add(commit[c]['commit']['committer']['email'])

    emails_found_clean = set()
    for email in emails_found:
        if "users.noreply.github.com" not in email:
            emails_found_clean.add(email)

    if args.json:
        write_json({"emails": list(emails_found_clean)}, args.json)
        exit(0)

    print("Emails found : ")
    for email in emails_found_clean:
        print(email)
