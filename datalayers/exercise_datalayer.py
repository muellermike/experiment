from datalayers.db import execute

def load_next_random_exercise(experimentId: int):
    """
    Load the next random exercise which has not been answered yet.
    """
    sql = "SELECT t.PK as TextID, t.Text, i.PK as ImageID, i.Mimetype, i.EncodedString FROM ExperimentParticipationExercise as epe JOIN Text as t ON epe.TextFK = t.PK JOIN Image as i ON epe.ImageFK = i.PK WHERE epe.ExperimentParticipationFK = %s AND epe.Answer IS NULL ORDER BY RAND() LIMIT 1"
    
    loaded_exercise = execute(sql, (experimentId), "SELECT")
    
    if not loaded_exercise:
        return None

    return loaded_exercise[0]

def load_random_exercises(exercise_type: str, experiment_id: int, number_of_exercises: int):
    """
    Load a number of random exercises
    """
    sql = ""
    
    # load n exercises of type exercise_type in a random order
    if(exercise_type == "text"):
        sql = "SELECT PK FROM Text WHERE ExperimentFK = %s ORDER BY RAND() LIMIT %s"
    elif (exercise_type == "image"):
        sql = "SELECT PK FROM Image WHERE ExperimentFK = %s ORDER BY RAND() LIMIT %s"
    else:
        print("no such type")
    
    loaded_exercises = execute(sql, (experiment_id, int(number_of_exercises)), "SELECT")

    return loaded_exercises