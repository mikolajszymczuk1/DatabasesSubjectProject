-- Test data for Experience table
INSERT INTO Experience (experienceID, experienceLevel)
    VALUES
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Elite');

-- Test data for ExerciseType table
INSERT INTO ExerciseType (exerciseTypeID, exerciseTypeName)
    VALUES
        (1, 'Regular pushups'),
        (2, 'Wide pushups'),
        (3, 'Bench press'),
        (4, 'Squats with elevated legs');

-- Test data for PlanGoal table
INSERT INTO PlanGoal (planGoalID, goalTypeName)
    VALUES
        (1, 'Weight loss'),
        (2, 'Muscle gain'),
        (3, 'Endurance building'),
        (4, 'Flexibility improvement');


-- Test data for Athlete table
INSERT INTO Athlete (athleteID, firstName, lastName, age, athleteWeight, gender, experienceID)
    VALUES
        (1, 'John', 'Doe', 25, 66, 'Male', 3),
        (2, 'Jane', 'Doe', 28, 86, 'Female', 2),
        (3, 'Michael', 'Johnson', 55, 190, 'Male', 4),
        (4, 'Sarah', 'Lee', 23, 90, 'Female', 1);

-- Test data for Plan table
INSERT INTO Plan (planID, planName, planGoalID, planStart, planEnd)
    VALUES
        (1, 'Weight Loss Plan', 1, '2023-05-01', '2023-06-30'),
        (2, 'Muscle Gain Plan', 2, '2023-06-01', '2023-07-31'),
        (3, 'Endurance Building Plan', 3, '2023-07-01', '2023-08-31'),
        (4, 'Flexibility Improvement Plan', 4, '2023-08-01', '2023-09-30');

-- Test data for Exercise table
INSERT INTO Exercise (exerciseID, athleteID, planID, exerciseTypeID, setsCount, repsPerSetCount)
    VALUES
        (1, 1, 1, 1, 3, 10),
        (2, 1, 1, 2, 3, 10),
        (3, 2, 2, 3, 4, 8),
        (4, 2, 2, 4, 3, 12);
