import argparse
from time import time
from gitEmails.helpers.utils import print_error, write_json
import requests

def main_credits(session: requests.Session, args: argparse.Namespace):
    res = session.get("https://api.github.com/octocat")
    if res.status_code != 200:
        if res.status_code == 403:
            print("You don't have enough credits to use this tool")
            exit(1)
        print_error("Error fetching credits", args, res.status_code)

    timestamp_actuel = int(time())
    futur_timestamp = int(res.headers.get("x-ratelimit-reset"))
    difference_secondes = futur_timestamp - timestamp_actuel
    minutes_restantes = difference_secondes / 60

    if args.json:
        write_json({"rate-limit": int(res.headers.get("x-ratelimit-limit")), "remaining": int(res.headers.get("x-ratelimit-remaining")), "reset": round(minutes_restantes,2)}, args.json)
        exit(0)

    print("You can use only", res.headers.get("x-ratelimit-limit"), "requests per hour")
    print("You still have", res.headers.get("x-ratelimit-remaining"), "requests")
    print(round(minutes_restantes,2), "minutes remaining before recharging")
    exit(0)
