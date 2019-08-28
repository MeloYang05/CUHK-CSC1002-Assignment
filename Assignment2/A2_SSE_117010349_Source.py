from bokeh.io import output_file, show
from bokeh.layouts import row, column, layout
from bokeh.plotting import figure, curdoc
from bokeh.layouts import widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, TextInput
from bokeh.models.widgets import RadioGroup, CheckboxGroup, MultiSelect, Dropdown
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn, Panel, Tabs
from bokeh.models.widgets import Paragraph
from bokeh.events import ButtonClick
from datetime import date
from random import randint
import string
import pyodbc
import functools
from functools import partial
from bokeh.core.properties import value, Instance

obdcConnection = None

def connectSQLServer():
    global obdcConnection
    attr = dict(
        server = '10.20.213.10',
        database = 'csc1002',
        username = 'csc1002',
        password = 'csc1002',
        port = 1433,
        driver = 'ODBC Driver 13 for SQL Server'
    )

    conn_str = 'DRIVER={driver};' \
        'SERVER={server};' \
        'PORT={port};' \
        'DATABASE={database};' \
        'UID={username};' \
        'PWD={password}'

    conn_str = conn_str.format(**attr)

    try:
        return pyodbc.connect(conn_str)
    except Exception as e:
        print(e)
        quit()
obdcConnection = connectSQLServer()
tsql = "SELECT * FROM lgu.course;"
cursor = obdcConnection.cursor()
with obdcConnection:
    rows = cursor.execute(tsql).fetchall()
    id_list=list()
    title_list=list()
    dept_name_list=list()
    credit_list=list()
    instructor_list=list()
    for row in rows:
        id_list.append(row.course_id)
        title_list.append(row.title)
        dept_name_list.append(row.dept_name)
        credit_list.append(row.credits)
        instructor_list.append(row.instructor)

data=dict(
        id=id_list,
        title=title_list,
        dept=dept_name_list,
        credit=credit_list,
        instructor=instructor_list
        )
new_dept_list=list()
for i in dept_name_list:
    if not i in new_dept_list:
        new_dept_list.append(i)

refresh = Button(label="Refresh")
btnGroupTitle = RadioButtonGroup(name='title', labels=["begins with...", "...contains...", "...ends with"], active=1)
btnGroupDept = RadioButtonGroup(name='dept', labels=["begins with...", "...contains...", "...ends with"], active=1)
paragraph = Paragraph(text="option")
optionGroup = RadioGroup(labels=["and", "or"], active=0, width=100, inline=True)
btnGroupLetters = RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
title_input = TextInput(value="", title="Title:", placeholder="contains....")
dept_input = TextInput(value="", title="Department:", placeholder="contains....")
dept_select = Select(title='Department',value='',options=new_dept_list)

columns = [
    TableColumn(field='id',title='Course ID'),
    TableColumn(field='title',title='Title'),
    TableColumn(field='dept',title='Department'),
    TableColumn(field='credit',title='Credit'),
    TableColumn(field='instructor',title='Instructor')
]
table_master=DataTable(source=ColumnDataSource(),
    columns=columns,width=800,height=200)
table_master.source.data=data

gpa=['A+','A','B+','B','C+','C','D+','D','F']
years=['2015','2016','2017']
colors=['#c9d9d3','#718dbf','#e84d60']
data={}
data['gpa']=gpa
data['2015']=[1, 4, 2, 4, 1, 6, 0, 2, 1]
data['2016']=[5, 2, 5, 8, 3, 10, 0, 1, 1]
data['2017']=[2, 4, 3, 12, 7, 12, 0, 2, 1]
source= ColumnDataSource(data=data)
p=figure(x_range=gpa,plot_height=500, title='GPA Counts by Year', toolbar_location=None,tools='')
p.vbar_stack(years,x='gpa', width=0.9, color=colors, source=source,legend=[value(x) for x in years])
p.y_range.start=0
p.y_range.end=30

def onclick(idx=0,name=None):
    if name=='Letters':
        letter=list(string.ascii_uppercase)[idx]
        cursor = obdcConnection.cursor()
        tsql="SELECT * FROM lgu.course where title like '"+letter+"%'"
        with obdcConnection:
            rows = cursor.execute(tsql).fetchall()
            id_list=list()
            title_list=list()
            dept_name_list=list()
            credit_list=list()
            instructor_list=list()
            for row in rows:
                id_list.append(row.course_id)
                title_list.append(row.title)
                dept_name_list.append(row.dept_name)
                credit_list.append(row.credits)
                instructor_list.append(row.instructor)
            data=dict(
                    id=id_list,
                    title=title_list,
                    dept=dept_name_list,
                    credit=credit_list,
                    instructor=instructor_list
                    )
            table_master.source.data=data
    elif name=='refresh':
        cursor = obdcConnection.cursor()
        if btnGroupTitle.active==0 and btnGroupDept.active==0:
            if optionGroup.active==0:
                tsql = "SELECT * FROM lgu.course where title like '"+title_input.value+"%' and dept_name like '"+dept_input.value+"%'"
            elif optionGroup.active==1:
                tsql = "SELECT * FROM lgu.course where title like '"+title_input.value+"%' or dept_name like '"+dept_input.value+"%'"
        elif btnGroupTitle.active==0 and btnGroupDept.active==1:
            if optionGroup.active==0:
                tsql = "SELECT * FROM lgu.course where title like '"+title_input.value+"%' and dept_name like '%"+dept_input.value+"%'"
            elif optionGroup.active==1:
                tsql = "SELECT * FROM lgu.course where title like '"+title_input.value+"%' or dept_name like '%"+dept_input.value+"%'"
        elif btnGroupTitle.active==0 and btnGroupDept.active==2:
            if optionGroup.active==0:
                tsql = "SELECT * FROM lgu.course where title like '"+title_input.value+"%' and dept_name like '%"+dept_input.value+"'"
            elif optionGroup.active==1:
                tsql = "SELECT * FROM lgu.course where title like '"+title_input.value+"%' or dept_name like '%"+dept_input.value+"'"
        elif btnGroupTitle.active==1 and btnGroupDept.active==0:
            if optionGroup.active==0:
                tsql = "SELECT * FROM lgu.course where title like '&"+title_input.value+"%' and dept_name like '"+dept_input.value+"%'"
            elif optionGroup.active==1:
                tsql = "SELECT * FROM lgu.course where title like '&"+title_input.value+"%' or dept_name like '"+dept_input.value+"%'"
        elif btnGroupTitle.active==1 and btnGroupDept.active==1:
            if optionGroup.active==0:
                tsql = "SELECT * FROM lgu.course where title like '%"+title_input.value+"%' and dept_name like '%"+dept_input.value+"%'"
            elif optionGroup.active==1:
                tsql = "SELECT * FROM lgu.course where title like '%"+title_input.value+"%' or dept_name like '%"+dept_input.value+"%'"
        elif btnGroupTitle.active==1 and btnGroupDept.active==2:
            if optionGroup.active==0:
                tsql = "SELECT * FROM lgu.course where title like '%"+title_input.value+"%' and dept_name like '%"+dept_input.value+"'"
            elif optionGroup.active==1:
                tsql = "SELECT * FROM lgu.course where title like '%"+title_input.value+"%' or dept_name like '%"+dept_input.value+"'"
        elif btnGroupTitle.active==2 and btnGroupDept.active==0:
            if optionGroup.active==0:
                tsql = "SELECT * FROM lgu.course where title like '&"+title_input.value+"' and dept_name like '"+dept_input.value+"%'"
            elif optionGroup.active==1:
                tsql = "SELECT * FROM lgu.course where title like '&"+title_input.value+"' or dept_name like '"+dept_input.value+"%'"
        elif btnGroupTitle.active==2 and btnGroupDept.active==1:
            if optionGroup.active==0:
                tsql = "SELECT * FROM lgu.course where title like '%"+title_input.value+"' and dept_name like '%"+dept_input.value+"%'"
            elif optionGroup.active==1:
                tsql = "SELECT * FROM lgu.course where title like '%"+title_input.value+"' or dept_name like '%"+dept_input.value+"%'"
        elif btnGroupTitle.active==2 and btnGroupDept.active==2:
            if optionGroup.active==0:
                tsql = "SELECT * FROM lgu.course where title like '%"+title_input.value+"' and dept_name like '%"+dept_input.value+"'"
            elif optionGroup.active==1:
                tsql = "SELECT * FROM lgu.course where title like '%"+title_input.value+"' or dept_name like '%"+dept_input.value+"'"
        else:
            tsql = "SELECT * FROM lgu.course;"
        with obdcConnection:
            rows = cursor.execute(tsql).fetchall()
            id_list=list()
            title_list=list()
            dept_name_list=list()
            credit_list=list()
            instructor_list=list()
            for row in rows:
                id_list.append(row.course_id)
                title_list.append(row.title)
                dept_name_list.append(row.dept_name)
                credit_list.append(row.credits)
                instructor_list.append(row.instructor)
        data=dict(
                id=id_list,
                title=title_list,
                dept=dept_name_list,
                credit=credit_list,
                instructor=instructor_list
                )
        table_master.source.data=data
    elif name=='Title':
        if btnGroupTitle.active==0:
            title_input.placeholder='begins with...'
        elif btnGroupTitle.active==1:
            title_input.placeholder='...contains...'
        elif btnGroupTitle.active==2:
            title_input.placeholder='...ends with'
    elif name=='Dept':
        if btnGroupDept.active==0:
            dept_input.placeholder='begins with...'
        elif btnGroupDept.active==1:
            dept_input.placeholder='...contains...'
        elif btnGroupDept.active==2:
            dept_input.placeholder='...ends with'


def onTableMasterSelect(attr,old,new):
    global data
    global source
    cursor = obdcConnection.cursor()
    tsql = "SELECT * FROM lgu.student"
    with obdcConnection:
        rows = cursor.execute(tsql).fetchall()
        gpa_list=list()
        years_list=list()
        dept_student_list=list()
        for row in rows:
            gpa_list.append(row.gpa)
            years_list.append(row.year)
            dept_student_list.append(row.dept_name)
        list_2015_new=list()
        list_2016_new=list()
        list_2017_new=list()    
        gpa=['A+','A','B+','B','C+','C','D+','D','F']
        for i in gpa:
            count_part=0
            count_total=0
            for j in gpa_list:
                if j==i and years_list[count_total]=='2015' and dept_student_list[count_total]==new:
                    count_part=count_part+1
                count_total=count_total+1
            list_2015_new.append(count_part)
            count_part=0
            count_total=0
            for j in gpa_list:
                if j==i and years_list[count_total]=='2016' and dept_student_list[count_total]==new:
                    count_part=count_part+1
                count_total=count_total+1
            list_2016_new.append(count_part)
            count_part=0
            count_total=0
            for j in gpa_list:
                if j==i and years_list[count_total]=='2017' and dept_student_list[count_total]==new:
                    count_part=count_part+1
                count_total=count_total+1
            list_2017_new.append(count_part)
        data={}
        data['gpa']=gpa
        data['2015']=list_2015_new
        data['2016']=list_2016_new
        data['2017']=list_2017_new
        source.data=data

btnGroupLetters.on_click(functools.partial(onclick,name='Letters'))
refresh.on_click(functools.partial(onclick,name='refresh'))
btnGroupTitle.on_click(functools.partial(onclick,name='Title'))
btnGroupDept.on_click(functools.partial(onclick,name='Dept'))
dept_select.on_change('value',onTableMasterSelect)

layout_query = layout(
    [
        [widgetbox(btnGroupLetters, width=1000)],
        [widgetbox(btnGroupTitle), widgetbox(btnGroupDept)],
        [widgetbox(title_input), widgetbox(paragraph, optionGroup, width=100), widgetbox(dept_input)],
        [widgetbox(refresh, width=100)],
        [widgetbox(table_master)],          
    ]
)

layout_chart = layout(
    [
        [widgetbox(dept_select),p]
    ]
)

tab1 = Panel(child=layout_query, title="Course Info")
tab2= Panel(child=layout_chart, title='Statistics')
tabs = Tabs(tabs=[tab1, tab2])

curdoc().add_root(tabs)

