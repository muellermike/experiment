from datalayers.exercise_datalayer import load_next_random_exercise, load_random_exercises
from datalayers.experiment_datalayer import load_experiment_exercise, load_user_experiment, update_experiment_exercise
from models.exercise_answer import ExerciseAnswer
from models.user import User

def get_experiment_exercises(number_of_ex: int, experiment_id: int):
    """
    loads a defined number of randomized experiment questions
    """

    # load random texts and random images
    text_ex = get_experiment_exercises_by_type("text", experiment_id, number_of_ex)
    image_ex = get_experiment_exercises_by_type("image", experiment_id, number_of_ex)

    return {"text": text_ex, "image": image_ex}

def get_experiment_exercises_by_type(exercise_type: str, experiment_id: int, num_of_ex: int):
    # load random exercises by type
    exercises = load_random_exercises(exercise_type, experiment_id, num_of_ex)
    return exercises

def get_next_random_exercise(experimend_id: int):
    """
    gets the next randomly selected exercise for the user experiment
    """

    # load the next exercise
    exercise = load_next_random_exercise(experimend_id)

    # when the exercise is None than there are two possibilities: 
    # either there is no experiment-participation with this id for the user 
    # or there are no more exercises
    if exercise is None:
        # check whether the user-participation exists
        user_ex = load_user_experiment(experimend_id)
        if user_ex is None:
            # if the experiment for the user doesn't exist, return None
            return None
        else:
            # otherwise the experiment exists but there are no more exericeses to solve -> return empty object
            return ()

    return exercise

def update_exercise_answer(exercise: ExerciseAnswer):
    """
    checks all parameter and stores the exercise answer then
    """
    # before storing the recording it is checked, whether this user_experiment exists.
    user_ex = load_user_experiment(exercise.experiment_id)
    
    if user_ex is None:
        # if the experiment for the user doesn't exist, return None
        return None
    
    # check that this exercise has not been answered yet
    ex = load_experiment_exercise(exercise.experiment_id, exercise.text_id, exercise.image_id)
    
    # if exercise hasn't been found or is already anwered, than return None
    if not ex or ex[0]["Answer"] is not None is not None:
        return None

    # set the answer of the current experiment exercise
    hasUpdated = update_experiment_exercise(exercise)

    return hasUpdated
