import psycopg2
import plotly.graph_objects as go
import plotly
import plotly.express as px
import config

def fetch_plot_data(UserID, FromDate, ToDate):
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="FebiacWoluwe2019",
        host="dev-smepostgres.cpesf20fxopt.eu-central-1.rds.amazonaws.com",
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(config.read_data)
    rows = cur.fetchall()
    startLat = []
    startLon = []
    endLat = []
    endLon = []
    startLoc = []
    endLoc = []

    for row in rows:
        startLat.append(row[1])
        startLon.append(row[2])
        endLat.append(row[3])
        endLon.append(row[4])
        startLoc.append(row[5])
        endLoc.append(row[6])

    fig = go.Figure()
    px.set_mapbox_access_token(config.mapbox_token)

    for i in range(len(endLon)):
        fig.add_trace(go.Scattermapbox(
            mode="markers+lines",
            lon=[startLon[i], endLon[i]],
            lat=[startLat[i], endLat[i]],
            showlegend=False,
            marker={'size': 10},
            text=[startLoc[i], endLoc[i]]))

    fig.update_layout(
        mapbox_style="dark", mapbox_accesstoken=config.mapbox_token)

    fig.update_layout(
        mapbox={
            'center': {'lon': 4.4834, 'lat': 50.7528},
            'style': "carto-darkmatter",
            'zoom': 8})

    return fig