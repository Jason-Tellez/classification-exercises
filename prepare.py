def prep_iris(df):
    """
    Takes in data from the iris db and turns it into a dataframe.
    Drops 'species_id' and 'measurement_id' columns.
    Renames the 'species_name' column to 'species'.
    Creates dummy variables of species name.
    """
    df.drop(columns=["species_id","measurement_id"], inplace=True)
    df.rename(columns={"species_name": "species"}, inplace=True)
    df_dummy = pd.get_dummies(df['species'])
    df = pd.concat([df, df_dummy], axis=1)
    return df