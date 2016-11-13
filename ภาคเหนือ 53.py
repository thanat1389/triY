import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('acarijang', '660yfl3eir')
data = Data([
    Pie(
        labels=['ผู้บัญญัติกฎหมาย', ' ผู้ประกอบวิชาชีพด้านต่างๆ', 'ผู้ประกอบวิชาชีพด้านเทคนิคสาขาต่างๆ', ' เสมียน', 'พนักงานบริการและพนักงานในร้านค้า', 'ผู้ปฏิบัติงานที่มีฝีมือในด้านการเกษตร', ' ผู้ปฏิบัติงานด้านความสามารถทางฝีมือ ', 'ผู้ปฏิบัติการโรงงานและเครื่องจักร ', 'อาชีพขั้นพื้นฐานต่างๆ ในด้านการขาย', 'คนงานซึ่งมิได้จำแนกไว้ในหมวดอื่น'],
        labelssrc='acarijang:17:0726c3',
        name='B',
        textinfo='label+value+percent',
        textposition='outside',
        uid='610750',
        values=['186.3', '304.4', '208.6', '227.8', '1,154.60', '3,175.10', '781.6', '308', '841.2', '                -'],
        valuessrc='acarijang:17:d12c88'
    )
])
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=1.1434563758389262,
            y=0.3720588235294118,
            showarrow=False,
            text='&nbsp;หน่วย 1:1000&nbsp;',
            xref='paper',
            yref='paper'
        )
    ]),
    autosize=True,
    hovermode='closest',
    legend=Legend(
        x=0.9941824440619621,
        y=0.8147058823529412
    ),
    title='อัตราของผู้ที่ประกอบอาชัพด้านต่างๆในภาคเหนือ ประจำปี 2553'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
