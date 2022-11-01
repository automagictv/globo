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

def _activeRecoverySelector():
    triSwitch = (datetime.datetime.today().isocalendar()[1] % 3) == 0
    if WORKOUT_SWITCH and triSwitch:
        return workout.YogaWorkoutA
    elif triSwitch:
        return workout.YogaWorkoutB
    else:
        return workout.StretchWorkout

BasicStrengthTraining = {
    MON: workout.WorkoutA if WORKOUT_SWITCH else workout.WorkoutB,
    TUE: workout.ConditioningA if WORKOUT_SWITCH else workout.ConditioningB,
    WED: workout.WorkoutB if WORKOUT_SWITCH else workout.WorkoutA,
    THU: workout.WorkoutA if WORKOUT_SWITCH else workout.WorkoutB,
    FRI: _activeRecoverySelector(),
}

TrekTraining = {
    MON: workout.TrekAerobicA if WORKOUT_SWITCH else workout.TrekAerobicB,
    TUE: workout.Climb,
    THU: workout.TrekAerobicB if WORKOUT_SWITCH else workout.TrekAerobicA,
    FRI: workout.TrekStrength,
    SAT: _activeRecoverySelector(),
    SUN: workout.Climb,
}

# Handled via Todoist for the main schedule.
# See https://thefitness.wiki/routines/5-3-1-for-beginners/
FiveThreeOne = {
    FRI: workout.Climb,
    SUN: _activeRecoverySelector(),
}
