# Define functions to return your charts in this file. You could also read in the data here.
import plotly.express as px
import data

def get_map(pref_lang=None):
    df = data.getPoints(pref_lang)
    df['size'] = 5
    fig1 = px.scatter_mapbox(df,
                             lat='latitude',
                             lon='longitude',
                             hover_name='name', 
                             hover_data={'latitude':False, 'longitude':False, 'name':False, 'desc':False, 'uri': False, 'size': False},
                             labels={
                                 'name': 'Attraction name',
                                 },
                             size='size',
                             zoom=14,
                             height=750,
                             mapbox_style='open-street-map',
                             )
    fig1.update_layout(clickmode='event', margin=dict(l=0, r=0, t=0, b=0))
    return fig1