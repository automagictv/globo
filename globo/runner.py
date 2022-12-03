import argparse
import datetime
import yagmail
import workout_program

parser = argparse.ArgumentParser(description="CLI for the Globo workout application.")
parser.add_argument("--username", type=str, help="The gmail address from which the emails will be sent (xxx@gmail.com)", required=True)
parser.add_argument("--app_password", type=str, help="Your gmail app password to sign into the sender account.", required=True)
parser.add_argument("--recipients", type=str, help="A comma separated list of one or more recipient email addresses.", required=True)

CURRENT_WORKOUT = workout_program.FiveThreeOne

if __name__ == "__main__":
    # Parse the command line arguments
    args = parser.parse_args()

    # Get today as a weekday integer
    today = datetime.datetime.today().weekday()

    # See if today is a workout day
    if today in CURRENT_WORKOUT.keys():
        workout = CURRENT_WORKOUT.get(today)
        subject = f"{datetime.datetime.today().date()} WORKOUT: {workout.name}"
        # Handle newlines in html (yagmail v0.14.245 see https://github.com/kootenpv/yagmail/issues/116)
        contents = [workout.as_html().replace("\n","")]

        with yagmail.SMTP(user=args.username, password=args.app_password) as yag:
            for recipient in args.recipients.split(","):
                yag.send(to=recipient, subject=subject, contents=contents)
