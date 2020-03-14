import numpy as np
import pandas as pd
import plotly.figure_factory as ff


def __transform(data: pd.DataFrame) -> pd.DataFrame:
    output = pd.DataFrame()
    output['Task'] = data['MethodName']
    output['Start'] = data['StartTime']
    output['Finish'] = data['EndTime']
    output['Description'] = data['ElapsedTimeInMS'].map(np.ceil).map(str) + ' ms'
    output['Resource'] = data['MethodName'] + ' (' + data['ProcessId'].map(str) + ',' + data['ThreadId'].map(str) + ')'
    output.sort_values(by='Start', ascending=True)
    return output


def visualize_performance(filename):
    data = pd.read_csv(filename)
    table = __transform(data)
    fig = ff.create_gantt(table, index_col='Resource', show_colorbar=True, group_tasks=False,
                          showgrid_x=True, title='performance visualization')

    fig.show()
