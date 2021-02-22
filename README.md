# Globo
Dodge, Duck, Dip, Dive, Dodge

Automated workout routines delivered straight to your inbox (**tutorial video [here](https://youtu.be/Y9l2-1YTdlI)**).

Add exercises, routines and workouts to fit your desired workout program. The `workout_program` scheduler will determine if a given workout should be delivered to your inbox on a given day.

## Setup
This uses `pipenv` to manage the virtual env and all dependencies. If you don't have pipenv install it [here](https://pypi.org/project/pipenv/) then:

```
git clone https://github.com/automagictv/globo.git
cd globo
pipenv install --ignore-pipfile
```

To run:

```
pipenv run python globo/runner.py \
  --username senders@email.com \
  --app_password 'yourapppassword' \
  --recipients recipient1@email.com,recipient2@email.com,recipientn@email.com
```

If you want to set this up on a cron, you can do something like:

```
# Run at 12:05 AM every day
5 0 * * * pipenv run python /path/to/globo/runner.py --username senders@email.com --app_password 'yourapppassword' --recipients recipient1@email.com,recipient2@email.com,recipientn@email.com >> /path/to/cronlog.txt 2>&1
```

You may have to add `/usr/local/bin` to your path for the above to work.

## Gmail App Password

To obtain a Gmail App Password, follow [this guide](https://support.google.com/accounts/answer/185833).

# Architecture

## exercise.py
Defines the `Exercise` object.

## routine.py
Defines the `ExerciseRoutine` objects (made up of `Exercise` objects).

## workout.py
Defines the `Workout` object (made up of `ExerciseRoutine` objects).

## workout_program.py
Defines a schdule (via DAY:Workout dicts) for a full workout program.

## runner.py
Determines if the active workout program has a workout on the current day and, if so, sends the workout to the recipient list (from `--username` email).
