-- ================== Utils tables ==================

-- Experience table that contains information about athlete experience level
CREATE TABLE IF NOT EXISTS Experience (
    experienceID INT UNIQUE NOT NULL,
    experienceLevel VARCHAR(100) NOT NULL,

    PRIMARY KEY (experienceID)
);

-- Exercise type table that contains information about types of exercise
CREATE TABLE IF NOT EXISTS ExerciseType (
    exerciseTypeID INT UNIQUE NOT NULL,
    exerciseTypeName VARCHAR(100) NOT NULL,

    PRIMARY KEY (exerciseTypeID)
);

-- Plan goal table that contains information about plan goals types
CREATE TABLE IF NOT EXISTS PlanGoal (
    planGoalID INT UNIQUE NOT NULL,
    goalTypeName VARCHAR(100) NOT NULL,

    PRIMARY KEY (planGoalID)
);


-- ================== Main tables ===================

-- Athlete table that contains information about athletes
CREATE TABLE IF NOT EXISTS Athlete (
    athleteID INT UNIQUE NOT NULL,
    fistName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    athleteWeight INT NOT NULL,
    gender VARCHAR(50) NOT NULL,
    experienceID INT NOT NULL,

    PRIMARY KEY (athleteID),
    FOREIGN KEY (experienceID) REFERENCES Experience(experienceID)
);

-- Plan table that contains information about traning plan
CREATE TABLE IF NOT EXISTS Plan (
    planID INT UNIQUE NOT NULL,
    planName VARCHAR(100) NOT NULL,
    planGoalID INT NOT NULL,
    planStart DATE NOT NULL,
    planEnd DATE NOT NULL,

    PRIMARY KEY (planID),
    FOREIGN KEY (planGoalID) REFERENCES PlanGoal(planGoalID)
);

-- Exercise table that contains information about single exercise for specific athlete
CREATE TABLE IF NOT EXISTS Exercise (
    exerciseID INT UNIQUE NOT NULL,
    athleteID INT NOT NULL,
    planID INT NOT NULL,
    exerciseTypeID INT NOT NULL,
    setsCount INT NOT NULL,
    repsPerSetCount INT NOT NULL,

    PRIMARY KEY (exerciseID),
    FOREIGN KEY (athleteID) REFERENCES Athlete(athleteID),
    FOREIGN KEY (planID) REFERENCES Plan(planID),
    FOREIGN KEY (exerciseTypeID) REFERENCES ExerciseType(exerciseTypeID)
);
