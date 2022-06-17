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
WORKOUT_SWITCH = (datetime.datetime.today().isocalendar()[1] % 2) == 0

BasicStrengthTraining = {
    TUE: workout.WorkoutAWithConditioning if WORKOUT_SWITCH else workout.WorkoutBWithConditioning,
    FRI: workout.WorkoutBWithConditioning if WORKOUT_SWITCH else workout.WorkoutAWithConditioning,
    SAT: workout.StretchWorkout,
    SUN: workout.WorkoutA if WORKOUT_SWITCH else workout.WorkoutB,
}
