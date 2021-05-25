import sqlite3
import pandas as pd

def loadCsv(con, fileName, tableName):
    alldata = pd.read_csv(fileName)
    alldata.to_sql(tableName,con, index=False,if_exists='replace')

def selectData(con, query):

    sqlCmd = query
    tableList = pd.read_sql_query(sqlCmd,con)

    result = pd.read_sql_query(sqlCmd, con)

    return result

def SelectDataToTable(con, query, tableName):

    sqlCmd = query
    tableList = pd.read_sql_query(sqlCmd,con)

    result = pd.read_sql_query(sqlCmd, con)
    result.to_sql(tableName ,con, index=False,if_exists='replace')

    
def queryData(con):

    sqlCmd = 'select name from sqlite_master where type=\'table\';'
    tableList = pd.read_sql_query(sqlCmd,con)

    while sqlCmd != 'exit':
        try:
            if(sqlCmd =='1'):
                sqlCmd = 'select name from sqlite_master where type=\'table\';'

            result = pd.read_sql_query(sqlCmd, con)
            print('----------------------------------------------------------------------------------------')
            print(result.to_string())
            
            sqlCmd = input('SQL> ')

        except Exception as e:
            print('')
            print(e)
            print('An exception happened. Look at the query')
            sqlCmd = input('SQL> ')

def dropTable(con, tableName):
    con.execute('drop table \''+tableName + '\'')
    
def execQuery(con, qry):
    ds = con.execute(qry)


