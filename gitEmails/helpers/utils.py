import jsonpickle
import json
import argparse
import requests

def write_json(data, filename='data.json'):
    with open(filename, 'w') as fichier:
        serialized = jsonpickle.encode(data)
        pretty_output = json.dumps(json.loads(serialized), indent=2)
        fichier.write(pretty_output)

def print_error(message: str, args: argparse.Namespace, status_code: int=None):
    if args.json:
        if status_code:
            write_json({"error": message, "status_code": status_code}, args.json)
            exit(1)
        with open(args.json, 'w') as fichier:
            write_json({"error": message}, args.json)
        exit(1)
    if status_code:
        print(message, status_code)
        exit(1)
    print(message)
    exit(1)


def have_token(session: requests.Session, args: argparse.Namespace):
    if not args.token:
        print("If you want to use this script more than 60 times per hour, please provide a token\n\n")
    else:
        headers = {
            "Authorization": f"Bearer {args.token}"
        }
        session.headers.update(headers)
def verif_api(session: requests.Session, args: argparse.Namespace):
    res = session.get("https://api.github.com/octocat")
    if res.status_code != 200:
        if res.status_code != 401:
            print_error("Invalid token", args, res.status_code)
            exit(1)
        if res.status_code != 403:
            print_error("Too many requests", args, res.status_code)
            exit(1)



def header_command():
    print("Created by LighTend3r\nhttps://github.com/LighTend3r\n")

def request_api(url: str, session: requests.Session, args: argparse.Namespace):
    res = session.get(url)
    if res.status_code != 200:
        print_error("Error fetching repos", args, res.status_code)
    return res.json()
