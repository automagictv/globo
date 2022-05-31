"""
All exercise files.
"""


class Exercise(object):
    """Object that defines the exercise interface."""

    def __init__(self, name, url):
        """Constructs an Exercise object with a name and url.

        Args:
            name: `string` The name of the exercise.
            url: `string` A url to a video of the exercise to depict proper form.
        """
        self.name = name
        self.url = url

    def as_html(self):
        """Formats the exercise as an html link."""
        return f"{self.name} (<a href=\"{self.url}\">example</a>)"

    def __str__(self):
        return self.as_html()


# Exercise Definitions
BenchPress = Exercise(
    "Bench Press",
    "https://www.youtube.com/watch?v=UaOwz6DNdjw")

BarbellFloorPress = Exercise(
    "Barbell floor press",
    "https://www.youtube.com/watch?v=9vYCwtHkWgI")

InclineBarbellBenchPress = Exercise(
    "Incline barbell bench press (regular grip or close grip)",
    "https://www.youtube.com/watch?v=11gY7Q5D5wo")

WeightedChinUps = Exercise(
    "Weighted chin-ups",
    "https://www.youtube.com/watch?v=7FiR9W_gVF0")

FlatDBBenchPress = Exercise(
    "Flat DB bench press (palms in or out)",
    "https://www.youtube.com/watch?v=omGiL5h2R_I")

InclineDBBenchPress = Exercise(
    "Incline DB bench press (palms in or out)",
    "https://www.youtube.com/watch?v=0G2_XV7slIg")

DBFloorPress = Exercise(
    "DB floor press (palms in)",
    "https://www.youtube.com/watch?v=A2dfGvoykPc")

DBRows = Exercise(
    "DB rows",
    "https://www.youtube.com/watch?v=PgpQ4-jHiq4")

BarbellRows = Exercise(
    "Barbell rows",
    "https://www.youtube.com/watch?v=I-qgwlP0J90")

SeatedCableRows = Exercise(
    "Seated cable rows (various bars)",
    "https://www.youtube.com/watch?v=a8qvJ2VDd9g")

TBarRows = Exercise(
    "T-bar rows",
    "https://www.youtube.com/watch?v=KDEl3AmZbVE")

ChestSupportedRows = Exercise(
    "Chest supported rows",
    "https://www.youtube.com/watch?v=H75im9fAUMc")

RearDeltFlyes = Exercise(
    "Rear delt flyes",
    "https://www.youtube.com/watch?v=0GSu6Z-Oj7U")

Scarecrows = Exercise(
    "Scarecrows",
    "https://www.youtube.com/watch?v=YakiNOaMMAA")

FacePulls = Exercise(
    "Face pulls",
    "https://www.youtube.com/watch?v=rep-qVOkqgk")

SeatedDBPowerCleans = Exercise(
    "Seated DB 'power cleans'",
    "https://www.youtube.com/watch?v=kvVEz-tBgvg")

BandPullAparts = Exercise(
    "Band pull-aparts",
    "https://www.youtube.com/watch?v=fo3ogdhMFLo")

DBShrugs = Exercise(
    "DB shrugs",
    "https://www.youtube.com/watch?v=g6qbq4Lf1FI")

BarbellShrugs = Exercise(
    "Barbell shrugs",
    "https://www.youtube.com/watch?v=NAqCVe2mwzM")

BarbellCurls = Exercise(
    "Barbell curls (regular or thick bar)",
    "https://www.youtube.com/watch?v=kwG2ipFRgfo")

StandingDBCurls = Exercise(
    "DB curls (standing)",
    "https://www.youtube.com/watch?v=av7-8igSXTs")

SeatedInclineDBCurls = Exercise(
    "Seated incline DB curls",
    "https://www.youtube.com/watch?v=soxrZlIl35U")

HammerCurls = Exercise(
    "Hammer curls",
    "https://www.youtube.com/watch?v=TwD-YGVP4Bk")

ZottmanCurls = Exercise(
    "Zottmann curls",
    "https://www.youtube.com/watch?v=FSGDM9-dZ9w")

IsoHoldDBCurls = Exercise(
    "Iso-hold DB curls",
    "https://www.youtube.com/watch?v=ooXEcYEdyGo")

BoxJumps = Exercise(
    "Box jumps",
    "http://www.youtube.com/watch?v=VK11KovyaP8&mode=related&search=")

VerticalJumps = Exercise(
    "Vertical jumps",
    "https://youtu.be/RgboWFzSUKo?t=46")

BroadJumps = Exercise(
    "Broad jumps",
    "https://youtu.be/P0N68OQDhNs?t=95")

HurdleHops = Exercise(
    "Hurdle hops (jump over hurdle and land on ground)",
    "https://youtu.be/0H_fXWTUSiY?t=49")

BoxSquatIntoBoxJump = Exercise(
    "Box squat into box jump",
    "http://www.youtube.com/watch?v=9PEdhxELbDQ")

DepthJumps = Exercise(
    "Depth jumps (onto box)",
    "http://www.youtube.com/watch?v=S6664b4UrGs")

BulgarianSplitSquats = Exercise(
    "Bulgarian split squats, front leg elevated (holding DB's or with a barbell)",
    "http://www.youtube.com/watch?v=RZlodHgCipk")

BarbellReverseLunge = Exercise(
    "Barbell reverse lunge, front foot elevated",
    "https://www.youtube.com/watch?v=zJkMQPZiwAc")

BarbellReverseLungeKneeLift = Exercise(
    "Barbell reverse lunge with knee lift (front foot elevated)",
    "https://www.youtube.com/watch?v=jU9y6hvJ40o")

StepUps = Exercise(
    "Step-ups (box height slightly above knee)",
    "https://www.youtube.com/watch?v=sZsmorjSzBM")

FortyFiveDegreeHyperextensions = Exercise(
    "45-degree hyperextensions",
    "https://www.youtube.com/watch?v=ry45nfO-PAU")

ReverseHyperextensions = Exercise(
    "Reverse hyperextensions",
    "https://www.youtube.com/watch?v=3d9_W--eUcI")

PullThroughs = Exercise(
    "Pull-throughs",
    "https://www.youtube.com/watch?v=DbSF7ipBh5Y")

SwissBallBackBridgeLegCurl = Exercise(
    "Swiss ball back bridge + leg curl",
    "https://www.youtube.com/watch?v=65W4XfSzP8U")

GluteHamRaise = Exercise(
    "Glute-ham raises",
    "https://www.youtube.com/watch?v=vSOCqsr1wlg")

RomanianDeadlift = Exercise(
    "Romanian deadlift",
    "https://www.youtube.com/watch?v=2SHsk9AzdjA")

DBSideBends = Exercise(
    "DB side bends",
    "https://www.youtube.com/watch?v=dL9ZzqtQI5c")

OffsetBarbellSideBends = Exercise(
    "Offset barbell side bends",
    "https://www.youtube.com/watch?v=1uI-7cwf9Tw")

BarbellRussianTwists = Exercise(
    "Barbell Russian twists",
    "https://www.youtube.com/watch?v=TImmxdzX0gk")

LowCablePullIns = Exercise(
    "Low cable or band pull-ins",
    "https://www.youtube.com/watch?v=sKtxdAgznB4")

HangingLegRaises = Exercise(
    "Hanging leg raises",
    "https://www.youtube.com/watch?v=arWjJtMsqvA")

WeightedSwissBallCrunches = Exercise(
    "Weighted Swiss ball crunches",
    "https://www.youtube.com/watch?v=Xdqgs6wK8eY")

SpreadEagleSitUps = Exercise(
    "Spread-eagle sit-ups (holding DB over chest)",
    "https://www.youtube.com/watch?v=kuMlr3Lkd8A")

StandingSitUps = Exercise(
    "Standing sit-ups (using a band or a high pulley)",
    "https://www.youtube.com/watch?v=ij3lWMnoFzA")

DBBenchPressOnSwissBall = Exercise(
    "DB bench press on Swiss ball (palms in or out)",
    "https://www.youtube.com/watch?v=uxgA5qEi2mc")

PushUpVariations = Exercise(
    "Push-up variations (choose 1 and do it)",
    "https://www.youtube.com/watch?v=FU_5LPjtjus")

ChinUpVariations = Exercise(
    "Chin-up variations (choose 1 and do it)",
    "https://www.youtube.com/watch?v=zaJQtvKkl6g")

BarbellBenchPress = Exercise(
    "Barbell bench press (55-60% of 1RM)",
    "http://www.youtube.com/watch?v=E-kNUEv0YgA")

LatPulldowns = Exercise(
    "Lat pulldowns (various bars)",
    "https://www.youtube.com/watch?v=84oCEetzdS4")

StraightArmPulldowns = Exercise(
    "Straight arm pulldowns",
    "https://www.youtube.com/watch?v=n3O1jkQyXC4")

DBLateralRaises = Exercise(
    "DB lateral raises",
    "https://www.youtube.com/watch?v=geenhiHju-o")

LLateralRaises = Exercise(
    "L-lateral raises",
    "https://www.youtube.com/watch?v=bXC7eL0H7AA")

CableLateralRaises = Exercise(
    "Cable lateral raises",
    "https://www.youtube.com/watch?v=IVBacQ0Q3Bw")

DBMilitaryPress = Exercise(
    "DB military press",
    "https://www.youtube.com/watch?v=qEwKCR5JCog")

DBSidePress = Exercise(
    "DB side press",
    "https://www.youtube.com/watch?v=Eyd-e7J3zFI")

BoxSquats = Exercise(
    "Box squats (regular bar, safety squat bar, cambered bar, buffalo bar)",
    "http://www.youtube.com/watch?v=paAR3wjFFks")

FreeSquats = Exercise(
    "Free squats (regular bar, safety squat bar, cambered bar, buffalo bar)",
    "http://www.youtube.com/watch?v=7IkyiekPIrg&NR=1",)

StraightBarDeadlifts = Exercise(
    "Straight bar deadlifts",
    "https://www.youtube.com/watch?v=L0vuwx9Q9VI")

RackPulls = Exercise(
    "Rack pulls",
    "https://www.youtube.com/watch?v=e11lVmLsvFU")

AbdominalCircuit = Exercise(
    "Abdominal circuit",
    "https://www.youtube.com/watch?v=izDf0MCR2DU")

ReverseLungeVariations = Exercise(
    "Reverse lunge variations",
    "https://www.youtube.com/watch?v=k_KoxW5Kpus")

StepUpVariations = Exercise(
    "Step up variations",
    "https://www.youtube.com/watch?v=dQqApCGd5Ss")

BarbellOverheadPress = Exercise(
    "Barbell Overhead Press",
    "https://www.youtube.com/watch?v=_RlRDWO2jfg")

Burpees = Exercise(
    "Burpees",
    "https://www.youtube.com/watch?v=qLBImHhCXSw")

Pullups = Exercise(
    "Pullups",
    "https://www.youtube.com/watch?v=eGo4IYlbE5g")

BodyweightSquats = Exercise(
    "Squats (bodyweight)",
    "https://youtu.be/R1v152b72lo?t=64")

AGTStretchRoutine = Exercise(
    "AGT Stretch Routine (follow link)",
    "https://agt.degreesofclarity.com/stretching/")
