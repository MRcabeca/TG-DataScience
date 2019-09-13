import plotly.offline as py
import plotly.graph_objects as go
from src.core.importacao.tratamentoDados import lerExcel,Teste

dataset = lerExcel()

def gerarGraficoLinhas():
    x=dataset.Date
    y=dataset.Close

    fig = go.Figure()
    fig.add_trace(go.Scatter(
            x=x, 
            y=y,
            mode='lines',
            name='Ações',
            line=dict(
                color='firebrick',
                width=3
            )
        )
    )

    fig.update_layout(
        xaxis_title="Data",
        yaxis_title="Valor das Ações",
        showlegend=True
    )

    fig.show()

def gerarGraficoVariacao():
    x = dataset['Date']
    y = dataset['Variation']

    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=x,
            y=y,
            marker=dict(
                color="crimson", 
                size=8
            ),
            mode="markers",
            name="Ações",
        )
    )

    fig.update_layout(
        xaxis_title="Data",
        yaxis_title="Variação",
        showlegend=True
    )

    fig.show()

def gerarGraficoRegressao():
    x2= Teste()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
            x=dataset.Date,
            y=dataset.Close,
            mode='lines+markers',
            name='Ações',
            line=dict(
                color='green',
                width=3
            )
        )
    )

    fig.add_trace(go.Scatter(
            x=x2.Date,
            y=x2.Close,
            marker=dict(
                color="firebrick", 
                size=8
            ),
            mode="markers",
            name="Previsões",
        )
    )

    fig.update_layout(
        xaxis_title="Data",
        yaxis_title="Valor das Ações",
        showlegend=True
    )

    fig.show()