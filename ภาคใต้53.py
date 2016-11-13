import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('acarijang', '660yfl3eir')
data = Data([
    Pie(
        labels=['ผู้บัญญัติกฎหมาย', ' ผู้ประกอบวิชาชีพด้านต่างๆ', 'ผู้ประกอบวิชาชีพด้านเทคนิคสาขาต่างๆ', ' เสมียน', 'พนักงานบริการและพนักงานในร้านค้า', 'ผู้ปฏิบัติงานที่มีฝีมือในด้านการเกษตร', ' ผู้ปฏิบัติงานด้านความสามารถทางฝีมือ ', 'ผู้ปฏิบัติการโรงงานและเครื่องจักร ', 'อาชีพขั้นพื้นฐานต่างๆ ในด้านการขาย', 'คนงานซึ่งมิได้จำแนกไว้ในหมวดอื่น'],
        labelssrc='acarijang:14:558718',
        marker=Marker(
            colors=['rgb(209,190,90)', 'rgb(177,173,42)', 'rgb(95,144,11)', 'rgb(57,129,27)', 'rgb(40,122,33)', 'rgb(13,86,44)'],
            colorssrc='acarijang:16:a212ef'
        ),
        name='B',
        textinfo='label+value+percent',
        textposition='outside',
        uid='b4736a',
        values=['145.9', '215.8', '155.4', '174', '1,035.00', '2,413.50', '485.7', '232.1', '492.8', '                -   ', ''],
        valuessrc='acarijang:14:a8bd45'
    )
])
layout = Layout(
    autosize=True,
    hovermode='closest',
    legend=Legend(
        x=1.02,
        y=0.8441176470588235
    ),
    title='อัตราของผู้ที่ประกอบอาชัพด้านต่างๆในภาคใต้ ประจำปี 2553'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
