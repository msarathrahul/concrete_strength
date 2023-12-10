import streamlit
import pickle
import numpy as np
import pandas as pd

header = streamlit.container()
data_container = streamlit.container()
prediction = streamlit.container()

with header:
    streamlit.title('Welcome to Concrete compressive strength prediction \nWeb application')
    streamlit.text("By Sarath Rahul Malla")
    streamlit.header('Project Summary : Concrete Compressive Strength Prediction')
    streamlit.text("In this project, I successfully developed a robust machine learning model for predicting \nconcrete compressive strength with a commendable R2 score of 0.91 and a Root Mean \nSquared Error (RMSE) of 4.9.")

    streamlit.header("Methodology :")
    streamlit.text("Utilizing advanced techniques, I implemented ensemble learning and hyperparameter tuning to enhance the predictive performance of the model. Ensemble methods, such as bagging or boosting, were instrumental in aggregating the strengths of multiple models, leading to a more accurate and reliable outcome.")

    streamlit.header("Feature Engineering :")
    streamlit.text("Employing advanced feature engineering techniques played a pivotal role in optimizing \nthe model's ability to discern patterns within the dataset. This process involved \ntransforming and selecting relevant features to extract meaningful insights and \nimprove overall predictive accuracy.")
    streamlit.text("The achieved R2 score of 0.91 reflects the model's high explanatory power, indicating \nits proficiency in capturing the variance in concrete compressive strength. The RMSE \nof 4.9 further underscores the precision of the model's predictions, showcasing its \neffectiveness in quantifying the error between predicted and actual values.")
    streamlit.text("This project stands as a testament to the successful application of sophisticated \nmethodologies in the realm of machine learning, contributing valuable insights to \nthe field of engineering.")
with data_container:
    streamlit.header("Dataset description : Concrete compressive strength")
    streamlit.text('Source:')
    streamlit.text("Original Owner and Donor: Prof. I-Cheng Yeh,\nDepartment of Information Management,\nChung-Hua University, Hsin Chu,\nTaiwan 30067, R.O.C.\n\n")

    streamlit.header("Data overview")
    streamlit.text("Type : Multivariate")
    streamlit.text("Abstract : Concrete is a fundamental material in civil engineering, and its compressive \nstrength is a complex function dependent on age and various ingredients. These ingredients \nencompass cement, blast furnace slag, fly ash, water, superplasticizer, coarse \naggregate, and fine aggregate.")

    streamlit.header('Data characterstics')
    streamlit.text('Instances : 1030')
    streamlit.text("Attributes : 9")
    streamlit.text("- 8 quantitative input variables")
    streamlit.text("- 1 quantitative output variable (Concrete Compressive Strength in MPa)")
    streamlit.text('Data Form: Raw, not scaled')

    streamlit.header('Variable information')
    streamlit.text("1. Cement (component 1) - Quantitative - kg/m3 mixture - Input Variable")
    streamlit.text("2. Blast Furnace Slag (component 2) - Quantitative - kg/m3 mixture - Input Variable")
    streamlit.text("3. Fly Ash (component 3) - Quantitative - kg/m3 mixture - Input Variable")
    streamlit.text("4. Water (component 4) - Quantitative - kg/m3 mixture - Input Variable")
    streamlit.text("5. Superplasticizer (component 5) - Quantitative - kg/m3 mixture - Input Variable")
    streamlit.text("6. Coarse Aggregate (component 6) - Quantitative - kg/m3 mixture - Input Variable")
    streamlit.text("7. Fine Aggregate (component 7) - Quantitative - kg/m3 mixture - Input Variable")
    streamlit.text("8. Age - Quantitative - Day (1~365) - Input Variable")

    streamlit.header('Objective')
    streamlit.text('Regression problem to predict concrete compressive strength.')


                
with prediction:
    streamlit.header('Time for predicting Concrete compressive strength')
    streamlit.text('Please enter the values of the following features : ')
    cement = streamlit.slider("Cement quantity (kg/m3)", min_value=140.0, max_value=500.0, value = 150.0)
    blast_furnace_slag = streamlit.slider("Blast Furnace Slag (kg/m3)", min_value=0.0, max_value=260.0, value = 237.0)
    fly_ash = streamlit.slider("Fly Ash (kg/m3)", min_value=0.0, max_value=170.0, value = 0.0)
    water = streamlit.slider("Water (kg/m3)", min_value=140.0, max_value=220.0, value = 174.0)
    superplasticizer = streamlit.slider("Superplasticizer (kg/m3)", min_value=0.0, max_value=18.0, value = 12.0)
    coarse_aggregate = streamlit.slider("Coarse Aggregate (kg/m3)", min_value=820.0, max_value=1120.0, value = 1069.0)
    fine_aggregate = streamlit.slider("Fine Aggregate (kg/m3)", min_value=600.0, max_value=900.0, value = 675.0)
    age = streamlit.slider("Age (days)", min_value=3.0, max_value=270.0, value = 28.0)

#Loading the model
with open('notebooks/models/model.pkl','rb') as file:
    model = pickle.load(file)

columns = ['cement','blast_furnace_slag','fly_ash','water','superplasticizer','coarse_aggregate','fine_aggregate','age']
data_dict = {'cement' : [cement],
             'blast_furnace_slag' : [blast_furnace_slag],
             'fly_ash' : [fly_ash],
             'water' : [water],
             'superplasticizer' : [superplasticizer],
             'coarse_aggregate' : [coarse_aggregate],
             'fine_aggregate ': [fine_aggregate],
             'age' : [age]}

df = pd.DataFrame(data = data_dict)
pred = (model.predict(df)[0])

streamlit.text('The Concrete compressive strength is : ')
streamlit.write(pred)

streamlit.header("By Sarath Rahul Malla")
streamlit.text('Thanks for visiting')