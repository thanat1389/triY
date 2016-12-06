"""make graph"""
import pygal
from xlrd import open_workbook
def make_graph():
    """make graph in section center"""

    #open worksheet2553
    book = open_workbook('D:/MB_Boss/KMITL/PSIT/Project/53,56.xlsx')
    sheet53 = book.sheet_by_index(0)
    law53 = [sheet53.cell(1, col_index).value for col_index in range(1, 13)]
    profess53 = [sheet53.cell(2, col_index).value for col_index in range(1, 13)]
    tech53 = [sheet53.cell(3, col_index).value for col_index in range(1, 13)]
    clerk53 = [sheet53.cell(4, col_index).value for col_index in range(1, 13)]
    market53 = [sheet53.cell(5, col_index).value for col_index in range(1, 13)]
    fishing53 = [sheet53.cell(6, col_index).value for col_index in range(1, 13)]
    business53 = [sheet53.cell(7, col_index).value for col_index in range(1, 13)]
    fact53 = [sheet53.cell(8, col_index).value for col_index in range(1, 13)]
    sale53 = [sheet53.cell(9, col_index).value for col_index in range(1, 13)]
    other53 = [sheet53.cell(10, col_index).value for col_index in range(1, 13)]

    #open worksheet2554
    book = open_workbook('D:/MB_Boss/KMITL/PSIT/Project/54,57.xlsx')
    sheet54 = book.sheet_by_index(0)
    law54 = [sheet54.cell(1, col_index).value for col_index in range(1, 12)]
    profess54 = [sheet54.cell(2, col_index).value for col_index in range(1, 12)]
    tech54 = [sheet54.cell(3, col_index).value for col_index in range(1, 12)]
    clerk54 = [sheet54.cell(4, col_index).value for col_index in range(1, 12)]
    market54 = [sheet54.cell(5, col_index).value for col_index in range(1, 12)]
    fishing54 = [sheet54.cell(6, col_index).value for col_index in range(1, 12)]
    business54 = [sheet54.cell(7, col_index).value for col_index in range(1, 12)]
    fact54 = [sheet54.cell(8, col_index).value for col_index in range(1, 12)]
    sale54 = [sheet54.cell(9, col_index).value for col_index in range(1, 12)]
    other54 = [sheet54.cell(10, col_index).value for col_index in range(1, 12)]

    #open worksheet2555
    book = open_workbook('D:/MB_Boss/KMITL/PSIT/Project/job55_2.xlsx')
    sheet55 = book.sheet_by_index(0)
    law55 = [sheet55.cell(1, col_index).value for col_index in range(1, 13)]
    profess55 = [sheet55.cell(2, col_index).value for col_index in range(1, 13)]
    tech55 = [sheet55.cell(3, col_index).value for col_index in range(1, 13)]
    clerk55 = [sheet55.cell(4, col_index).value for col_index in range(1, 13)]
    market55 = [sheet55.cell(5, col_index).value for col_index in range(1, 13)]
    fishing55 = [sheet55.cell(6, col_index).value for col_index in range(1, 13)]
    business55 = [sheet55.cell(7, col_index).value for col_index in range(1, 13)]
    fact55 = [sheet55.cell(8, col_index).value for col_index in range(1, 13)]
    sale55 = [sheet55.cell(9, col_index).value for col_index in range(1, 13)]
    other55 = [sheet55.cell(10, col_index).value for col_index in range(1, 13)]

    #open worksheet2556
    book = open_workbook('D:/MB_Boss/KMITL/PSIT/Project/53,56.xlsx')
    sheet56 = book.sheet_by_index(1)
    law56 = [sheet56.cell(1, col_index).value for col_index in range(1, 13)]
    profess56 = [sheet56.cell(2, col_index).value for col_index in range(1, 13)]
    tech56 = [sheet56.cell(3, col_index).value for col_index in range(1, 13)]
    clerk56 = [sheet56.cell(4, col_index).value for col_index in range(1, 13)]
    market56 = [sheet56.cell(5, col_index).value for col_index in range(1, 13)]
    fishing56 = [sheet56.cell(6, col_index).value for col_index in range(1, 13)]
    business56 = [sheet56.cell(7, col_index).value for col_index in range(1, 13)]
    fact56 = [sheet56.cell(8, col_index).value for col_index in range(1, 13)]
    sale56 = [sheet56.cell(9, col_index).value for col_index in range(1, 13)]
    other56 = [sheet56.cell(10, col_index).value for col_index in range(1, 13)]

    #open worksheet2557
    book57 = open_workbook('D:/MB_Boss/KMITL/PSIT/Project/54,57.xlsx')
    sheet57 = book57.sheet_by_index(1)
    law57 = [sheet57.cell(1, col_index).value for col_index in range(1, 13)]
    profess57 = [sheet57.cell(2, col_index).value for col_index in range(1, 13)]
    tech57 = [sheet57.cell(3, col_index).value for col_index in range(1, 13)]
    clerk57 = [sheet57.cell(4, col_index).value for col_index in range(1, 13)]
    market57 = [sheet57.cell(5, col_index).value for col_index in range(1, 13)]
    fishing57 = [sheet57.cell(6, col_index).value for col_index in range(1, 13)]
    business57 = [sheet57.cell(7, col_index).value for col_index in range(1, 13)]
    fact57 = [sheet57.cell(8, col_index).value for col_index in range(1, 13)]
    sale57 = [sheet57.cell(9, col_index).value for col_index in range(1, 13)]
    other57 = [sheet57.cell(10, col_index).value for col_index in range(1, 13)]

    #open worksheet2558
    book = open_workbook('D:/MB_Boss/KMITL/PSIT/Project/job58.xlsx')
    sheet = book.sheet_by_index(0) #select sheet
    law = [sheet.cell(1, col_index).value for col_index in range(1, 13)]
    profess = [sheet.cell(2, col_index).value for col_index in range(1, 13)]
    tech = [sheet.cell(3, col_index).value for col_index in range(1, 13)]
    clerk = [sheet.cell(4, col_index).value for col_index in range(1, 13)]
    market = [sheet.cell(5, col_index).value for col_index in range(1, 13)]
    fishing = [sheet.cell(6, col_index).value for col_index in range(1, 13)]
    business = [sheet.cell(7, col_index).value for col_index in range(1, 13)]
    fact = [sheet.cell(8, col_index).value for col_index in range(1, 13)]
    sale = [sheet.cell(9, col_index).value for col_index in range(1, 13)]
    other = [sheet.cell(10, col_index).value for col_index in range(1, 13)]


    #----------------------------------------------------------------------------#


    #make graph
    line_chart =  pygal.Bar(x_label_rotation=25)
    line_chart.title = 'กราฟแสดงอัตราเฉลี่ยแต่ละอาชีพต่อปี พ.ศ.2553-2558'
    career = []
    #แกนx
    for i in [sheet54.cell(col_index, 0).value for col_index in range(1, 11)]:
        career.append(i)

    #2553
    count_law53 = 0
    count_profess53 = 0
    count_tech53 = 0
    count_clerk53 = 0
    count_market53 = 0
    count_fishing53 = 0
    count_business53 = 0
    count_fact53 = 0
    count_sale53 = 0
    count_other53 = 0
    for i in law53:
        count_law53 += i
    count_law53 = float("%.2f" %(count_law53/12))
    for i in profess53:
        count_profess53 += i
    count_profess53 = float("%.2f" %(count_profess53/12))
    for i in tech53:
        count_tech53 += i
    count_tech53 = float("%.2f" %(count_tech53/12))
    for i in clerk53:
        count_clerk53 += i
    count_clerk53 = float("%.2f" %(count_clerk53/12))
    for i in market53:
        count_market53 += i
    count_market53 = float("%.2f" %(count_market53/12))
    for i in fishing53:
        count_fishing53 += i
    count_fishing53 = float("%.2f" %(count_fishing53/12))
    for i in business53:
        count_business53 += i
    count_business53 = float("%.2f" %(count_business53/12))
    for i in fact53:
        count_fact53 += i
    count_fact53 = float("%.2f" %(count_fact53/12))
    for i in sale53:
        count_sale53 += i
    count_sale53 = float("%.2f" %(count_sale53/12))
    for i in other53:
        count_other53 += i
    count_other53 = float("%.2f" %(count_other53/12))


    #2554
    count_law54 = 0
    count_profess54 = 0
    count_tech54 = 0
    count_clerk54 = 0
    count_market54 = 0
    count_fishing54 = 0
    count_business54 = 0
    count_fact54 = 0
    count_sale54 = 0
    count_other54 = 0
    for i in law54:
        count_law54 += i
    count_law54 = float("%.2f" %(count_law54/11))
    for i in profess54:
        count_profess54 += i
    count_profess54 = float("%.2f" %(count_profess54/11))
    for i in tech54:
        count_tech54 += i
    count_tech54 = float("%.2f" %(count_tech54/11))
    for i in clerk54:
        count_clerk54 += i
    count_clerk54 = float("%.2f" %(count_clerk54/11))
    for i in market54:
        count_market54 += i
    count_market54 = float("%.2f" %(count_market54/11))
    for i in fishing54:
        count_fishing54 += i
    count_fishing54 = float("%.2f" %(count_fishing54/11))
    for i in business54:
        count_business54 += i
    count_business54 = float("%.2f" %(count_business54/11))
    for i in fact54:
        count_fact54 += i
    count_fact54 = float("%.2f" %(count_fact54/11))
    for i in sale54:
        count_sale54 += i
    count_sale54 = float("%.2f" %(count_sale54/11))
    for i in other54:
        count_other54 += i
    count_other54 = float("%.2f" %(count_other54/11))


    #2555
    count_law55 = 0
    count_profess55 = 0
    count_tech55 = 0
    count_clerk55 = 0
    count_market55 = 0
    count_fishing55 = 0
    count_business55 = 0
    count_fact55 = 0
    count_sale55 = 0
    count_other55 = 0
    for i in law55:
        count_law55 += i
    count_law55 = float("%.2f" %(count_law55/12))
    for i in profess55:
        count_profess55 += i
    count_profess55 = float("%.2f" %(count_profess55/12))
    for i in tech55:
        count_tech55 += i
    count_tech55 = float("%.2f" %(count_tech55/12))
    for i in clerk55:
        count_clerk55 += i
    count_clerk55 = float("%.2f" %(count_clerk55/12))
    for i in market55:
        count_market55 += i
    count_market55 = float("%.2f" %(count_market55/12))
    for i in fishing55:
        count_fishing55 += i
    count_fishing55 = float("%.2f" %(count_fishing55/12))
    for i in business55:
        count_business55 += i
    count_business55 = float("%.2f" %(count_business55/12))
    for i in fact55:
        count_fact55 += i
    count_fact55 = float("%.2f" %(count_fact55/12))
    for i in sale55:
        count_sale55 += i
    count_sale55 = float("%.2f" %(count_sale55/12))
    for i in other55:
        count_other55 += i
    count_other55 = float("%.2f" %(count_other55/12))


    #2556
    count_law56 = 0
    count_profess56 = 0
    count_tech56 = 0
    count_clerk56 = 0
    count_market56 = 0
    count_fishing56 = 0
    count_business56 = 0
    count_fact56 = 0
    count_sale56 = 0
    count_other56 = 0
    for i in law56:
        count_law56 += i
    count_law56 = float("%.2f" %(count_law56/12))
    for i in profess56:
        count_profess56 += i
    count_profess56 = float("%.2f" %(count_profess56/12))
    for i in tech56:
        count_tech56 += i
    count_tech56 = float("%.2f" %(count_tech56/12))
    for i in clerk56:
        count_clerk56 += i
    count_clerk56 = float("%.2f" %(count_clerk56/12))
    for i in market56:
        count_market56 += i
    count_market56 = float("%.2f" %(count_market56/12))
    for i in fishing56:
        count_fishing56 += i
    count_fishing56 = float("%.2f" %(count_fishing56/12))
    for i in business56:
        count_business56 += i
    count_business56 = float("%.2f" %(count_business56/12))
    for i in fact56:
        count_fact56 += i
    count_fact56 = float("%.2f" %(count_fact56/12))
    for i in sale56:
        count_sale56 += i
    count_sale56 = float("%.2f" %(count_sale56/12))
    for i in other56:
        count_other56 += i
    count_other56 = float("%.2f" %(count_other56/12))


    #2557
    count_law57 = 0
    count_profess57 = 0
    count_tech57 = 0
    count_clerk57 = 0
    count_market57 = 0
    count_fishing57 = 0
    count_business57 = 0
    count_fact57 = 0
    count_sale57 = 0
    count_other57 = 0
    for i in law57:
        count_law57 += i
    count_law57 = float("%.2f" %(count_law57/12))
    for i in profess57:
        count_profess57 += i
    count_profess57 = float("%.2f" %(count_profess57/12))
    for i in tech57:
        count_tech57 += i
    count_tech57 = float("%.2f" %(count_tech57/12))
    for i in clerk57:
        count_clerk57 += i
    count_clerk57 = float("%.2f" %(count_clerk57/12))
    for i in market57:
        count_market57 += i
    count_market57 = float("%.2f" %(count_market57/12))
    for i in fishing57:
        count_fishing57 += i
    count_fishing57 = float("%.2f" %(count_fishing57/12))
    for i in business57:
        count_business57 += i
    count_business57 = float("%.2f" %(count_business57/12))
    for i in fact57:
        count_fact57 += i
    count_fact57 = float("%.2f" %(count_fact57/12))
    for i in sale57:
        count_sale57 += i
    count_sale57 = float("%.2f" %(count_sale57/12))
    for i in other57:
        count_other57 += i
    count_other57 = float("%.2f" %(count_other57/12))


    #2558
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
    for i in law:
        count_law += i
    count_law = float("%.2f" %(count_law/12))
    for i in profess:
        count_profess += i
    count_profess = float("%.2f" %(count_profess/12))
    for i in tech:
        count_tech += i
    count_tech = float("%.2f" %(count_tech/12))
    for i in clerk:
        count_clerk += i
    count_clerk = float("%.2f" %(count_clerk/12))
    for i in market:
        count_market += i
    count_market = float("%.2f" %(count_market/12))
    for i in fishing:
        count_fishing += i
    count_fishing = float("%.2f" %(count_fishing/12))
    for i in business:
        count_business += i
    count_business = float("%.2f" %(count_business/12))
    for i in fact:
        count_fact += i
    count_fact = float("%.2f" %(count_fact/12))
    for i in sale:
        count_sale += i
    count_sale = float("%.2f" %(count_sale/12))
    for i in other:
        count_other += i
    count_other = float("%.2f" %(count_other/12))

    
    line_chart.x_labels = map(str, career)
    line_chart.add('2553', [count_law53, count_profess53, count_tech53, count_clerk53, count_market53,\
                           count_fishing53, count_business53, count_fact53, count_sale53, count_other53])
    line_chart.add('2554', [count_law54, count_profess54, count_tech54, count_clerk54, count_market54,\
                           count_fishing54, count_business54, count_fact54, count_sale54, count_other54])
    line_chart.add('2555', [count_law55, count_profess55, count_tech55, count_clerk55, count_market55,\
                           count_fishing55, count_business55, count_fact55, count_sale55, count_other55])
    line_chart.add('2556', [count_law56, count_profess56, count_tech56, count_clerk56, count_market56,\
                           count_fishing56, count_business56, count_fact56, count_sale56, count_other56])
    line_chart.add('2557', [count_law57, count_profess57, count_tech57, count_clerk57, count_market57,\
                           count_fishing57, count_business57, count_fact57, count_sale57, count_other57])
    line_chart.add('2558', [count_law, count_profess, count_tech, count_clerk, count_market,\
                           count_fishing, count_business, count_fact, count_sale, count_other])
    line_chart.render_to_file('ave_all.svg')

make_graph()
