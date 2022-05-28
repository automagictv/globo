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
            <p>Don't forget to <a href="https://www.youtube.com/watch?v=qQ96oXp5RTU">warm up</a>!</p>
            <ul>
                {routines_formatted}
            </ul>"""

        return html

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
        routone.Deadlifts,
    ])

WorkoutAWithConditioning = Workout(
    name="Workout A + Conditioning",
    routines=[
        routine.BarbellRows,
        routine.BenchPress,
        routine.Squats,
    ])

WorkoutBWithConditioning = Workout(
    name="Workout B + Conditioning",
    routines=[
        routine.Pullups,
        routine.OverheadPress,
        routone.Deadlifts,
    ])
