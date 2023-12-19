from flask import Flask, render_template, request
from plotly.offline import plot
import plotly.graph_objs as go
import predictor_analysis as pa

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

#import reasons_analysis as ra
#import high_score as hs

app = Flask(__name__)

csv_file = "violence_data.csv"
#csv_file = "C:\\Users\\lgeri\\OneDrive - Technische Universität Dortmund\\M\\Lehigh\\A&SJ\\Code\\violence_data.csv"


data_df = pd.read_csv(csv_file)
#print(data_df.head())
data_df = data_df.dropna(subset=['Value'])
countries = []
countries.append("ALL")
countries.extend(data_df['Country'].unique())
questions = []
questions.append("ALL")
questions.extend(data_df['Question'].unique())

print(countries)
print(questions)

#Create Plots
def create_plots_2(selected_question,selected_country,selected_gender):
    print("country=",selected_country," quetsion=",selected_question," gender=",selected_gender)
    
    if selected_question != "ALL":
        sample_data = data_df[data_df['Question']==selected_question]
    else:
        sample_data = data_df

    if selected_country != "ALL":
        sample_data = sample_data[sample_data['Country']==selected_country]
    else:
        sample_data = sample_data

    if selected_gender != "All":
        sample_data = sample_data[sample_data['Gender']==selected_gender]
    
    plots = []
    
    fig = pa.predictor_analysis(sample_data,"Education")
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    plots.append(plot_div)

    fig = pa.predictor_analysis(sample_data,"Employment")
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    plots.append(plot_div)

    fig = pa.predictor_analysis(sample_data,"Age")
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    plots.append(plot_div)

    fig = pa.predictor_analysis(sample_data,"Residence")
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    plots.append(plot_div)

    fig = pa.predictor_analysis(sample_data,"Marital status")
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    plots.append(plot_div)

    if selected_question == 'ALL':
        fig = pa.question_analysis(sample_data)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        plots.append(plot_div)


    return plots

@app.route('/')
def index():
    selected_question = request.args.get('question','ALL')
    selected_country = request.args.get('country', 'ALL')
    selected_gender = request.args.get('gender', 'All')

    plots = create_plots_2(selected_question,selected_country,selected_gender)
    return render_template('index2.html', questions=questions, countries=countries, plots=plots, selected_country=selected_country, selected_gender = selected_gender,selected_question=selected_question)

if __name__ == '__main__':
    app.run(debug=True)