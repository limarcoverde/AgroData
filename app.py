from functions import*

VALID_USERNAME_PASSWORD_PAIRS = {
    'garoa': '123',
    'startup':'123',
    'investidor':'123',
}

app = dash.Dash(__name__)
server = app.server

auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)

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
                                                                                        html.H5("Qual o nome da statup?"),
                                                                                        dcc.Dropdown(id='my-input',options=[
                                                                                                        {'label': 'Startup 1', 'value': 'Startup 1'},
                                                                                                        {'label': 'Startup 2', 'value': 'Startup 2'},
                                                                                                ],
                                                                                                searchable=False
                                                                                        ),
                                                                                        html.H5("Qual o mês da operação? "),
                                                                                        dcc.Dropdown(id='drop1',options=[
                                                                                                        {'label': 'Janeiro', 'value': 'Janeiro'},
                                                                                                        {'label': 'Fevereiro', 'value': 'Fevereiro'},
                                                                                                        {'label': 'Março', 'value': 'Março'},
                                                                                                        {'label': 'Abril', 'value': 'Abril'},
                                                                                                        {'label': 'Maio', 'value': 'Maio'},
                                                                                                        {'label': 'Junho', 'value': 'Junho'},
                                                                                                        {'label': 'Julho', 'value': 'Julho'},
                                                                                                        {'label': 'Agosto', 'value': 'Agosto'},
                                                                                                        {'label': 'Setembro', 'value': 'Setembro'},
                                                                                                        {'label': 'Outubro', 'value': 'Outubro'},
                                                                                                        {'label': 'Novembro', 'value': 'Novembro'},
                                                                                                        {'label': 'Dezembro', 'value': 'Dezembro'},

                                                                                                ],
                                                                                                searchable=False
                                                                                        ),
                                                                                        html.H5("Qual a quantidade de pessoas entrevistadas? "),
                                                                                        dcc.Input(id="drop2",placeholder='Enter a value...',value='',type='text'),
                                                                                        html.H5("Qual a quantidade de clientes gerados?"),
                                                                                        dcc.Input(id="drop3",placeholder='Enter a value...',value='',type='text'),
                                                                                        html.H5("Qual a quantidade de pessoas impactadas"),
                                                                                        dcc.Input(id="drop4",placeholder='Enter a value...',value='',type='text'),
                                                                                        html.H5("qual a quantidade de novos parceiros?"),
                                                                                        dcc.Input(id="drop5",placeholder='Enter a value...',value='',type='text'),
                                                                                        html.H5("Qual a receita da startup?"),
                                                                                        dcc.Input(id="drop6",placeholder='Enter a value...',value='',type='text'),
                                                                                        html.H5("Quanto foi o dinheiro investido?"),
                                                                                        dcc.Input(id="drop7",placeholder='Enter a value...',value='',type='text'),
                                                                                        html.H5("Quanto foi o numero de integrantes?"),
                                                                                        dcc.Input(id="drop8",placeholder='Enter a value...',value='',type='text'),
                                                                                        html.H5("Quanto foi o numero de integrantes novos?"),
                                                                                        dcc.Input(id="drop9",placeholder='Enter a value...',value='',type='text'),
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
                                                        className='tab1',
                                                        children=[
                                                                html.H5("Escolha a startup: "),
                                                                dcc.Dropdown(
                                                                        id='dropdown-Name',
                                                                        options=[
                                                                                {'label': 'Startup 1', 'value': 'Startup 1'},
                                                                                {'label': 'Startup 2', 'value': 'Startup 2'},
                                                                        ],
                                                                        searchable=False
                                                                ),
                                                                html.Button('Atualizar informações', id='submit-name', n_clicks=0),
                                                        ]
                                                ),
                                                html.Div(
                                                        className='tab2',
                                                        children=[
                                                                html.H5("Gráfico - Receitas"),
                                                                dcc.Graph(
                                                                        id='example-graph-1'
                                                                ),
                                                        ]
                                                ),
                                                html.Div(
                                                        className='tab3',
                                                        children=[
                                                                html.H5("Gráfico - Novos Clientes"),
                                                                dcc.Graph(
                                                                        id='example-graph-2'
                                                                ),
                                                        ]
                                                ),
                                                html.Div(
                                                        className='tab3',
                                                        children=[
                                                                html.H5("Gráfico - Novos Parceiros"),
                                                                dcc.Graph(
                                                                        id='example-graph-3'
                                                                ),
                                                        ]
                                                ),
                                                html.Div(
                                                        className='tab2',
                                                        children=[
                                                                html.H5("Gráfico - Alcance total"),
                                                                dcc.Graph(
                                                                        id='example-graph-4'
                                                                ),
                                                        ]
                                                ),

                                        ],
                                        style=tab_style, 
                                        selected_style=tab_selected_style
                                ),

                                dcc.Tab(
                                        label='Comparações', 
                                        children=[
                                                html.Div(
                                                        className='tab3',
                                                        children=[
                                                                html.H5("Escolha as startups para comparação: "),
                                                                dcc.Dropdown(
                                                                        id='dropd1',
                                                                        options=[
                                                                                {'label': 'Startup 1 - 2020', 'value': 'Startup 1-20'},
                                                                                {'label': 'Startup 1 - 2021', 'value': 'Startup 1-21'},
                                                                                {'label': 'Startup 2 - 2020', 'value': 'Startup 2-20'},
                                                                                {'label': 'Startup 2 - 2021', 'value': 'Startup 2-21'},
                                                                        ],
                                                                        searchable=False
                                                                ),
                                                                dcc.Dropdown(
                                                                        id='dropd2',
                                                                        options=[
                                                                                {'label': 'Startup 1 - 2020', 'value': 'Startup 1-20'},
                                                                                {'label': 'Startup 1 - 2021', 'value': 'Startup 1-21'},
                                                                                {'label': 'Startup 2 - 2020', 'value': 'Startup 2-20'},
                                                                                {'label': 'Startup 2 - 2021', 'value': 'Startup 2-21'},
                                                                        ],
                                                                        searchable=False
                                                                ),
                                                                html.H5("Escolha o critério de comparação: "),
                                                                dcc.Dropdown(
                                                                        id='dropd3',
                                                                        options=[
                                                                                {'label': 'Geração de novos clientes', 'value': 'Geração de novos clientes'},
                                                                                {'label': 'Gastos em novos investimentos', 'value': 'Gastos em novos investimentos'},
                                                                                {'label': 'Alcance total de público', 'value': 'Alcance total de público'},
                                                                        ],
                                                                        searchable=False
                                                                ),
                                                                html.Button('Comparar', id='submit-filtro', n_clicks=0),


                                                                html.Div(
                                                                        className='resp',
                                                                        children=[
                                                                                html.H5("Gráfico - Receitas"),
                                                                                dcc.Graph(
                                                                                        id='graph-resp'
                                                                                ),
                                                                        ]
                                                                ),
                                                        ]
                                                ),
                                        ],
                                        style=tab_style, 
                                        selected_style=tab_selected_style
                                ),
                        ], 
                        style=tabs_styles
                ),
        ])

@app.callback(Output('graph-resp', 'figure'),
              Input('dropd1', 'value'),
              Input('dropd2', 'value'),
              Input('dropd3', 'value'),
              Input('submit-filtro', 'n_clicks'))
def showGraph(value1,value2,value3,n_clicks):
        fig = go.Figure()
        if((value1 == 'Startup 1-20' and value2 == 'Startup 1-21') or (value2 == 'Startup 1-20' and value1 == 'Startup 1-21')):
                df1 = pd.read_csv("data/startup1-2020.csv")
                df2 = pd.read_csv("data/startup1-2021.csv")
                if(value3 == 'Geração de novos clientes'):
                        fig = novos_clientes(fig,df1,df2)
                elif(value3 == 'Gastos em novos investimentos'):
                        fig = novos_investimentos(fig,df1,df2)
                else:
                        fig = alcance(fig,df1,df2)
        elif((value1 == 'Startup 2-20' and value2 == 'Startup 2-21') or (value2 == 'Startup 2-20' and value1 == 'Startup 2-21')):
                df1 = pd.read_csv("data/startup2-2020.csv")
                df2 = pd.read_csv("data/startup2-2021.csv")
                if(value3 == 'Geração de novos clientes'):
                        fig = novos_clientes(fig,df1,df2)
                elif(value3 == 'Gastos em novos investimentos'):
                        fig = novos_investimentos(fig,df1,df2)
                else:
                        fig = alcance(fig,df1,df2)
        elif((value1 == 'Startup 1-20' and value2 == 'Startup 2-20') or (value2 == 'Startup 1-20' and value1 == 'Startup 2-20')):
                df1 = pd.read_csv("data/startup1-2020.csv")
                df2 = pd.read_csv("data/startup2-2020.csv")
                if(value3 == 'Geração de novos clientes'):
                        fig = novos_clientes(fig,df1,df2)
                elif(value3 == 'Gastos em novos investimentos'):
                        fig = novos_investimentos(fig,df1,df2)
                else:
                        fig = alcance(fig,df1,df2)
        elif((value1 == 'Startup 1-20' and value2 == 'Startup 2-21') or (value2 == 'Startup 1-20' and value1 == 'Startup 2-21')):
                df1 = pd.read_csv("data/startup1-2020.csv")
                df2 = pd.read_csv("data/startup2-2021.csv")
                if(value3 == 'Geração de novos clientes'):
                        fig = novos_clientes(fig,df1,df2)
                elif(value3 == 'Gastos em novos investimentos'):
                        fig = novos_investimentos(fig,df1,df2)
                else:
                        fig = alcance(fig,df1,df2)
        elif((value1 == 'Startup 1-21' and value2 == 'Startup 2-20') or (value2 == 'Startup 1-21' and value1 == 'Startup 2-20')):
                df1 = pd.read_csv("data/startup1-2021.csv")
                df2 = pd.read_csv("data/startup2-2020.csv")
                if(value3 == 'Geração de novos clientes'):
                        fig = novos_clientes(fig,df1,df2)
                elif(value3 == 'Gastos em novos investimentos'):
                        fig = novos_investimentos(fig,df1,df2)
                else:
                        fig = alcance(fig,df1,df2)
        elif((value1 == 'Startup 1-21' and value2 == 'Startup 2-21') or (value2 == 'Startup 1-21' and value1 == 'Startup 2-21')):
                df1 = pd.read_csv("data/startup1-2021.csv")
                df2 = pd.read_csv("data/startup2-2021.csv")
                if(value3 == 'Geração de novos clientes'):
                        fig = novos_clientes(fig,df1,df2)
                elif(value3 == 'Gastos em novos investimentos'):
                        fig = novos_investimentos(fig,df1,df2)
                else:
                        fig = alcance(fig,df1,df2)
        else:
                print("AHHHHHH vai tomar no cu poha")
        return fig

@app.callback(Output('submit-val', 'n_clicks'),
              Input('my-input', 'value'),
              Input('drop1', 'value'),
              Input('drop2', 'value'),
              Input('drop3', 'value'),
              Input('drop4', 'value'),
              Input('drop5', 'value'),
              Input('drop6', 'value'),
              Input('drop7', 'value'),
              Input('drop8', 'value'),
              Input('drop9', 'value'),
              Input('submit-val', 'n_clicks')
              )
def insertion(inputStartup,drop1,drop2,drop3,drop4,drop5,drop6,drop7,drop8,drop9,n_clicks):
        if (n_clicks == 1):
                flag = check(inputStartup,drop1,drop2,drop3,drop4,drop5,drop6,drop7,drop8,drop9)
                if(flag == 0):
                        write(inputStartup,drop1,drop2,drop3,drop4,drop5,drop6,drop7,drop8,drop9)
                else:
                        print("Deu ruim pai")
        n_clicks = 0
        return n_clicks
        
@app.callback(Output('example-graph-1', 'figure'),
              Input('dropdown-Name', 'value'),
              Input('submit-name', 'n_clicks'))
def figGraph1(value,n_clicks):
        if(value == 'Startup 1'):
                df1 = pd.read_csv("data/startup1-2021.csv")
                labels = df1['meses'].tolist()
                values = df1['receitas'].tolist()

                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        elif(value == 'Startup 2'):
                df1 = pd.read_csv("data/startup2-2021.csv")
                labels = df1['meses'].tolist()
                values = df1['receitas'].tolist()

                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        else:
                fig = go.Figure()
        return fig

@app.callback(Output('example-graph-2', 'figure'),
              Input('dropdown-Name', 'value'),
              Input('submit-name', 'n_clicks'))
def figGraph2(value,n_clicks):
        fig = go.Figure()
        if(value == 'Startup 1'):
                df1 = pd.read_csv("data/startup1-2020.csv")
                df2 = pd.read_csv("data/startup1-2021.csv")
                columns1 = df1['meses'].tolist()
                nClientes1 = (df1["clientes_gerados"]).values.tolist()

                columns2 = df2['meses'].tolist()
                nClientes2 = (df2["clientes_gerados"]).values.tolist()
                
                fig.add_trace(go.Scatter(y=nClientes1,x=columns1,name='Clientes Gerados - ano 2020'))
                fig.add_trace(go.Scatter(y=nClientes2,x=columns2,name='Clientes Gerados - ano 2021'))

        elif(value == 'Startup 2'):
                df1 = pd.read_csv("data/startup2-2020.csv")
                df2 = pd.read_csv("data/startup2-2021.csv")
                columns1 = df1['meses'].tolist()
                nClientes1 = (df1["clientes_gerados"]).values.tolist()

                columns2 = df2['meses'].tolist()
                nClientes2 = (df2["clientes_gerados"]).values.tolist()
                
                fig.add_trace(go.Scatter(y=nClientes1,x=columns1,name='Clientes Gerados - ano 2020'))
                fig.add_trace(go.Scatter(y=nClientes2,x=columns2,name='Clientes Gerados - ano 2021'))

        return fig

@app.callback(Output('example-graph-3', 'figure'),
              Input('dropdown-Name', 'value'),
              Input('submit-name', 'n_clicks'))
def figGraph3(value,n_clicks):
        fig = go.Figure()
        if(value == 'Startup 1'):
                df1 = pd.read_csv("data/startup1-2021.csv")
                columns1 = df1['meses'].tolist()
                nClientes1 = (df1["novos_parceiros"]).values.tolist()
                
                fig.add_trace(go.Scatter(y=nClientes1,x=columns1,name='Novos Parceiros'))
        elif(value == 'Startup 2'):
                df1 = pd.read_csv("data/startup2-2021.csv")
                columns1 = df1['meses'].tolist()
                nClientes1 = (df1["novos_parceiros"]).values.tolist()
                
                fig.add_trace(go.Scatter(y=nClientes1,x=columns1,name='Novos Parceiros'))

        return fig

@app.callback(Output('example-graph-4', 'figure'),
              Input('dropdown-Name', 'value'),
              Input('submit-name', 'n_clicks'))
def figGraph4(value,n_clicks):
        fig = go.Figure()
        if(value == 'Startup 1'):
                df1 = pd.read_csv("data/startup1-2021.csv")
                columns1 = df1['meses'].tolist()
                ent3 = df1['pessoas_impactadas'].tolist()
                ent4 = (df1["pessoas_entrevistadas_total"]).values.tolist()
                zipped_lists = zip(ent3, ent4)
                soma = [int(x) + int(y) for (x, y) in zipped_lists]
                
                fig.add_trace(go.Scatter(y=soma,x=columns1,name='Alcance total'))
        elif(value == 'Startup 2'):
                df1 = pd.read_csv("data/startup2-2021.csv")
                columns1 = df1['meses'].tolist()
                ent3 = df1['pessoas_impactadas'].tolist()
                ent4 = (df1["pessoas_entrevistadas_total"]).values.tolist()
                zipped_lists = zip(ent3, ent4)
                soma = [int(x) + int(y) for (x, y) in zipped_lists]
                
                
                fig.add_trace(go.Scatter(y=soma,x=columns1,name='Alcance total'))

        return fig

if __name__ == '__main__':
    app.run_server(debug=True)