import sqlite3
import pandas as pd
from icecream import ic

def data():
    connection = sqlite3.connect("MissionSQL.db") ## establish the connection to db

    query ='''
    SELECT price, AVG(positive) as avg_reviews, COUNT(*) as game_count
    FROM games
    WHERE price > 0
    GROUP BY price
    HAVING game_count > 5 
    ORDER BY price ASC
    '''
    ## excluding ftp games due to alot of them not being popular enough causing
    ## skewed results.
    ##
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

df = data() # establish data frame through func
ic("Data Ready") 

ic(df.head()) # print out the head of df for simplicity.