import datetime
import workout

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


WS4SB = {
    MON: workout.MaxEffortUpperBody,
    WED: workout.DynamicEffortLowerBody,
    FRI: workout.RepetitionUpperBody,
    SAT: workout.MaxEffortLowerBody,
}

# r/Fitness beginner routine
# https://thefitness.wiki/routines/r-fitness-basic-beginner-routine/
# Switch back and forth by week so order goes A, B, A, B, ...
WORKOUT_SWITCH = datetime.datetime.today().isocalendar()[1]

BasicStrengthTraining = {
    TUE: if WORKOUT_SWITCH workout.WorkoutA else workout.WorkoutB,
    FRI: if WORKOUT_SWITCH workout.WorkoutB else workout.WorkoutA,
    SUN: if WORKOUT_SWITCH workout.WorkoutA else workout.WorkoutB,
}
