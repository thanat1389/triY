"""make graph"""
import pygal                                                       # First import pygal
from xlrd import open_workbook
def make_graph():
    """make graph in section center"""

    #open worksheet
    book = open_workbook('D:/MB_Boss/KMITL/PSIT/Project/54,57.xlsx')
    sheet = book.sheet_by_index(0) #code select sheet
    law = [sheet.cell(col_index, 1).value for col_index in range(1, 11)]
    profes = [sheet.cell(col_index, 2).value for col_index in range(1, 11)]
    tech = [sheet.cell(col_index, 3).value for col_index in range(1, 11)]
    clerk = [sheet.cell(col_index, 4).value for col_index in range(1, 11)]
    market = [sheet.cell(col_index, 5).value for col_index in range(1, 11)]
    fishing = [sheet.cell(col_index, 6).value for col_index in range(1, 11)]
    business = [sheet.cell(col_index, 7).value for col_index in range(1, 11)]
    factory = [sheet.cell(col_index, 8).value for col_index in range(1, 11)]
    sale = [sheet.cell(col_index, 9).value for col_index in range(1, 11)]
    other = [sheet.cell(col_index, 10).value for col_index in range(1, 11)]
    sep = [sheet.cell(col_index, 11).value for col_index in range(1, 11)]


    #make graph
    line_chart =  pygal.Bar() #รูปแบบของ graph
    line_chart.title = sheet.cell(0, 0).value
    career = []
    for i in [sheet.cell(col_index, 0).value for col_index in range(1, 11)]:
        career.append(i)

    line_chart.x_labels = map(str, career)
    line_chart.add(sheet.cell(0, 1).value, law)
    line_chart.add(sheet.cell(0, 2).value, profes)
    line_chart.add(sheet.cell(0, 3).value, tech)
    line_chart.add(sheet.cell(0, 4).value, clerk)
    line_chart.add(sheet.cell(0, 5).value, market)
    line_chart.add(sheet.cell(0, 6).value, fishing)
    line_chart.add(sheet.cell(0, 7).value, business)
    line_chart.add(sheet.cell(0, 8).value, factory)
    line_chart.add(sheet.cell(0, 9).value, sale)
    line_chart.add(sheet.cell(0, 10).value, other)
    line_chart.add(sheet.cell(0, 11).value, sep)
    line_chart.render_to_file('54.svg')
make_graph()
