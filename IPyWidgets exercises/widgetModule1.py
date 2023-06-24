import ipywidgets as widgets
from IPython.display import display

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# url = "C:\\Users\\dkrizman\\Desktop\\international-visitors-london-raw.csv"
# df_london = pd.read_csv(url)

ALL = 'ALL'
def uniqueSortedValues(df):
    unique = df.unique().tolist()
    unique.sort
    unique.insert(0,ALL)
    return unique



# def dropDownYearEventHandler(change):
#     outputYear.clear_output()
#     with outputYear:
#         if change.new == ALL:
#             display(df_london)
#         else:
#             display(df_london[df_london.year == change.new])

class dashboard:
    
    ALL = 'ALL'
    
    def uniqueSortedValues(df):
        unique = df.unique().tolist()
        unique.sort
        unique.insert(0,ALL)
        return unique
    
    def __init__(self, df_london):
        self.df_london = df_london
        self.output = widgets.Output()
        self.pltOutput = widgets.Output()
        self.dropdownYear = widgets.Dropdown(options = uniqueSortedValues(df_london.year), description = 'year')
        self.dropdownPurpose = widgets.Dropdown(options = uniqueSortedValues(df_london.purpose), description = 'purpose')
        
    
    def commonFiltering(self, year, purpose):
        self.output.clear_output()
        self.pltOutput.clear_output()
        
        if year == ALL and purpose == ALL:
            commonFilter = self.df_london
        elif year == ALL:
            commonFilter = self.df_london[self.df_london.purpose == purpose]
        elif purpose == ALL:
            commonFilter = self.df_london[self.df_london.year == year]
        else:
            commonFilter = self.df_london[(self.df_london.year == year) & (self.df_london.purpose == purpose)]
            
        with self.output:
            display(commonFilter)
            
        with self.pltOutput:
            sns.kdeplot(commonFilter['Visits'], shade = True)
            plt.show()

    def dropDownYearEventHandler(self, change):
        self.commonFiltering(change.new, self.dropdownPurpose.value)
        
    def dropDownPurposeEventHandler(self, change):
        self.commonFiltering(self.dropdownYear.value, change.new)
    
    def runDashboard(self):
        self.dropdownYear.observe(self.dropDownYearEventHandler, names = 'value')
        self.dropdownPurpose.observe(self.dropDownPurposeEventHandler, names = 'value')

        item_layout = widgets.Layout(margin='0 0 50px 0')

        inputWidgets = widgets.HBox([self.dropdownYear, self.dropdownPurpose], layout = item_layout)

        tab = widgets.Tab([self.output, self.pltOutput], layout = item_layout)
        tab.set_title(0, 'Dataset exploration')
        tab.set_title(1, 'KDE Plot')

        dashboard = widgets.VBox([inputWidgets, tab])

        # display(inputWidgets)
        # display(output)
        # display(pltOutput)
        # display(tab)
        display(dashboard)