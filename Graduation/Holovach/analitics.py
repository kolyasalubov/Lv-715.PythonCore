from db_connect import DbConnection
import pandas as pd
from datetime import datetime

class Analitics():

    def __init__(self) -> None:
        self.db_connect = DbConnection("Stat",'DESKTOP-I12GKNF\Rex', '', 'yes', 'DESKTOP-I12GKNF\SQLEXPRESS')

    def query(self, table):
        self.query = f"SELECT TOP 50 * FROM {table}"
        self.data = pd.read_sql(self.query, self.db_connect.connect())
        return self.data#['STC_NAME']

    def log(self, txt="Table created"):
            self.sql = f"INSERT INTO LOGS (DATE_OF_LOGGING, LOG_DATA) VALUES ('{datetime.now()}', '{txt}')"
            self.cursor = self.db_connect.connect().cursor()
            self.cursor.execute(self.sql)
            self.cursor.commit()
            return True


