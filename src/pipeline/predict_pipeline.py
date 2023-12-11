import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        cement: float,
        blast_furnace: float,
        fly_ash : float,
        water : float,
        superplasticizer : float,
        coarse_aggregate: float,
        fine_aggregate : float,
        age : float):

        self.cement = cement

        self.blast_furnace = blast_furnace

        self.fly_ash = fly_ash

        self.water = water

        self.superplasticizer = superplasticizer

        self.coarse_aggregate = coarse_aggregate

        self.fine_aggregate = fine_aggregate

        self.age = age

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "cement": [self.cement],
                "blast_furnace": [self.blast_furnace],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
                "age" : [self.age]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
