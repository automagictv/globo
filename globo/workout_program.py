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
    TUE: workout.WorkoutA if WORKOUT_SWITCH else workout.WorkoutB,
    FRI: workout.WorkoutB if WORKOUT_SWITCH else workout.WorkoutA,
    SUN: workout.WorkoutA if WORKOUT_SWITCH else workout.WorkoutB,
}
