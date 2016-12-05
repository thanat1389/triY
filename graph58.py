"""analyse data"""
import pygal
from xlrd import open_workbook
def make_graph():
    """make graph in section center"""

    #open worksheet
    book = open_workbook('D:/PSIIT/job58.xlsx')
    sheet = book.sheet_by_index(0) #select sheet
    jan = [sheet.cell(col_index, 1).value for col_index in range(1, 11)]
    feb = [sheet.cell(col_index, 2).value for col_index in range(1, 11)]
    mar = [sheet.cell(col_index, 3).value for col_index in range(1, 11)]
    apr = [sheet.cell(col_index, 4).value for col_index in range(1, 11)]
    may = [sheet.cell(col_index, 5).value for col_index in range(1, 11)]
    jun = [sheet.cell(col_index, 6).value for col_index in range(1, 11)]
    july = [sheet.cell(col_index, 7).value for col_index in range(1, 11)]
    aug = [sheet.cell(col_index, 8).value for col_index in range(1, 11)]
    sep = [sheet.cell(col_index, 9).value for col_index in range(1, 11)]
    octo = [sheet.cell(col_index, 10).value for col_index in range(1, 11)]
    nov = [sheet.cell(col_index, 11).value for col_index in range(1, 11)]
    dec = [sheet.cell(col_index, 12).value for col_index in range(1, 11)]

    #make graph
    line_chart = pygal.Bar(x_label_rotation=25) #style's graph
    line_chart.title = 'ภาวะการทำงานของประชากร พ.ศ. 2558'
    line_chart.x_labels = []
    for i in [sheet.cell(col_index, 0).value for col_index in range(1,11)]:
        line_chart.x_labels.append(i)

    line_chart.x_labels = map(str, line_chart.x_labels)
    line_chart.add(sheet.cell(0,1).value, jan)
    line_chart.add(sheet.cell(0,2).value, feb)
    line_chart.add(sheet.cell(0,3).value, mar)
    line_chart.add(sheet.cell(0,4).value, apr)
    line_chart.add(sheet.cell(0,5).value, may)
    line_chart.add(sheet.cell(0,6).value, jun)
    line_chart.add(sheet.cell(0,7).value, july)
    line_chart.add(sheet.cell(0,8).value, aug)
    line_chart.add(sheet.cell(0,9).value, sep)
    line_chart.add(sheet.cell(0,10).value, octo)
    line_chart.add(sheet.cell(0,11).value, nov)
    line_chart.add(sheet.cell(0,12).value, dec)
    line_chart.render_to_file('graph58.svg')

make_graph()
