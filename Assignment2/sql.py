import pyodbc

# cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

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

#Select Query
def select():
    print ('Reading data from table')
    tsql = "SELECT * FROM lgu.course;"
    cursor = obdcConnection.cursor()
    with obdcConnection:
        rows = cursor.execute(tsql).fetchall()
        for row in rows:
            print ('Title: {}, Dept: {}, Instructor: {}'.format(row.title, row.dept_name, row.instructor))


obdcConnection = connectSQLServer()
select()