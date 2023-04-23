import argparse
import datetime
import os
import yagmail
import workout_program

from globo import todoist

parser = argparse.ArgumentParser(description="CLI for the Globo workout application.")
parser.add_argument("--username", type=str, help="The gmail address from which the emails will be sent (xxx@gmail.com)", required=True)
parser.add_argument("--app_password", type=str, help="Your gmail app password to sign into the sender account.", required=True)
parser.add_argument("--recipients", type=str, help="A comma separated list of one or more recipient email addresses.", required=True)
parser.add_argument("--todoist", type=bool, help="If workouts should be sent to Todoist instead of gmail. If true, TODOIST_API_TOKEN environment variable is expected to be set.", required=False, default=False)

CURRENT_WORKOUT = workout_program.DumbbellStopGap

if __name__ == "__main__":
    # Parse the command line arguments
    args = parser.parse_args()

    # Get today as a weekday integer
    today = datetime.datetime.today().weekday()

    # See if today is a workout day
    if today in CURRENT_WORKOUT.keys():
        workout = CURRENT_WORKOUT.get(today)

        if args.todoist:
            task_name = f"WORKOUT: {workout.name}"
            description = workout.as_markdown()

            todoist.Todoist.create(
                os.environ.get("TODOIST_API_TOKEN")).addTask(
                    task_name, description)
 
        else:
            subject = f"{datetime.datetime.today().date()} WORKOUT: {workout.name}"
            # Handle newlines in html (yagmail v0.14.245 see https://github.com/kootenpv/yagmail/issues/116)
            contents = [workout.as_html().replace("\n","")]

            with yagmail.SMTP(user=args.username, password=args.app_password) as yag:
                for recipient in args.recipients.split(","):
                    yag.send(to=recipient, subject=subject, contents=contents)
