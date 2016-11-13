import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('acarijang', '660yfl3eir')
data = Data([
    Pie(
        labels=['ผู้บัญญัติกฎหมาย', ' ผู้ประกอบวิชาชีพด้านต่างๆ', 'ผู้ประกอบวิชาชีพด้านเทคนิคสาขาต่างๆ', ' เสมียน', 'พนักงานบริการและพนักงานในร้านค้า', 'ผู้ปฏิบัติงานที่มีฝีมือในด้านการเกษตร', ' ผู้ปฏิบัติงานด้านความสามารถทางฝีมือ ', 'ผู้ปฏิบัติการโรงงานและเครื่องจักร ', 'อาชีพขั้นพื้นฐานต่างๆ ในด้านการขาย', 'คนงานซึ่งมิได้จำแนกไว้ในหมวดอื่น'],
        labelssrc='acarijang:19:7af87e',
        marker=Marker(
            colors=['rgb(255,255,204)', 'rgb(161,218,180)', 'rgb(65,182,196)', 'rgb(44,127,184)', 'rgb(8,104,172)', 'rgb(37,52,148)'],
            colorssrc='acarijang:21:a09dff'
        ),
        name='B',
        textinfo='label+value+percent',
        textposition='outside',
        uid='e1f776',
        values=['362.5', '489.5', '247.7', '337.7', '1,661.70', '7,135.00', '1,218.90', '533.2', '970.6', '                -  '],
        valuessrc='acarijang:19:fe36b4'
    )
])
layout = Layout(
    autosize=True,
    hovermode='closest',
    title='อัตราของผู้ที่ประกอบอาชัพด้านต่างๆในภาคอีสาน ประจำปี 2553'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)