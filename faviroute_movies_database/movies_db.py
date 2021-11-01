import sqlite3
# Creating a movie database
connection = sqlite3.connect('movies.db')
# creating a cursor
cursor = connection.cursor()
# creating a movies table
cursor.execute(""" CREATE TABLE movies(
    movie_name text,
    lead_actor text,
    actress text,
    release_date text,
    director_name text
)
""")

# creating records to store in database
movies_list = [('Maharshi', 'Mahesh Babu', 'Pooja Hegde', '9-May-2019', 'Vamshi Paidapally'),
               ('Pushpa', 'Allu Arjun', 'Rashmika Mandanna',
                '25-December-2021', 'Sukumar'),
               ('Rangasthalam', 'Ram Charan',
                'Samantha', '30-March-2018', 'Sukumar'),
               ('Geetha Govindam', 'Vijay Deverakonda',
                'Rashmika Mandanna', '15-August-2018', 'Parasuram'),
               ('Rebel', 'Prabhas', 'Tamanna',
                '28-Sepetember-2012', 'Raghava Lawrence'),
               ]

# inserting values into table
cursor.execute(
    "INSERT INTO movies VALUES ('Maharshi', 'Mahesh Babu', 'Pooja Hegde', '9-May-2019', 'Vamshi Paidapally')")
cursor.execute(
    "INSERT INTO movies VALUES ('Pushpa', 'Allu Arjun', 'Rashmika Mandanna','25-December-2021', 'Sukumar')")
cursor.execute(
    "INSERT INTO movies VALUES ('Rangasthalam', 'Ram Charan','Samantha', '30-March-2018', 'Sukumar')")
cursor.execute(
    "INSERT INTO movies VALUES ('Geetha Govindam', 'Vijay Deverakonda','Rashmika Mandanna', '15-August-2018', 'Parasuram')")
cursor.execute(
    "INSERT INTO movies VALUES ('Rebel', 'Prabhas', 'Tamanna','28-Sepetember-2012', 'Raghava Lawrence')")

# Retreving data
cursor.execute("SELECT * FROM movies")

# fetching the first record
# print(cursor.fetchone())

# fetching the first n records
# print(cursor.fetchmany(3))

# fetching all records
items = cursor.fetchall()
for item in items:
    print(item[0]+" "+item[1]+" "+item[2]+" "+item[3]+" "+item[4])

# commit our command
connection.commit()
# closing connection
connection.close()
