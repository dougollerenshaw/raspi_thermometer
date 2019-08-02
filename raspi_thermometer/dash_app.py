import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
import random

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Thermometer(
        id='my-thermometer',
        value=5,
        min=30,
        max=110,
        style={
            'margin-bottom': '5%'
        },
        showCurrentValue=True,
        units="F",
        label='Current temperature',
        labelPosition='top',
        color='red'
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    ),
])


@app.callback(
    dash.dependencies.Output('my-thermometer', 'value'),
    [dash.dependencies.Input('interval-component', 'n_intervals')])
def update_thermometer(n_intervals):
    value = random.uniform(40,100)
    print('temp = {}'.format(value))
    return value


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=80)