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

refresh = Button(label="Refresh")
btnGroupTitle = RadioButtonGroup(name='title', labels=["begins with...", "...contains...", "...ends with"], active=1)
btnGroupDept = RadioButtonGroup(name='dept', labels=["begins with...", "...contains...", "...ends with"], active=1)
paragraph = Paragraph(text="option")
optionGroup = RadioGroup(labels=["and", "or"], active=0, width=100, inline=True)
btnGroupLetters = RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
title_input = TextInput(value="", title="Title:", placeholder="contains....")
dept_input = TextInput(value="", title="Department:", placeholder="contains....")

layout_query = layout(
    [
        [widgetbox(btnGroupLetters, width=1000)],
        [widgetbox(btnGroupTitle), widgetbox(btnGroupDept)],
        [widgetbox(title_input), widgetbox(paragraph, optionGroup, width=100), widgetbox(dept_input)],
        [widgetbox(refresh, width=100)],            
    ]
)

x = list(range(11))
y0 = x
y1 = [10 - i for i in x]
y2 = [abs(i - 5) for i in x]

# create a new plot
s1 = figure(plot_width=250, plot_height=250, title=None)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# create another one
s2 = figure(plot_width=250, plot_height=250, title=None)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# create and another
s3 = figure(plot_width=250, plot_height=250, title=None)
s3.square(x, y2, size=10, color="olive", alpha=0.5)


layout_chart = layout (
    [s1,s2],
    [s3]
)

tab1 = Panel(child=layout_query, title="Course Info")
tab2 = Panel(child=layout_chart, title="Statistics")
tabs = Tabs(tabs=[tab1, tab2])

curdoc().add_root(tabs)