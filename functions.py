import dash
import csv
import dash_auth
import pandas as pd
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
from flask import request

def createHeader():
        return html.Div(
                className="header",
                children=[
                        #html.P(children="🌵", className="header-emoji"),
                        html.H1(
                                className="header-title",
                                children="📈AgroData", 
                        ),
                        html.P(
                                className="header-description",
                                children="Uma plataforma para mudar tudo já visto em análise de dados",
                        ),
                ],
        )        

def CreateMenu(children,className="menu-body"):
        return html.Div(
                className=className,
                children=children
        )
        
def tabStyles ():
        tabs_styles = {
                'height': '44px'
        }
        tab_style = {
                'borderBottom': '1px solid #d6d6d6',
                'padding': '6px',
                'fontWeight': 'bold'
        }
        tab_selected_style = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#119DFF',
        'color': 'white',
        'padding': '6px'
        }

        return tabs_styles,tab_style,tab_selected_style

def check_month(inputStartup,mes):
        if(inputStartup == 'Startup 1'):
                df = pd.read_csv("data/startup1-2021.csv")
                meses = df["meses"].tolist()
                if(mes in meses):
                        return True
                return False
        elif(inputStartup == 'Startup 2'):
                df = pd.read_csv("data/startup2-2021.csv")
                meses = df["meses"].tolist()
                if(mes in meses):
                        return True
                return False
        
        return True
        
def check(inputStartup,mes,drop2,drop3,drop4,drop5,drop6,drop7,drop8,drop9):
        flag = 0
        if(inputStartup == None):
                flag = 1
        if(mes is None or check_month(inputStartup,mes)):
                flag = 1
        if(drop2 == ''):
                flag = 1
        if(drop3 == ''):
                flag = 1
        if(drop4 == ''):
                flag = 1
        if(drop5 == ''):
                flag = 1
        if(drop6 == ''):
                flag = 1
        if(drop7 == ''):
                flag = 1
        if(drop8 == ''):
                flag = 1
        if(drop9 == ''):
                flag = 1
                
        return flag

def write(inputStartup,mes,drop2,drop3,drop4,drop5,drop6,drop7,drop8,drop9):
        if(inputStartup == 'Startup 1'):
                df = pd.read_csv("data/startup1-2021.csv")
        elif(inputStartup == 'Startup 2'):
                df = pd.read_csv("data/startup2-2021.csv")
        data = {
                'meses': [mes],
                'pessoas_entrevistadas_total': [drop2],
                'clientes_gerados': [drop3],
                'pessoas_impactadas': [drop4],
                'novos_parceiros': [drop5],
                'receitas': [drop6],
                'dinheiro_investido': [drop7],
                'numero_de_integrantes': [drop8],
                'integrantes_novos_do_mes': [drop9],
        }

        df2 = pd.DataFrame(data)

        df = df.append(df2, ignore_index = True)
        if(inputStartup == 'Startup 1'):
                df.to_csv("data/startup1-2021.csv",index=False)
        elif(inputStartup == 'Startup 2'):
                df.to_csv("data/startup2-2021.csv",index=False)

def pegaReceita(df,x):
        return df.iloc[x]['receita']

def novos_clientes(fig,df1,df2):
        columns1 = df1['meses'].tolist()
        nClientes1 = (df1["clientes_gerados"]).values.tolist()

        columns2 = df2['meses'].tolist()
        nClientes2 = (df2["clientes_gerados"]).values.tolist()
        
        fig.add_trace(go.Scatter(y=nClientes1,x=columns1,name='Clientes Gerados - ano 2020'))
        fig.add_trace(go.Scatter(y=nClientes2,x=columns2,name='Clientes Gerados - ano 2021'))

        return fig

def novos_investimentos(fig,df1,df2):
        columns1 = df1['meses'].tolist()
        nClientes1 = (df1["dinheiro_investido"]).values.tolist()

        columns2 = df2['meses'].tolist()
        nClientes2 = (df2["dinheiro_investido"]).values.tolist()
        
        fig.add_trace(go.Scatter(y=nClientes1,x=columns1,name='Gastos em novos investimentos - ano 2020'))
        fig.add_trace(go.Scatter(y=nClientes2,x=columns2,name='Gastos em novos investimentos - ano 2021'))
        return fig

def alcance(fig,df1,df2):
        columns1 = df1['meses'].tolist()
        ent3 = df1['pessoas_impactadas'].tolist()
        ent4 = (df1["pessoas_entrevistadas_total"]).values.tolist()
        zipped_lists = zip(ent3, ent4)
        soma = [int(x) + int(y) for (x, y) in zipped_lists]
        
        fig.add_trace(go.Scatter(y=soma,x=columns1,name='Alcance total'))

        columns1 = df2['meses'].tolist()
        ent3 = df2['pessoas_impactadas'].tolist()
        ent4 = (df2["pessoas_entrevistadas_total"]).values.tolist()
        zipped_lists = zip(ent3, ent4)
        soma = [int(x) + int(y) for (x, y) in zipped_lists]
        
        fig.add_trace(go.Scatter(y=soma,x=columns1,name='Alcance total'))
        return fig