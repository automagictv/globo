import routine


class Workout(object):
    """An interface for a full workout. Typically this would be a full set of routines to do on a given day."""

    def __init__(self, name, routines):
        self.name = name
        self.routines = routines

    def as_html(self):
        """Helper method to format the routine as HTML.

        Returns:
            A `string` of HTML formatted workout routines.
        """
        routines_formatted = ''.join([routine.as_html() for routine in self.routines])
        html = f"""
            <p><b>{self.name}</b></p>
            <ul>
                {routines_formatted}
            </ul>"""

        return html
    
    def as_markdown(self):
        routines_formatted = ''.join([routine.as_markdown() for routine in self.routines])
        return f"""
        **{self.name}**
          {routines_formatted}
            """

    def __str__(self):
        return self.as_html()


# WS4SB Workouts
MaxEffortUpperBody = Workout(
    name="Max-Effort Upper Body",
    routines=[
        routine.MaxEffortExercise,
        routine.SupplementalExercise,
        routine.RearDeltSuperset,
        routine.Traps,
        routine.ElbowFlexorExercise,
    ])

DynamicEffortLowerBody = Workout(
    name="Dynamic-Effort Lower Body",
    routines=[
        routine.JumpTraining,
        routine.UnilateralExercise,
        routine.HipExtensionExercise,
        routine.WeightedAbdominals,
    ])

RepetitionUpperBody = Workout(
    name="Repetition Upper Body",
    routines=[
        routine.RepetitionExercise,
        routine.VerticalPullingDeltSuperset,
        routine.MedialDelts,
        routine.TrapsArmsSuperset,
    ])

MaxEffortLowerBody = Workout(
    name="Max-Effort Lower Body",
    routines=[
        routine.MaxEffortLift,
        routine.UnilateralMovement,
        routine.HamstringMovement,
        routine.GroundBasedAbCricuit,
    ])

# r/Fitness beginner workouts
WorkoutA = Workout(
    name="Workout A",
    routines=[
        routine.BarbellRows,
        routine.BenchPress,
        routine.Squats,
    ])

WorkoutB = Workout(
    name="Workout B",
    routines=[
        routine.Pullups,
        routine.OverheadPress,
        routine.Deadlifts,
    ])

ConditioningA = Workout(
    name="Conditioning A",
    routines=[
        routine.NoExcusesConditioningA,
    ])

ConditioningB = Workout(
    name="Conditioning B",
    routines=[
        routine.NoExcusesConditioningB,
    ])

WorkoutAWithConditioning = Workout(
    name="Workout A + Conditioning",
    routines=[
        routine.BarbellRows,
        routine.BenchPress,
        routine.Squats,
        routine.NoExcusesConditioningA,
    ])

WorkoutBWithConditioning = Workout(
    name="Workout B + Conditioning",
    routines=[
        routine.Pullups,
        routine.OverheadPress,
        routine.Deadlifts,
        routine.NoExcusesConditioningB,
    ])

StretchWorkout = Workout(
    name="Active Recovery",
    routines=[
        routine.AGTStretchRoutine,
    ])

YogaWorkoutA = Workout(
    name="Yoga - Active Recovery",
    routines=[
        routine.YogaForFlexibilityA,
    ])

YogaWorkoutB = Workout(
    name="Yoga - Active Recovery",
    routines=[
        routine.YogaForFlexibilityB,
    ])

TrekAerobicA = Workout(name="Aerobics and Trek Back A (in Hevy)", routines=[routine.AerobicTrainingA])
TrekAerobicB = Workout(name="Aerobics and Core A (in Hevy)", routines=[routine.AerobicTrainingB])
Climb = Workout(name="Climb", routines=[routine.Climb])
TrekStrength = Workout(name="Strength Training: Trek Lower A (in Hevy)", routines=[routine.TrekStrength])
FiveThreeOneWorkout = Workout(name="5/3/1 (in sheets and Hevy)", routines=[routine.FiveThreeOneRoutine])
DownDogYoga = Workout(name="DownDog Yoga", routines=[routine.DownDogYogaRoutine])
DumbbellStopgapA = Workout(name="Dumbbell stopgap A", routines=[routine.DumbbellStopgapA])
DumbbellStopgapB = Workout(name="Dumbbell stopgap B", routines=[routine.DumbbellStopgapB])
