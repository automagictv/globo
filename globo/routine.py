import random
import exercise
import itertools


class ExerciseRoutine(object):
    """Interface to define an exercise routine.

    Routines are descriptions / notes combined with a set of exercises. Typically,
    they will represent one group, or part, of a full workout.
    """

    def __init__(self, name, description, exercises, n_exercises=1):
        """Constructor for the ExerciseRoutine object.

        Args:
            name: `string` The name of hte routine.
            description: `string` A description for the routine.
            exercises: `list` A list of `Exercise` objects that make up the routine.
            n_exercises: `int` The number of exercises that make up the reoutine. Defaults to 1.
        """
        if len(exercises) < n_exercises:
            raise ValueError(f"n_exercises must be <= exercises. Got n_exercises = {n_exercises} "
                             f"for {len(exercises)} exercises.")

        self.name = name
        self.description = description
        self.exercises = exercises
        self.n_exercises = n_exercises

        self.exercises_for_routine = [] 

    def get_exercises(self):
        """Randomly chooses and returns self.n_exercises for the routine.

        Exercises will not repeat.

        Returns:
            A `list` of `Exercise` objects.
        """
        if not self.exercises_for_routine:
            exercises = self.exercises[:]
            for _ in range(self.n_exercises):
                ind = random.randint(0, len(exercises) - 1)
                self.exercises_for_routine.append(exercises.pop(ind))

        return self.exercises_for_routine
    
    def as_html(self):
        """Formats the routine as a list element with a nested list of exercises.

        Returns:
            A `string` formatted as an html list.
        """
        exercises_formatted = ''.join(
            [f"<li>{exercise}</li>" for exercise in self.get_exercises()])
        return f"""
            <li><b>{self.name}</b> {self.description.rstrip(".")}:
                <ul>
                    {exercises_formatted}
                </ul>
            </li>
            """

    def __str__(self):
        return self.as_html()


class SupersetRoutine(ExerciseRoutine):
    """Interface for a superset routine.

    This is a slight derivation from a normal exercise routine.
    """

    def __init__(self, name, description, exercise_groups, n_exercises=1):
        for exercises in exercise_groups:
            if len(exercises) < n_exercises:
                raise ValueError(f"n_exercises must be <= exercises. Got n_exercises = {n_exercises} "
                                 f"for {len(exercises)} exercises.")

        exercises = itertools.chain.from_iterable(exercise_groups)
        super().__init__(name, description, exercises, n_exercises)
        self.exercise_groups = exercise_groups

    def get_exercises(self):
        if not self.exercises_for_routine:
            for exercise_group in self.exercise_groups:
                exercises = exercise_group[:]
                for _ in range(self.n_exercises):
                    ind = random.randint(0, len(exercises) - 1)
                    self.exercises_for_routine.append(exercises.pop(ind))

        return self.exercises_for_routine


# Monday routines
MaxEffortExercise = ExerciseRoutine(
    name="Max-Effort Exercise",
    description="Work up to a max set of 3-5 reps.",
    exercises=[
        exercise.BenchPress,
        exercise.BarbellFloorPress,
        exercise.InclineBarbellBenchPress,
        exercise.WeightedChinUps,
    ])

SupplementalExercise = ExerciseRoutine(
    name="Supplemental Exercise",
    description=("Perform 2 sets of max reps. Choose a weight you can perform 15-20 reps on the 1st set. "
                 "Use the same weight for both sets and rest 3-4 minutes in between."),
    exercises=[
        exercise.FlatDBBenchPress,
        exercise.InclineDBBenchPress,
        exercise.DBFloorPress,
    ])

RearDeltSuperset = SupersetRoutine(
    name="Horizontal pulling / Rear delt superset",
    description="Superset! Perform 3-4 supersets of 8-12 reps of each exercise.",
    exercises=[
        [
            exercise.DBRows,
            exercise.BarbellRows,
            exercise.SeatedCableRows,
            exercise.TBarRows,
            exercise.ChestSupportedRows,
        ], [
            exercise.RearDeltFlyes,
            exercise.Scarecrows,
            exercise.FacePulls,
            exercise.SeatedDBPowerCleans,
            exercise.BandPullAparts,
        ]
    ])

Traps = ExerciseRoutine(
    name="Traps",
    description="Perform 3-4 sets of 8-15 reps.",
    exercises=[
        exercise.DBShrugs,
        exercise.BarbellShrugs,
    ])


ElbowFlexorExercise = ExerciseRoutine(
    name="Elbow flexor exercise",
    description="Perform 3-4 sets of 8-15 reps.",
    exercises=[
        exercise.BarbellCurls,
        exercise.StandingDBCurls,
        exercise.SeatedInclineDBCurls,
        exercise.HammerCurls,
        exercise.ZottmanCurls,
        exercise.IsoHoldDBCurls,
    ])

# Tuesday routines
JumpTraining = ExerciseRoutine(
    name="Jump training",
    description="Perform 5-8 sets of 1-3 jumps",
    exercises=[
        exercise.BoxJumps,
        exercise.VerticalJumps,
        exercise.BroadJumps,
        exercise.HurdleHops,
        exercise.BoxSquatIntoBoxJump,
        exercise.DepthJumps,
    ])

UnilateralExercise = ExerciseRoutine(
    name="Unilateral exercise (w/ added ROM)",
    description="Perform 2-3 sets of 8-10 reps.",
    exercises=[
        exercise.BulgarianSplitSquats,
        exercise.BarbellReverseLunge,
        exercise.BarbellReverseLungeKneeLift,
        exercise.StepUps,
    ])

HipExtensionExercise = ExerciseRoutine(
    name="Hip extension exercise",
    description="Perform 3 sets of 8-12 reps.",
    exercises=[
        exercise.FortyFiveDegreeHyperextensions,
        exercise.ReverseHyperextensions,
        exercise.PullThroughs,
        exercise.SwissBallBackBridgeLegCurl,
        exercise.GluteHamRaise,
        exercise.RomanianDeadlift,
    ])

WeightedAbdominals = ExerciseRoutine(
    name="Weighted Abdominals",
    description="Perform 4 sets of 10-15 reps.",
    exercises=[
        exercise.DBSideBends,
        exercise.OffsetBarbellSideBends,
        exercise.BarbellRussianTwists,
        exercise.LowCablePullIns,
        exercise.HangingLegRaises,
        exercise.WeightedSwissBallCrunches,
        exercise.SpreadEagleSitUps,
        exercise.StandingSitUps,
    ])

# Thursday routines
RepetitionExercise = ExerciseRoutine(
    name="Repetition Exercise",
    description="Perform 3 sets of max reps OR 4 sets of 12-15 reps.",
    exercises=[
        exercise.FlatDBBenchPress,
        exercise.InclineDBBenchPress,
        exercise.DBBenchPressOnSwissBall,
        exercise.DBFloorPress,
        exercise.PushUpVariations,
        exercise.ChinUpVariations,
        exercise.BarbellBenchPress,
    ])

VerticalPullingDeltSuperset = SupersetRoutine(
    name="Vertical pulling / Rear delt superset",
    description="Superset! Perform 3-4 supersets of 8-12 reps of each exercise.",
    exercises=[
        [
            exercise.LatPulldowns,
            exercise.StraightArmPulldowns,
        ], [
            exercise.RearDeltFlyes,
            exercise.Scarecrows,
            exercise.FacePulls,
            exercise.SeatedDBPowerCleans,
            exercise.BandPullAparts,
        ]
    ])

MedialDelts = ExerciseRoutine(
    name="Medial delts",
    description="Perform 4 sets of 8-12 reps.",
    exercises=[
        exercise.DBLateralRaises,
        exercise.LLateralRaises,
        exercise.CableLateralRaises,
        exercise.DBMilitaryPress,
        exercise.DBSidePress,
    ])

TrapsArmsSuperset = SupersetRoutine(
    name="Traps / Arms superset",
    description="Superset! Perform 3 supersets of 8-10 reps of each exercise.",
    exercises=[
        [
            exercise.DBShrugs,
            exercise.BarbellShrugs,
        ], [
            exercise.BarbellCurls,
            exercise.StandingDBCurls,
            exercise.SeatedInclineDBCurls,
            exercise.HammerCurls,
            exercise.ZottmanCurls,
            exercise.IsoHoldDBCurls,
        ]
    ])

# Friday exercises
MaxEffortLift = ExerciseRoutine(
    name="Max-effort lift",
    description="Work up to a max set of 3-5 reps.",
    exercises=[
        exercise.BoxSquats,
        exercise.FreeSquats,
        exercise.StraightBarDeadlifts,
        exercise.RackPulls,
    ])

UnilateralMovement = ExerciseRoutine(
    name="Unilateral Movement",
    description="Perform 3 sets of 6-12 reps.",
    exercises=[
        exercise.BulgarianSplitSquats,
        exercise.ReverseLungeVariations,
        exercise.StepUpVariations,
    ])

HamstringMovement = ExerciseRoutine(
    name="Hamstring / Posterior Chain Movement",
    description="Perform 3 sets of 8-12 reps.",
    exercises=[
        exercise.FortyFiveDegreeHyperextensions,
        exercise.ReverseHyperextensions,
        exercise.PullThroughs,
        exercise.SwissBallBackBridgeLegCurl,
        exercise.GluteHamRaise,
        exercise.RomanianDeadlift,
    ])

GroundBasedAbCricuit = ExerciseRoutine(
    name="Ground-based, high-rep abdominal circuit",
    description=("Perform 10-20 reps of each exercise and go through the circuit 2-3 times. "
                 "Rest 1-2 mins between circuits."),
    exercises=[exercise.AbdominalCircuit])
