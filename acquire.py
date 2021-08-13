import os
import env


def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    filename = "titanic.csv"
    if os.path.isfile(filename):
        df_titanic = pd.read_csv(filename)
        return df_titanic
    else:
        # read the SQL query into a dataframe
        df_titanic = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df_titanic.to_csv(filename)
        # Return the dataframe to the calling code
        return df_titanic



def new_iris_data():
    filename = "iris_df.csv"
    if os.path.isfile(filename):
        df_iris = pd.read_csv(filename)
        return df_iris
    sql_query = """
                SELECT measurements.measurement_id,
	                species.species_name,
                    species.species_id,
                    measurements.sepal_length,
                    measurements.sepal_width,
                    measurements.petal_length,
                    measurements.petal_width
                FROM measurements 
                JOIN species 
                ON measurements.species_id = species.species_id;
                """
    df_iris = pd.read_sql(sql_query, get_connection('iris_db'))
    df_iris.to_csv(filename)
    return df_iris