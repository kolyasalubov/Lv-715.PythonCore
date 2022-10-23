from db_connect import DbConnection
import pandas as pd

class Analitics():

    def __init__(self) -> None:
        self.db_connect = DbConnection("Stat",'DESKTOP-I12GKNF\Rex', '', 'yes', 'DESKTOP-I12GKNF\SQLEXPRESS')

    def query(self, table):
        self.query = f"SELECT TOP 50 * FROM {table}"
        self.data = pd.read_sql(self.query, self.db_connect.connect())
        return self.data#['STC_NAME']


r= Analitics()
to_html = r.query('STC').to_html(index=False)
text_t = open("table.html", "w")
text_t.write(to_html)
text_t.close()



