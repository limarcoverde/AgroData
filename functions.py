import dash
import csv
import dash_auth
import pandas as pd
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


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

def check(inputStartup,drop1,drop2,drop3,drop4,drop5):
        flag = 0
        if(inputStartup == ''):
                flag = 1
        if(drop1 is None):
                flag = 1
        if(drop2 is None):
                flag = 1
        if(drop3 is None):
                flag = 1
        if(drop4 is None):
                flag = 1
        if(drop5 is None):
                flag = 1
                
        return flag

def write(inputStartup,ecmo,ccp,et,ep,es):
        df = pd.read_csv("data/db.csv")
        listaRespostas = [ecmo, ccp, et, ep, es]
        for x in range (len(listaRespostas)):
                if listaRespostas[x] == 'False':
                        listaRespostas[x] = False
                else:
                        listaRespostas[x] = True

        data = {'Startups': [inputStartup],
          'Entender_como_mercado_opera': [listaRespostas[0]],
          'Consegue_construir_produto': [listaRespostas[1]],
          'Explicar_transformacao': [listaRespostas[2]],
          'Experenciou_problema': [listaRespostas[3]],
          'Evidencia_de_Solucao': [listaRespostas[4]]
        }

        df2 = pd.DataFrame(data)

        df = df.append(df2, ignore_index = True)
        
        df.to_csv("data/db.csv",index=False)
