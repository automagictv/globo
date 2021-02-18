import argparse
import datetime
import yagmail
import workout_program

parser = argparse.ArgumentParser(description="CLI for the Globo workout application.")
parser.add_argument("--recipients", type=str, help="A comma separated list of one or more recipient email addresses.", required=True)
parser.add_argument("--credsfile", type=str, help="The Gmail OATH2 credentials json file path.", required=True)


CURRENT_WORKOUT = workout_program.WS4SB

if __name__ == "__main__":
    args = parser.parse_args()
    today = datetime.datetime.today().weekday()
    # See if today is a workout day
    if today in CURRENT_WORKOUT.keys():
        workout = CURRENT_WORKOUT.get(today)
        subject = f"WORKOUT: {workout.name}"

        with yagmail.SMTP(user=args.gmail_username, oauth2_file=args.credsfile) as yag:
            for recipient in args.recipients.split(","):
                yag.send(recipient, subject, workout.as_html())
