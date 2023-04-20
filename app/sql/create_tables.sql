-- Athlete table that contains information about athletes
CREATE TABLE IF NOT EXISTS athlete (
    athleteID INT NOT NULL PRIMARY KEY,
    fistName VARCHAR NOT NULL,
    lastName VARCHAR NOT NULL,
    age INT NOT NULL,
    gender VARCHAR NOT NULL
);

-- Exercise type table that contains information about types of exercise
CREATE TABLE IF NOT EXISTS exerciseType (
    exerciseID INT NOT NULL PRIMARY KEY,
    exerciseTypeName VARCHAR NOT NULL
)

-- Exercise table that contains information about single exercise for specific athlete
CREATE TABLE IF NOT EXISTS exercise (
    exerciseID INT NOT NULL PRIMARY KEY,
)

-- Plan table that contains information about traning plan
CREATE TABLE IF NOT EXISTS plan (
    planID INT NOT NULL PRIMARY KEY,
    planName VARCHAR NOT NULL
)
