"""make graph"""
import pygal
from pygal.style import RotateStyle, DarkStyle
from xlrd import open_workbook
def make_graph():
    """make graph in section center"""

    #open worksheet
    book = open_workbook('D:/MB_Boss/KMITL/PSIT/Project/54,57.xlsx')
    sheet = book.sheet_by_index(0)
    law = [sheet.cell(1, col_index).value for col_index in range(1, 12)]
    profess = [sheet.cell(2, col_index).value for col_index in range(1, 12)]
    tech = [sheet.cell(3, col_index).value for col_index in range(1, 12)]
    clerk = [sheet.cell(4, col_index).value for col_index in range(1, 12)]
    market = [sheet.cell(5, col_index).value for col_index in range(1, 12)]
    fishing = [sheet.cell(6, col_index).value for col_index in range(1, 12)]
    business = [sheet.cell(7, col_index).value for col_index in range(1, 12)]
    fact = [sheet.cell(8, col_index).value for col_index in range(1, 12)]
    sale = [sheet.cell(9, col_index).value for col_index in range(1, 12)]
    other = [sheet.cell(10, col_index).value for col_index in range(1, 12)]


    #make graph
    neon_lighten_style = RotateStyle('#FFCCFF', base_style=DarkStyle)
    line_chart =  pygal.Bar(x_label_rotation=25, style=neon_lighten_style)
    line_chart.title = 'กราฟแสดงอัตราเฉลี่ยแต่ละอาชีพต่อปี พ.ศ.2554'
    career = []
    count_law = 0
    count_profess = 0
    count_tech = 0
    count_clerk = 0
    count_market = 0
    count_fishing = 0
    count_business = 0
    count_fact = 0
    count_sale = 0
    count_other = 0
    #แกนx
    for i in [sheet.cell(col_index, 0).value for col_index in range(1, 11)]:
        career.append(i)
    #ave per month
    for i in law:
        count_law += i
    count_law = float("%.2f" %(count_law/11))
    for i in profess:
        count_profess += i
    count_profess = float("%.2f" %(count_profess/11))
    for i in tech:
        count_tech += i
    count_tech = float("%.2f" %(count_tech/11))
    for i in clerk:
        count_clerk += i
    count_clerk = float("%.2f" %(count_clerk/11))
    for i in market:
        count_market += i
    count_market = float("%.2f" %(count_market/11))
    for i in fishing:
        count_fishing += i
    count_fishing = float("%.2f" %(count_fishing/11))
    for i in business:
        count_business += i
    count_business = float("%.2f" %(count_business/11))
    for i in fact:
        count_fact += i
    count_fact = float("%.2f" %(count_fact/11))
    for i in sale:
        count_sale += i
    count_sale = float("%.2f" %(count_sale/11))
    for i in other:
        count_other += i
    count_other = float("%.2f" %(count_other/11))

    
    line_chart.x_labels = map(str, career)
    line_chart.add('Average/year', [count_law, count_profess, count_tech, count_clerk, count_market,\
                           count_fishing, count_business, count_fact, count_sale, count_other])
    line_chart.render_to_file('ave 54.svg')

make_graph()
