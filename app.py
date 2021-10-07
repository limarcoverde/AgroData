from functions import*

VALID_USERNAME_PASSWORD_PAIRS = {
    'garoa': '123',
    'startup':'123',
    'investidor':'123',
}


app = dash.Dash(__name__)
server = app.server

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.title = "AgroData"

tabs_styles,tab_style,tab_selected_style = tabStyles()

app.layout = html.Div([
                createHeader(),
                dcc.Tabs(
                        id="tabs-styled-with-inline", 
                        value='tab-1', 
                        children=[
                                dcc.Tab(
                                        label='Inserção dos dados', 
                                        children=[
                                                html.Div([
                                                        CreateMenu(
                                                                className="menu-header",
                                                                children=[
                                                                        html.Div(
                                                                                className='drops',
                                                                                children=[
                                                                                        html.H5("Digite o nome da nova Startup"),
                                                                                        dcc.Input(id='my-input',placeholder='Enter a value...',value='',type='text'),
                                                                                        html.H3("Empreendedorismo"),
                                                                                        html.H5("A Startup entende como o mercado opera?"),
                                                                                        dcc.Dropdown(
                                                                                                id="drop1",
                                                                                                options=[
                                                                                                        {'label': 'Sim.', 'value': 'True'},
                                                                                                        {'label': 'não.', 'value': 'False'},
                                                                                                ],
                                                                                                searchable=False
                                                                                        ),
                                                                                        html.H5("A startup consegue construir um produto?"),
                                                                                        dcc.Dropdown(
                                                                                                id="drop2",
                                                                                                options=[
                                                                                                        {'label': 'Sim.', 'value': 'True'},
                                                                                                        {'label': 'não.', 'value': 'False'},
                                                                                                ],
                                                                                                searchable=False
                                                                                        ),
                                                                                        html.H5("A startup consegue explicar a transformação?"),
                                                                                        dcc.Dropdown(
                                                                                                id="drop3",
                                                                                                options=[
                                                                                                        {'label': 'Sim.', 'value': 'True'},
                                                                                                        {'label': 'não.', 'value': 'False'},
                                                                                                ],
                                                                                                searchable=False
                                                                                        ),
                                                                                        html.H5("A startup experenciou problema?"),
                                                                                        dcc.Dropdown(
                                                                                                id="drop4",
                                                                                                options=[
                                                                                                        {'label': 'Sim.', 'value': 'True'},
                                                                                                        {'label': 'não.', 'value': 'False'},
                                                                                                ],
                                                                                                searchable=False
                                                                                        ),
                                                                                        html.H5("A startup consegue evidênciar a solução?"),
                                                                                        dcc.Dropdown(
                                                                                                id="drop5",
                                                                                                options=[
                                                                                                        {'label': 'Sim.', 'value': 'True'},
                                                                                                        {'label': 'não.', 'value': 'False'},
                                                                                                ],
                                                                                                searchable=False
                                                                                        ),
                                                                                        html.Button('Submit', id='submit-val', n_clicks=0),
                                                                                ]
                                                                        )       
                                                                ]
                                                        )
                                                ])
                                        ],
                                        style=tab_style, 
                                        selected_style=tab_selected_style
                                ),
                                                
                                dcc.Tab(
                                        label='Visualização dos dados', 
                                        children=[
                                                html.Div(
                                                        className='tab2',
                                                        children=[
                                                                html.H5("Grafico dos Empreendedores"),
                                                                dcc.Graph(
                                                                        id='example-graph-2'
                                                                ),
                                                                html.Button('Atualizar o Grafico', id='submit-val1', n_clicks=0),
                                                        ]
                                                ),
                                        ],
                                        style=tab_style, 
                                        selected_style=tab_selected_style
                                ),
                        ], 
                        style=tabs_styles
                ),
                html.Div(id="container-button-timestamp"),
        ]
)

@app.callback(Output('submit-val', 'n_clicks'),
              Input('my-input', 'value'),
              Input('drop1', 'value'),
              Input('drop2', 'value'),
              Input('drop3', 'value'),
              Input('drop4', 'value'),
              Input('drop5', 'value'),
              Input('submit-val', 'n_clicks')
              )
def insertion(inputStartup,drop1,drop2,drop3,drop4,drop5,n_clicks):
        if (n_clicks == 1):
                flag = check(inputStartup,drop1,drop2,drop3,drop4,drop5)
                if(flag == 0):
                        write(inputStartup,drop1,drop2,drop3,drop4,drop5)
                else:
                        print("Deu ruim pai")
        n_clicks = 0
        return n_clicks

@app.callback(Output('example-graph-2', 'figure'),
              Input('submit-val1', 'n_clicks'))
def figGraph(n_clicks):
        listStartup = []
        listCount = []
        count = 0
        df1 = pd.read_csv("data/db.csv")
        listStartup = df1["Startups"]
        stats1 = df1["Entender_como_mercado_opera"]
        stats2 = df1["Consegue_construir_produto"]
        stats3 = df1["Explicar_transformacao"]
        stats4 = df1["Experenciou_problema"]
        stats5 = df1["Evidencia_de_Solucao"]

        
        for i in range(len(listStartup)):
                if(stats1[i] == True):
                        count += 1
                if(stats2[i] == True):
                        count += 1
                if(stats3[i] == True):
                        count += 1
                if(stats4[i] == True):
                        count += 1
                if(stats5[i] == True):
                        count += 1
                listCount.append(count)
                count = 0

        fig = go.Figure(data=[go.Scatter(x=listStartup, y=listCount)])
        return fig

if __name__ == '__main__':
    app.run_server(debug=True)