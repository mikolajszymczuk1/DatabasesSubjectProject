from enum import Enum

class TablesEnum(Enum):
    """ Enum with all tables names """

    EXPERIENCE_TABLE = 'experience'
    EXERCISE_TYPE_TABLE = 'exerciseType'
    PLAN_GOAL_TABLE = 'planGoal'

    ATHLETE_TABLE = 'athlete'
    PLAN_TABLE = 'plan'
    EXERCISE_TABLE = 'exercise'

    @staticmethod
    def getValues() -> list[str]:
        return [
            TablesEnum.EXPERIENCE_TABLE.value,
            TablesEnum.EXERCISE_TYPE_TABLE.value,
            TablesEnum.PLAN_GOAL_TABLE.value,
            TablesEnum.ATHLETE_TABLE.value,
            TablesEnum.PLAN_TABLE.value,
            TablesEnum.EXERCISE_TABLE.value
        ]
