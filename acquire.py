import os
def get_titanic_data():
    filename = "titanic.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)
        # Return the dataframe to the calling code
        return df  