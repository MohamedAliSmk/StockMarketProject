from timeit import default_timer as timer
import pandas as pd
import unittest
import sqlite3

from TrandingViewClasses import START, DataBase

class TestCode(unittest.TestCase):

    def test_database_connection(self):
        DataBase.Start()
        self.assertTrue(isinstance(DataBase.conn, sqlite3.Connection))
        DataBase.Stop()

    def test_store_in_database(self):
        # creating a test dataframe
        test_data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
        test_df = pd.DataFrame(data=test_data)

        # storing the dataframe in the database
        DataBase.Start()
        table_name = 'test_table'
        DataBase.StoreInDatabase(data=test_df, table_name=table_name, if_exists_value='replace', data_index=False)

        # reading the dataframe from the database
        read_df = pd.read_sql(f"SELECT * FROM {table_name}", con=DataBase.conn)

        self.assertTrue(test_df.equals(read_df))
        DataBase.Stop()

    def test_get_data(self):
        companies_urls =  ['EGX-MNHD','EGX-CCAP','EGX-FWRY']
        companies = START.get_data(companies_urls)
        self.assertTrue(len(companies) == 3)
        self.assertTrue(hasattr(companies[0], 'income_statement'))
        self.assertTrue(hasattr(companies[0], 'balance_sheet'))
        self.assertTrue(hasattr(companies[0], 'cashflow_statement'))
        self.assertTrue(hasattr(companies[0], 'statistics'))
        self.assertTrue(hasattr(companies[0], 'company_data'))

if __name__ == '__main__':
    unittest.main()
