import pandas as pd
from urllib.parse import quote
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt
from bson.json_util import dumps

import connectAndQuery as cq
import layoutFromSample1212 as lyout
import mongoDataAnalysis as mda

app = lyout.app

@app.callback(
    Output('dbNames', 'options'),
    [Input('hostNames', 'value')])
def set_host_names(selectedHost):
    if selectedHost is not None:
        try:
            databases = cq.getDbNames(selectedHost)
        except:
            databases = [{'error': 'requested database is out of reach'}]
            return [{'label': i, 'value': i} for i in databases]
    else:
        databases = []
    return [{'label': i, 'value': i} for i in databases]


@app.callback(
    Output('collectionNames', 'options'),
    [Input('hostNames', 'value'),
     Input('dbNames', 'value')])
def set_host_names(selectedHost, selectedDb):
    if selectedDb is not None:
        try:
            collections = cq.getCollections(selectedHost, selectedDb)
        except:
            collections = [{'error': 'requested collections are out of reach'}]
            return [{'label': i, 'value': i} for i in collections]
    else:
        collections = []
    return [{'label': i, 'value': i} for i in collections]


@app.callback(Output('intermediate-value', 'children'),
              [Input('button', 'n_clicks'),
               Input('hostNames', 'value'),
               Input('dbNames', 'value'),
               Input('collectionNames', 'value')],
              [State('mongoQuery', 'value')])
def data(click, host, db, collection, query):
    if click is not None:
        try:
            dataSet = cq.get_db(host, db, collection)
            queryRes = eval('dataSet.'+query)
            # queryRes = dataSet.find({})
            l = list(queryRes)
            df = pd.DataFrame(l)
            df = mda.dataCleanUp(df)
            # df = df.drop(['_id'], axis=1)
            # df = df.drop(['Earnings Date'], axis=1)
            return df.to_json(date_format='iso', orient='split')
        except:
            df = pd.DataFrame()
            return df.to_json(date_format='iso', orient='split')
    else:
        df = pd.DataFrame()
        return df.to_json(date_format='iso', orient='split')

@app.callback(
    Output('advancedTable', 'columns'),
    [Input('button', 'n_clicks'),
    Input('intermediate-value', 'children')
    ])
def getColumns(click, Jdataframe):
    if click is not None:
        try:
            df = pd.read_json(Jdataframe, orient='split')
            if df.empty:
                df = pd.DataFrame()
                return [{"name": 'empty', "id": 'empty'}]
            else:
                report = mda.nullReport(df)
                cols = [{"name": i, "id": i} for i in report.columns]
                return cols
        except:
            return [{"name": 'empty', "id": 'empty'}]
    else:
        return [{"name": 'empty', "id": 'empty'}]

@app.callback(
    dash.dependencies.Output('advancedTable', 'data'),
    [Input('button', 'n_clicks'),
    dash.dependencies.Input('intermediate-value', 'children')
    ])
def getData(click, Jdataframe):
    if click is not None:
        try:
            df = pd.read_json(Jdataframe, orient='split')
            if df.empty:
                df = pd.DataFrame()
                data = df.to_dict('records')
                return data
            else:
                report = mda.nullReport(df)
                data = report.to_dict('records')
                return data
        except:
            df = pd.DataFrame()
            data = df.to_dict('records')
            return data
    else:
        df = pd.DataFrame()
        data = df.to_dict('records')
        return data


@app.callback(
    Output('topTenTable', 'columns'),
    [Input('button', 'n_clicks'),
    Input('intermediate-value', 'children')
    ])
def getColumns(click, Jdataframe):
    if click is not None:
        try:
            df = pd.read_json(Jdataframe, orient='split')
            if df.empty:
                df = pd.DataFrame()
                return [{"name": 'empty', "id": 'empty'}]
            else:
                report = mda.topFrequent(df,10)
                cols = [{"name": i, "id": i} for i in report.columns]
                return cols
        except:
            return [{"name": 'empty', "id": 'empty'}]
    else:
        return [{"name": 'empty', "id": 'empty'}]

@app.callback(
    dash.dependencies.Output('topTenTable', 'data'),
    [Input('button', 'n_clicks'),
    dash.dependencies.Input('intermediate-value', 'children')
    ])
def getData(click, Jdataframe):
    if click is not None:
        try:
            df = pd.read_json(Jdataframe, orient='split')
            if df.empty:
                df = pd.DataFrame()
                data = df.to_dict('records')
                return data
            else:
                report = mda.topFrequent(df,10)
                data = report.to_dict('records')
                return data
        except:
            df = pd.DataFrame()
            data = df.to_dict('records')
            return data
    else:
        df = pd.DataFrame()
        data = df.to_dict('records')
        return data


@app.callback(
    dash.dependencies.Output('download-link', 'href'),
    [dash.dependencies.Input('intermediate-value', 'children')])
def update_download_link(Jdataframe):
    df = pd.read_json(Jdataframe, orient='split')
    if df.empty:
        df = pd.DataFrame()
        csv_string = df.to_csv(index=False, encoding='utf-8')
    else:
        csv_string = df.to_csv(index=False, encoding='utf-8')
        csv_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + \
            quote(csv_string)
        return csv_string

@app.callback(
    dash.dependencies.Output('download-report', 'href'),
    [dash.dependencies.Input('intermediate-value', 'children')])
def update_download_link(Jdataframe):
    df = pd.read_json(Jdataframe, orient='split')
    if df.empty:
        df = pd.DataFrame()
        csv_string = df.to_csv(index=False, encoding='utf-8')
    else:
        report = mda.nullReport(df)
        csv_string = report.to_csv(index=False, encoding='utf-8')
        csv_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + \
            quote(csv_string)
        return csv_string

@app.callback(
    dash.dependencies.Output('download-topValues', 'href'),
    [dash.dependencies.Input('intermediate-value', 'children')])
def update_download_link(Jdataframe):
    df = pd.read_json(Jdataframe, orient='split')
    if df.empty:
        df = pd.DataFrame()
        csv_string = df.to_csv(index=False, encoding='utf-8')
    else:
        report = mda.topFrequent(df,10)
        csv_string = report.to_csv(index=False, encoding='utf-8')
        csv_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + \
            quote(csv_string)
        return csv_string

if __name__ == '__main__':
    app.run_server(debug=True)
