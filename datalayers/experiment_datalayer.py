import random
from datalayers.db import execute
from models.exercise_answer import ExerciseAnswer
from models.experiment import Experiment

def load_experiment_by_name(experiment_name: str):
    """
    Get experiment information by its name but only return first found experiment.
    Experiment name should be unique in db.
    """
    sql = "SELECT PK, NumberOfExercises, NextText, Introduction, FinalPageTexts FROM Experiment WHERE ExperimentName = %s"
    userexperiment_id = execute(sql, (experiment_name), "SELECT")

    if (not userexperiment_id):
        return None

    return userexperiment_id[0]

def load_experiment_questions(experiment_id: int):
    """
    Get the experiment question by the participation id
    """
    sql = "SELECT Questions FROM Experiment e JOIN ExperimentParticipation ep ON e.PK = ep.ExperimentFK WHERE ep.PK = %s"
    questions = execute(sql, (experiment_id), "SELECT")

    return questions

def load_experiment_questions_for_experiment(experiment_id: int):
    """
    Get the experiment question by the participation id
    """
    sql = "SELECT Questions FROM Experiment e WHERE e.PK = %s"
    questions = execute(sql, (experiment_id), "SELECT")

    return questions

def store_experiment_participation(user_experiment: Experiment, experiment_id: int):
    """
    Store experiment with the information into the database
    """
    sql = "INSERT INTO ExperimentParticipation (ExperimentFK, OriginID, Start) VALUES (%s, %s, %s)"
    
    userexperiment_id = execute(sql, (experiment_id, user_experiment.origin_id, user_experiment.start), "INSERT")

    return userexperiment_id

def store_experiment_exercises(exercises, experiment: Experiment):
    """
    Stores all experiment exercises into the database
    """
    # sql statement to insert multi rows
    sql = "INSERT INTO ExperimentParticipationExercise (ExperimentParticipationFK, TextFK, ImageFK) VALUES (%s, %s, %s)"

    # create list with the experiment id and the exercise id to insert into the database
    experiment_exercises = list([(experiment.id, exercises["text"][i]["PK"], exercises["image"][i]["PK"]) for i in range(len(exercises["text"]))])
    random.shuffle(experiment_exercises)

    # execute the INSERT MANY statement
    execute(sql, (experiment_exercises), "INSERT MANY")

    return True

def update_experiment_exercise(exercise: ExerciseAnswer):
    """
    Updates the experiment exercise with the answer
    """
    sql = "UPDATE ExperimentParticipationExercise SET Answer = %s, AnswerStoredTimestamp = %s, TimeToClick = %s, TimeToSubmit = %s WHERE ExperimentParticipationFK = %s AND TextFK = %s AND ImageFK = %s"
    execute(sql, (exercise.answer, exercise.time, exercise.time_to_click, exercise.time_to_submit, exercise.experiment_id, exercise.text_id, exercise.image_id), "UPDATE")

    return True

def update_experiment_endtime(experiment: Experiment):
    """
    Updates the experiment endtime
    """
    # sql statement to update experiment endtime
    sql = "UPDATE ExperimentParticipation SET End = %s WHERE PK = %s AND End IS NULL"

    # execute the UPDATE statement
    execute(sql, (experiment.end, experiment.id), "UPDATE")

    return True

def load_user_experiment(experiment_id: int):
    """
    Loads a specific experiment for a specific user
    """
    # sql statement for the experiment load
    sql = "SELECT * FROM ExperimentParticipation WHERE PK = %s"

    # execute sql statement
    result = execute(sql, (experiment_id), "SELECT")

    if not result:
        return None

    return result

def load_experiment_exercise(experiment_id: int, text_id: int, image_id: int):
    """
    Loads a specific experiment exercise by experiment id and exercise id
    """
    # sql statement for the selection
    sql = "SELECT * FROM ExperimentParticipationExercise WHERE ExperimentParticipationFK = %s AND TextFK = %s AND ImageFK = %s"

    # execute sql statement
    result = execute(sql, (experiment_id, text_id, image_id), "SELECT")

    return result

def load_responses_by_experiment_id(experiment_id: int):
    """
    Load all responses of an experiment
    """
    # sql statement for the selection
    sql = "SELECT ep.PK as ParticipationID, ep.OriginID as tic, ep.IsTestUser, ep.Start as ExperimentStart, ep.End as ExperimentEnd, epe.DateGenerated, epe.AnswerStoredTimestamp, t.PK as TextID, t.ShortText, i.PK as ImageID, i.Number as ImageNumber, i.Filename, epe.Answer FROM ExperimentParticipationExercise epe JOIN ExperimentParticipation ep ON epe.ExperimentParticipationFK = ep.PK JOIN Text t ON epe.TextFK = t.PK JOIN Image i ON epe.ImageFK = i.PK WHERE ep.ExperimentFK = %s ORDER BY ep.OriginID"

    # execute sql statement
    result = execute(sql, (experiment_id), "SELECT")

    return result