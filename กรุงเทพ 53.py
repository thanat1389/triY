import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('acarijang', '660yfl3eir')
data = Data([
    Pie(
        direction='counterclockwise',
        hoverinfo='label+value+text+percent',
        labels=['ผู้บัญญัติกฎหมาย', ' ผู้ประกอบวิชาชีพด้านต่างๆ', 'ผู้ประกอบวิชาชีพด้านเทคนิคสาขาต่างๆ', ' เสมียน', 'พนักงานบริการและพนักงานในร้านค้า', 'ผู้ปฏิบัติงานที่มีฝีมือในด้านการเกษตร', ' ผู้ปฏิบัติงานด้านความสามารถทางฝีมือ ', 'ผู้ปฏิบัติการโรงงานและเครื่องจักร ', 'อาชีพขั้นพื้นฐานต่างๆ ในด้านการขาย', 'คนงานซึ่งมิได้จำแนกไว้ในหมวดอื่น'],
        labelssrc='acarijang:8:5d1d12',
        marker=Marker(
            colors=['rgb(5,10,172)', 'rgb(106,137,247)', 'rgb(190,190,190)', 'rgb(220,170,132)', 'rgb(230,145,90)', 'rgb(178,10,28)'],
            colorssrc='acarijang:10:f33b64',
            line=Line(
                color='rgb(68, 68, 68)'
            )
        ),
        name='B',
        opacity=1,
        sort=True,
        textfont=dict(
            size=13
        ),
        textinfo='label+value+percent',
        textposition='outside',
        uid='7c3199',
        values=['260.24', '286.32', '418.24', '312.09', '1055.22', '23.1', '535.83', '484.05', '462.26', '9.58'],
        valuessrc='acarijang:8:263b45'
    )
])
layout = Layout(
    autosize=True,
    boxmode='group',
    dragmode='pan',
    hidesources=False,
    hovermode=False,
    legend=Legend(
        x=1.1407194003303565,
        y=1.1058823529411765
    ),
    paper_bgcolor='rgb(255, 255, 255)',
    plot_bgcolor='rgba(255, 127, 14, 0.18)',
    scene=Scene(
        aspectratio=dict(
            x=1,
            y=1,
            z=1
        )
    ),
    title='อัตราของผู้ที่ประกอบอาชีพด้านต่างๆในกรุงเทะมหานครประจำปี 2553'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
