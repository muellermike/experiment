from flask import current_app
from datalayers.experiment_datalayer import load_experiment_by_name, store_experiment_participation, store_experiment_exercises, update_experiment_endtime, load_experiment_questions, load_experiment_questions_for_experiment, load_responses_by_experiment_id
from models.experiment import Experiment
from services.exercise_service import get_experiment_exercises
import json
import pandas as pd

def create_experiment(experiment: Experiment):
    """
    implements the logic to create a new experiment. This means that first the user-experiment connection
    is established by inserting a userexperiment in the database. 
    After positive, random 12 questions of each task are loaded and stored into the database.
    """
    experiment = load_experiment_by_name(experiment.experiment_name)

    if(experiment['PK'] is None):
        return None
    
    experiment_id = experiment['PK']
    
    # the user-experiment connection is stored with the corresponding foreign keys.
    result = store_experiment_participation(experiment, experiment_id)

    # save the generated participation id into the experiment object
    experiment.id = result
    
    exercises = get_experiment_exercises(experiment['NumberOfExercises'], experiment_id)
    
    store_experiment_exercises(exercises, experiment)
    
    return result

def get_experiment_questions(experiment_id: int):
    """
    Loads the questions of an experiment. If there is no experiment for the provided participation id None is returned.
    """
    result = load_experiment_questions(experiment_id)

    # since there is only one object for questions take the first one
    retValue = {
        "questions": result[0]["Questions"]
    }
    return retValue

def update_experiment(experiment: Experiment):
    """
    implements the logic to update an existing experiment. This means that first it is checked whether the experiment participation exists and has this experiment.
    After that all allowed updated are executed.
    """
    # UPDATE endtime of experiment when the endtime is not set yet (logic in SQL Statement)
    result = update_experiment_endtime(experiment)

    return result

def download_experiment_data(experiment_name: str):
    experiment_id = get_experiment_by_name_service(experiment_name)['PK']

    columns, data_types = get_experiment_data_headers(experiment_id)

    responses = get_experiment_responses(experiment_id, columns, data_types)

    return pd.concat(responses, ignore_index= True)

def get_experiment_by_name_service(experiment_name: str):
    """
    Loads the information of an experiment. If there is no experiment for the provided participation id None is returned.
    """
    result = load_experiment_by_name(experiment_name)

    return result

def get_experiment_data_headers(experiment_id: int):
    questions = load_experiment_questions_for_experiment(experiment_id)

    data = json.loads(questions[0]['Questions'])

    sorted_columns = ['tic', 'participationID', 'isTestUser', 'experimentStart', 'experimentEnd', 'dateGenerated', 'answerStoredTimestamp', 'textID', 'textShortName', 'imageID', 'imageFilename']
    data_types = {}

    # iterate through experiment groups
    for d in data:
        # go through all questions in a group
        for q in d['questions']:
            # Flatten JSON data
            flat_data = {k: v if not isinstance(v, dict) else json.dumps(v) for k, v in q.items()}

            # get internal name of the questions and append it to the columns
            sorted_columns.append(flat_data['internalName'])
            # eppend answerTime to the columns
            sorted_columns.append(flat_data['internalName'] + ".answerTime")
            
            # store data type of the answer into a dict to validate the data
            # if answerType specified with the question take it from there
            if "answerType" in flat_data:
                data_types[flat_data['internalName']] = eval(flat_data['answerType'])['answerDataType']
            else: # otherwise take it from parent (for example in a table question)
                data_types[flat_data['internalName']] = d['answerType']['answerDataType']

    return sorted_columns, data_types

def get_experiment_responses(experiment_id: int, columns: list, data_type: dict):
    responses = load_responses_by_experiment_id(experiment_id)
    
    df_list = []
    for res in responses:
        # initialize answer_entry
        answer_entry = {}
        # get general response information
        answer_entry['tic'] = res.get('tic')
        answer_entry['participationID'] = res.get('ParticipationID')
        answer_entry['isTestUser'] = res.get('IsTestUser')
        answer_entry['experimentStart'] = res.get('ExperimentStart')
        answer_entry['experimentEnd'] = res.get('ExperimentEnd')
        answer_entry['dateGenerated'] = res.get('DateGenerated')
        answer_entry['answerStoredTimestamp'] = res.get('AnswerStoredTimestamp')
        answer_entry['textID'] = res.get('TextID')
        answer_entry['textShortName'] = res.get('ShortText')
        answer_entry['imageID'] = res.get('ImageID')
        answer_entry['imageFilename'] = res.get('Filename')

        if res.get("Answer") is not None:
            answer = eval(res.get("Answer"))
            # iterate through groups
            for g in answer:
                answer_entry[g["answer"]["questionName"]] = g["answer"]["answerValue"]
                answer_entry[g["answer"]["questionName"] + ".answerTime"] = g["answer"]["answerTime"]
        else:
            print("None answer")
        
        df = pd.DataFrame.from_dict([answer_entry])
        df = df.reindex(columns = columns)
        df_list.append(df)

    return df_list