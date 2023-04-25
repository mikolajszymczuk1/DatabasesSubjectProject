-- Basic data for Experience table
INSERT INTO Experience (experienceID, experienceLevel)
    VALUES
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Elite'),
        (5, 'Professional'),
        (6, 'Olympic/World-class'),
        (7, 'All-Star/Champion'),
        (8, 'Hall of Fame/Legendary');

-- Basic data for ExerciseType table
INSERT INTO ExerciseType (exerciseTypeID, exerciseTypeName)
    VALUES
        (1, 'Regular pushups'),
        (2, 'Wide pushups'),
        (3, 'Bench press'),
        (4, 'Squats with elevated legs'),
        (5, 'Deadlifts'),
        (6, 'Lat pulldowns'),
        (7, 'Bicep curls'),
        (8, 'Tricep extensions'),
        (9, 'Calf raises'),
        (10, 'Leg press'),
        (11, 'Hammer curls'),
        (12, 'Shoulder press'),
        (13, 'Incline bench press'),
        (14, 'Barbell rows'),
        (15, 'Dumbbell flys'),
        (16, 'Chest dips'),
        (17, 'Reverse flys'),
        (18, 'Lunges'),
        (19, 'Crunches'),
        (20, 'Plank');

-- Basic data for PlanGoal table
INSERT INTO PlanGoal (planGoalID, goalTypeName)
    VALUES
        (1, 'Weight loss'),
        (2, 'Muscle gain'),
        (3, 'Endurance building'),
        (4, 'Flexibility improvement'),
        (5, 'Strength training'),
        (6, 'Cardiovascular health improvement'),
        (7, 'Sport-specific training'),
        (8, 'Injury rehabilitation'),
        (9, 'Postural improvement'),
        (10, 'Overall fitness enhancement');


-- Basic data for Athlete table
INSERT INTO Athlete (athleteID, firstName, lastName, age, athleteWeight, gender, experienceID)
    VALUES
        (1, 'John', 'Doe', 25, 66, 'Male', 3),
        (2, 'Jane', 'Doe', 28, 86, 'Female', 2),
        (3, 'Michael', 'Johnson', 55, 190, 'Male', 4),
        (4, 'Sarah', 'Lee', 23, 90, 'Female', 1),
        (5, 'David', 'Smith', 32, 78, 'Male', 5),
        (6, 'Emily', 'Wong', 27, 58, 'Female', 2),
        (7, 'James', 'Kim', 29, 70, 'Male', 4),
        (8, 'Linda', 'Nguyen', 24, 60, 'Female', 1),
        (9, 'Brandon', 'Chen', 31, 68, 'Male', 5),
        (10, 'Sophia', 'Park', 26, 72, 'Female', 3);

-- Basic data for Plan table
INSERT INTO Plan (planID, planName, planGoalID, planStart, planEnd)
    VALUES
        (1, 'Weight Loss Plan', 1, '2023-05-01', '2023-06-30'),
        (2, 'Muscle Gain Plan', 2, '2023-06-01', '2023-07-31'),
        (3, 'Endurance Building Plan', 3, '2023-07-01', '2023-08-31'),
        (4, 'Flexibility Improvement Plan', 4, '2023-08-01', '2023-09-30'),
        (5, 'Strength Training Plan', 5, '2023-09-01', '2023-10-31');

-- Basic data for Exercise table
INSERT INTO Exercise (exerciseID, athleteID, planID, exerciseTypeID, setsCount, repsPerSetCount)
    VALUES
        (1, 1, 1, 1, 3, 10),
        (2, 1, 1, 2, 3, 10),
        (3, 2, 2, 3, 4, 8),
        (4, 2, 2, 4, 3, 12),
        (5, 3, 3, 5, 5, 5),
        (6, 3, 3, 6, 3, 10),
        (7, 4, 4, 7, 3, 12),
        (8, 4, 4, 8, 3, 12),
        (9, 5, 5, 9, 4, 10),
        (10, 5, 5, 10, 4, 10),
        (11, 6, 1, 11, 3, 10),
        (12, 6, 1, 12, 3, 10),
        (13, 7, 2, 13, 4, 8),
        (14, 7, 2, 14, 3, 12),
        (15, 8, 3, 15, 3, 12),
        (16, 8, 3, 16, 3, 12),
        (17, 9, 4, 17, 3, 10),
        (18, 9, 4, 18, 3, 10),
        (19, 10, 5, 19, 4, 10),
        (20, 10, 5, 20, 4, 10);
