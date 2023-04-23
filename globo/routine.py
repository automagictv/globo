import random
import exercise
import itertools


class ExerciseRoutine(object):
    """Interface to define an exercise routine.

    Routines are instructionss / notes combined with a set of exercises. Typically,
    they will represent one group, or part, of a full workout.
    """

    def __init__(self, name, instructions, exercises, include_all=False):
        """Constructor for the ExerciseRoutine object.

        Args:
            name: `string` The name of hte routine.
            instructions: `string` Instructions for the routine.
            exercises: `list` A list of `Exercise` objects that make up the routine.
            include_all: `boolean` Flag to include all exercises.
        """
        self.name = name
        self.instructions = instructions
        self.exercises = exercises
        self.include_all = include_all

        self.exercises_for_routine = [] 
    
    def get_exercises(self):
        """Randomly chooses and returns exercises for the routine.

        Exercises will not repeat.

        Returns:
            A `list` of `Exercise` objects.
        """
        if not self.exercises_for_routine:
            if self.include_all:
                self.exercises_for_routine = self.exercises[::]
            else:
                self.exercises_for_routine.append(random.choice(self.exercises))

        return self.exercises_for_routine
    
    def as_html(self):
        """Formats the routine as a list element with a nested list of exercises.

        Returns:
            A `string` formatted as an html list.
        """
        exercises_formatted = ''.join(
            [f"<li>{exercise}</li>" for exercise in self.get_exercises()])
        return f"""
            <li><b>{self.name}</b> {self.instructions.rstrip(".")}:
                <ul>
                    {exercises_formatted}
                </ul>
            </li>"""

    def as_markdown(self):
        """Formats the routine as a nested list of markdown links."""
        exercises_formatted = ''.join([
            f"- {exercise.as_markdown()}\n"
            for exercise in self.get_exercises()
        ])
        return f"""
          - {self.name} {self.instructions.rstrip(".")}:
            {exercises_formatted}
            """

    def __str__(self):
        return self.as_html()


class SupersetRoutine(ExerciseRoutine):
    """Interface for a superset routine.

    This is a slight derivation from a normal exercise routine.
    """

    def __init__(self, name, instructions, exercise_groups):
        # Reformat exercise_groups to be a single list so we can use the
        # parent constructor.
        _unused_exercises = itertools.chain.from_iterable(exercise_groups)
        super().__init__(name, instructions, _unused_exercises)
        self.exercise_groups = exercise_groups

    def get_exercises(self):
        """Overwrites the get_exercises method to work with an exercise list of lists."""
        if not self.exercises_for_routine:
            for exercise_group in self.exercise_groups:
                self.exercises_for_routine.append(random.choice(exercise_group))

        return self.exercises_for_routine


# Monday routines
MaxEffortExercise = ExerciseRoutine(
    name="Max-Effort Exercise",
    instructions="Work up to a max set of 3-5 reps.",
    exercises=[
        exercise.BenchPress,
        exercise.BarbellFloorPress,
        exercise.InclineBarbellBenchPress,
        exercise.WeightedChinUps,
    ])

SupplementalExercise = ExerciseRoutine(
    name="Supplemental Exercise",
    instructions=("Perform 2 sets of max reps. Choose a weight you can perform 15-20 reps on the 1st set. "
                  "Use the same weight for both sets and rest 3-4 minutes in between."),
    exercises=[
        exercise.FlatDBBenchPress,
        exercise.InclineDBBenchPress,
        exercise.DBFloorPress,
    ])

RearDeltSuperset = SupersetRoutine(
    name="Horizontal pulling / Rear delt superset",
    instructions="Superset! Perform 3-4 supersets of 8-12 reps of each exercise.",
    exercise_groups=[
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
    instructions="Perform 3-4 sets of 8-15 reps.",
    exercises=[
        exercise.DBShrugs,
        exercise.BarbellShrugs,
    ])


ElbowFlexorExercise = ExerciseRoutine(
    name="Elbow flexor exercise",
    instructions="Perform 3-4 sets of 8-15 reps.",
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
    instructions="Perform 5-8 sets of 1-3 jumps",
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
    instructions="Perform 2-3 sets of 8-10 reps.",
    exercises=[
        exercise.BulgarianSplitSquats,
        exercise.BarbellReverseLunge,
        exercise.BarbellReverseLungeKneeLift,
        exercise.StepUps,
    ])

HipExtensionExercise = ExerciseRoutine(
    name="Hip extension exercise",
    instructions="Perform 3 sets of 8-12 reps.",
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
    instructions="Perform 4 sets of 10-15 reps.",
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
    instructions="Perform 3 sets of max reps OR 4 sets of 12-15 reps.",
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
    instructions="Superset! Perform 3-4 supersets of 8-12 reps of each exercise.",
    exercise_groups=[
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
    instructions="Perform 4 sets of 8-12 reps.",
    exercises=[
        exercise.DBLateralRaises,
        exercise.LLateralRaises,
        exercise.CableLateralRaises,
        exercise.DBMilitaryPress,
        exercise.DBSidePress,
    ])

TrapsArmsSuperset = SupersetRoutine(
    name="Traps / Arms superset",
    instructions="Superset! Perform 3 supersets of 8-10 reps of each exercise.",
    exercise_groups=[
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
    instructions="Work up to a max set of 3-5 reps.",
    exercises=[
        exercise.BoxSquats,
        exercise.FreeSquats,
        exercise.StraightBarDeadlifts,
        exercise.RackPulls,
    ])

UnilateralMovement = ExerciseRoutine(
    name="Unilateral Movement",
    instructions="Perform 3 sets of 6-12 reps.",
    exercises=[
        exercise.BulgarianSplitSquats,
        exercise.ReverseLungeVariations,
        exercise.StepUpVariations,
    ])

HamstringMovement = ExerciseRoutine(
    name="Hamstring / Posterior Chain Movement",
    instructions="Perform 3 sets of 8-12 reps.",
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
    instructions=("Perform 10-20 reps of each exercise and go through the circuit 2-3 times. "
                  "Rest 1-2 mins between circuits."),
    exercises=[exercise.AbdominalCircuit])

# r/Fitness beginner routines
BarbellRows = ExerciseRoutine(
    name="Barbell Rows",
    instructions=("Perform 3 sets of 5 reps, going 1-2 reps before failure on the last set. "
                  "Finish all 3 sets before moving on."),
    exercises=[exercise.BarbellRows])

BenchPress = ExerciseRoutine(
    name="Bench Press",
    instructions=("Perform 3 sets of 5 reps, going 1-2 reps before failure on the last set. "
                  "Finish all 3 sets before moving on."),
    exercises=[exercise.BarbellBenchPress])

Squats = ExerciseRoutine(
    name="Free Squats",
    instructions=("Perform 3 sets of 5 reps, going 1-2 reps before failure on the last set. "
                  "Finish all 3 sets before moving on."),
    exercises=[exercise.FreeSquats])

Pullups = ExerciseRoutine(
    name="Pullups / Chinups",
    instructions=("Perform 3 sets of 5 reps, going 1-2 reps before failure on the last set. "
                  "Finish all 3 sets before moving on."),
    exercises=[exercise.WeightedChinUps])

OverheadPress = ExerciseRoutine(
    name="Overhead Barbell Press",
    instructions=("Perform 3 sets of 5 reps, going 1-2 reps before failure on the last set. "
                  "Finish all 3 sets before moving on."),
    exercises=[exercise.BarbellOverheadPress])

Deadlifts = ExerciseRoutine(
    name="Deadlifts",
    instructions=("Perform 3 sets of 5 reps, going 1-2 reps before failure on the last set. "
                  "Finish all 3 sets before moving on."),
    exercises=[exercise.StraightBarDeadlifts])

NoExcusesConditioningA = ExerciseRoutine(
    name="No Excuses! (Conditioning)",
    instructions=("Perform each exercise one after another with no breaks for "
                  "4 sets. Exercise time for each set: 60, 45, 30, 15 for 10 "
                  "minutes total (60x4 + 45x4 + 30x4 + 15x4)."),
    exercises=[
        exercise.Burpees,
        exercise.Pullups,
        exercise.BodyweightSquats,
        exercise.PushUpVariations,
    ],
    include_all=True
)

NoExcusesConditioningB = ExerciseRoutine(
    name="No Excuses! (Conditioning)",
    instructions=("Perform each exercise one after another with no breaks for "
                  "4 sets. Exercise time for each set: 60, 45, 30, 15 for 10 "
                  "minutes total (60x4 + 45x4 + 30x4 + 15x4)."),
    exercises=[
        exercise.MountainClimbers,
        exercise.JumpLunge,
        exercise.Bicycle,
        exercise.Burpees,
    ],
    include_all=True
)

AGTStretchRoutine = ExerciseRoutine(
    name="Static Stretching!",
    instructions="Follow the link for instructions.",
    exercises=[exercise.AGTStretchRoutine]
)

YogaForFlexibilityA = ExerciseRoutine(
    name="Yoga for Flexibility (A)",
    instructions="Do this yoga!",
    exercises=[exercise.YogaA]
)

YogaForFlexibilityB = ExerciseRoutine(
    name="Yoga for Flexibility (B)",
    instructions="Do this yoga!",
    exercises=[exercise.YogaB]
)

AerobicTrainingA = ExerciseRoutine(
    name="Aerobic Training",
    instructions="20-60 minutes of training. Keep HR between 135-145 for Aerobic base training. Then do Trek Back A in Hevy.",
    exercises=[
        exercise.AerobicA,
        exercise.BackA
    ],
    include_all=True
)

AerobicTrainingB = ExerciseRoutine(
    name="Aerobic Training",
    instructions="20-60 minutes of training. Keep HR between 135-145 for Aerobic base training. Then do Core A in Hevy.",
    exercises=[
        exercise.AerobicA,
        exercise.CoreA
    ],
    include_all=True
)

Climb = ExerciseRoutine(
    name="Climb",
    instructions="Hit the wall baby!",
    exercises=[exercise.Climb]
)

TrekStrength = ExerciseRoutine(
    name="Trek Lower A in Hevy",
    instructions="Hit it hard.",
    exercises=[exercise.LowerA]
)

FiveThreeOneRoutine = ExerciseRoutine(
    name="5/3/1",
    instructions="Hit it hard.",
    exercises=[exercise.FiveThreeOne]
)

DownDogYogaRoutine = ExerciseRoutine(
    name="DownDog Yoga",
    instructions="Get loose!",
    exercises=[exercise.DownDogYoga]
)

DumbbellStopgapA = ExerciseRoutine(
    name="Dumbbell Stopgap A in Hevy",
    instructions="You may be tired, but let's get it done!",
    exercises=[exercise.DumbbellStopgapA]
)

DumbbellStopgapB = ExerciseRoutine(
    name="Dumbbell Stopgap B in Hevy",
    instructions="You may be tired, but let's get it done!",
    exercises=[exercise.DumbbellStopgapB]
)
