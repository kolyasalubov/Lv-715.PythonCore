import pyodbc
import pandas as pd

class DbConnection():

    __connection = None

    def __new__(cls, *args, **kwargs):
        if cls.__connection == None:
            cls.__connection = super().__new__(cls)
        return cls.__connection

    def __del__(self):
        DbConnection.__connection = None

    def __init__(self,  db, user, password, trust, server):
        self.server = server
        self.db = db
        self.user = user
        self.password = password
        self.trust = trust
        # self.connect()
    
    def connect(self):
        self.cnxn_str = (
                    "Driver={SQL Server Native Client 11.0};"
                    f"Server={self.server};"
                    f"Database={self.db};"
                    f"Trusted_Connection={self.trust};"
                    f'UID={self.user};'
                    f"PWD={self.password}"
                    )
                    
        self.cnxn = pyodbc.connect(self.cnxn_str)

        return self.cnxn

    def close(self):
        del cnxn