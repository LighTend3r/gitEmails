import sys
import argparse
import requests
from gitEmails.modules.credits import main_credits
from gitEmails.modules.find_emails import main_find_emails
from gitEmails.helpers.utils import header_command, have_token, verif_api

def parse_run():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="module")

    ### CREDITS
    parser_credits = subparsers.add_parser('credits', help="Number of credits left")
    parser_credits.add_argument('-t', '--token', type=str, help="GitHub token")
    parser_credits.add_argument('-j', '--json', type=str, help="Output as JSON in a file")

    ### EMAILS
    parser_emails = subparsers.add_parser('emails', help="Find emails from GitHub account")
    parser_emails.add_argument('-t', '--token', type=str, help="GitHub token")
    parser_emails.add_argument('-j', '--json', type=str, help="Output as JSON in a file")
    parser_emails.add_argument('-u','--url', type=str, help="URL to GitHub account, e.g. https://github.com/<username>")
    parser_emails.add_argument('-user', '--user', type=str, help="GitHub username, you found it in the URL")
    parser_emails.add_argument('-a', '--accuracy', type=int, help="Accuracy of the search, default 5", default=5)

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    process_args(args)


def process_args(args: argparse.Namespace):
    header_command()
    session = requests.Session()

    have_token(session, args) # if token is provided, add it to the session

    verif_api(session, args) # verify if the API is working

    match args.module:
        case "credits":
            main_credits(session, args)
        case "emails":
            main_find_emails(session, args)

