from pyexpat import model
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

def predictor_analysis(data_dff,predictor):
    filtered_df = data_dff.loc[data_dff.DemographicsQuestion ==predictor]
    if predictor == "Marital status":
        predictor = "MaritalStatus"
    filtered_df = filtered_df.rename(columns={'DemographicsResponse': predictor})

    #activate seperated histplot
    #value_histogram(filtered_df,predictor)


    if predictor == "Education":
        mapping = {'No education': 1, 'Primary': 2,'Secondary':3, 'Higher':4}
    if predictor == "Employment":
        mapping = {"Unemployed": 1, "Employed for kind": 2,"Employed for cash":3}
    if predictor == "Age":
        mapping = {"15-24": 1, "25-34": 2,"35-49":3}
    if predictor == "Residence":
        mapping = {"Urban": 1, "Rural": 2}
    if predictor == "MaritalStatus":
        mapping = {"Never married": 1,"Widowed, divorced, separated": 2, "Married or living together": 3}

    #filtered_df = filtered_df.replace({predictor: mapping})
    #print(filtered_df.head())

    #activate correlation heatmap
    cheatmap_fig = cheatmap(filtered_df,predictor)

    #activate threshold model
    #threshold_model(filtered_df,15)


    return cheatmap_fig


def question_analysis(data_dff):
    #filtered_df = data_dff.loc[data_dff.DemographicsQuestion ==predictor]

    #filtered_df = filtered_df.rename(columns={'DemographicsResponse': predictor})

    #activate seperated histplot
    #value_histogram(filtered_df,predictor)

    #mapping = {'No education': 1, 'Primary': 2,'Secondary':3, 'Higher':4}
    #filtered_df = filtered_df.replace({predictor: mapping})

    #print(filtered_df.head())

    #activate correlation heatmap
    cheatmap_fig = cheatmap2(data_dff)

    #activate threshold model
    #threshold_model(filtered_df,15)


    return cheatmap_fig

def value_histogram(df,predictor):
    categories = df[predictor].unique()
    plt.figure()
    fig, ax = plt.subplots()
    alpha = 0.25
    for category in categories:
        category_data = df[df[predictor] == category]['Value']
        ax.hist(category_data, bins=10, alpha=alpha, label=category)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
    ax.legend()
    plt.show()
    return

def cheatmap(df,predictor):
    #fig = go.Figure(go.Histogram2dDensity(x=df[predictor], y=df["Value"]))
    fig = px.density_heatmap(df, x=predictor, y="Value")
    #fig.show()
    return fig

def cheatmap2(df):
    #fig = go.Figure(go.Histogram2dDensity(x=df[predictor], y=df["Value"]))
    fig = px.density_heatmap(df, x='Question', y="Value")
    #fig.show()
    return fig

def threshold_model(filtered_df,accpetance_level):
    def categorize_value(value):
        if value < accpetance_level:
            return 0
        else:
            return 1
    filtered_df["High_Acceptance"] = filtered_df['Value'].apply(categorize_value)
    #filtered_df = filtered_df.dropna(subset=['EducationLevel', 'Value'])

    sns.histplot(data=filtered_df[filtered_df["High_Acceptance"]==1], x="EducationLevel", discrete=True, color='purple', alpha=0.5)
    sns.histplot(data=filtered_df[filtered_df["High_Acceptance"]==0], x="EducationLevel", discrete=True, color='green', alpha=0.5)
    plt.legend(labels=["High Acceptance", "Low Acceptance"])
    plt.show()
    return

