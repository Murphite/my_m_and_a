import pandas as pd

def my_m_and_a(csv1, csv2, csv3):
    # Load the CSV files into pandas dataframes
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2, delimiter=';') # use tab as separator for second CSV file
    df3 = pd.read_csv(csv3) # set header to None and use semicolon as separator for third CSV file

    #rename specific column names
    df1.rename(columns = {'Gender': 'gender', 
                            'FirstName':'firstname',
                            'LastName':'lastname', 
                            'UserName': 'username', 
                            'Email':'email', 
                            'Age':'age', 
                            'City': 'city',
                            'Country':'country'},
                            inplace = True)
    
    df1['firstname'] = df1['firstname'].str.replace('"', '').replace('\\\\', '', regex=True)
    df1['lastname'] = df1['lastname'].str.replace('"', '').replace('\\\\', '', regex=True)    
    df1['gender'] = df1['gender'].replace({'0':'Male','1': 'Female'}).replace({'M': 'Male','F': 'Female'})

    df1.dropna(subset=['firstname'], inplace=True)
    df1.dropna(subset=['lastname'], inplace=True)
    df1.dropna(subset=['age'], inplace=True) 
        
    #turn entries to title case
    df1['city'] = df1['city'].str.title() 
    df1['country'] = df1['country'].str.title() 
    df1['username'] = df1['username'].str.title() 
    df1['firstname'] = df1['firstname'].str.title()
    df1['lastname'] = df1['lastname'].str.title()
    df1['gender'] = df1['gender'].str.title() 
    df1['age'] = df1['age'].astype(str)  
   
    # assign column names
    df2.columns = ['age', 'city', 'gender', 'name', 'email']
    
    # remove any quotation marks from name and email
    df2['name'] = df2['name'].str.replace('"', '').replace('\\\\', '', regex=True)
    
    df2['name'] = df2['name'].str.title() 
    df2['city'] = df2['city'].str.title()
    df2['gender'] = df2['gender'].str.title()
   
    df2.dropna(subset=['name'], inplace=True)
    df2.dropna(subset=['age'], inplace=True)

    df2['email'] = df2['email'].str.replace('"', '')
    df2['age'] = df2['age'].apply(lambda x: str(x.replace('yo', '').replace('s', '').replace('"', '').replace('years', '').replace('s', '').replace('year', '').replace('integer_', '')))
    df2['gender'] = df2['gender'].replace({'0':'Male','1': 'Female'}).replace({'M': 'Male','F': 'Female'})
    
    # split the Name column into First Name and Last Name columns
    df2[['firstname', 'lastname']] = df2['name'].str.split(expand=True)
    df2 = df2.drop(columns=['name'])
    df2['age'] = df2['age'].astype(str)
    
     # remove the "string_" prefix from each value in the DataFrame and spliting
    df3[['Gender', 'Name', 'Email', 'Age', 'City', 'Country']] = df3['Gender'].apply(lambda x: x.replace('string_', '')).str.split('\t', expand=True)

    df3.dropna(subset=['Age'], inplace=True)
    df3.dropna(subset=['Name'], inplace=True)
    #df3['Age'] = df3['Age'].astype(float)

    df3['Name'] = df3['Name'].apply(lambda x: str(x.replace('"', '')))

    #clean up Gender column
    df3['Gender'] = df3['Gender'].apply(lambda x: str(x.replace('boolean_', '').replace('character_', '')))
    df3['Name'] = df3['Name'].str.title()
    df3['Gender'] = df3['Gender'].str.title()
    df3['City'] = df3['City'].str.title() 
    df3['Country'] = df3['Country'].str.title() 
   
    # split the Name column into First Name and Last Name columns
    df3[['Firstname', 'Lastname']] = df3['Name'].str.split(expand=True)
    df3 = df3.drop(columns=['Name'])


    # clean up age column
    df3.dropna(subset=['Age'], inplace=True)
    df3['Age'] = df3['Age'].apply(lambda x: str(x.replace('yo', '').replace('s', '').replace('"', '').replace('years', '').replace('s', '').replace('year', '').replace('integer_', '')))

    df3['Gender'] = df3['Gender'].replace({'0':'Male','1': 'Female'}).replace({'M': 'Male','F': 'Female'})
    df3['Age'] = df3['Age'].astype(str)

    # assign new column names
    df3.columns = ['gender', 'email', 'age', 'city', 'country', 'firstname', 'lastname']

    
    
    # Rename the columns to match the database schema
    df1 = df1.rename(columns={
        "firstname": "FirstName",
        "lastname": "LastName",
        "gender": "Gender",
        "email": "Email",
        "age": "Age",
        "city": "City",
        "country": "Country",
        "username": "UserName"
    })

    df2 = df2.rename(columns={
        "age": "Age",
        "city": "City",
        "gender": "Gender",
        "firstname": "FirstName",
        "lastname": "LastName",
        "email": "Email"
    })

    df3 = df3.rename(columns={        
        "gender": "Gender",
        "firstname": "FirstName",
        "lastname": "LastName",
        "email": "Email",
        "age": "Age",
        "city": "City",
        "country": "Country"
    })
    
    # Return the merged dataframe
    merged_df = pd.concat([df1, df2, df3], ignore_index=True)
    return merged_df
