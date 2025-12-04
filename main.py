import plotly.graph_objects as go
from data.cleanedData import cityPopulationDict

'''
To-do: need a way to actually draw the lines, maybe using pygame for that - I think that pygame has more control over the figures I create and could be a better library
for animation in general. I think that plotly works great for quick data representation, but I don't think I will have the needed animations with it. I could use it to 
quickly get the plots I need then use pygame to implement the acutal animation behind forming the interstates

- get the actual lines to generate in an animation
- figure out how to actually use plotly
'''

fig = go.Figure(go.Scattermap(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
        marker=go.scattermap.Marker(
            size=14
        ),
        text=['Montreal'],
    ))

fig.update_layout(
    hovermode='closest',
    map=dict(
        bearing=0,
        center=go.layout.map.Center(
            lat=45,
            lon=-73
        ),
        pitch=0,
        zoom=5
    )
)

fig.show()