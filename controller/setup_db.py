import sqllite3
con=sqllite3.connect("childcare_data.db")

#You can drop tables in LIFO order due to foreign key dependancies
con.execute('DROP TABLE IF EXISTS inspection_data')
con.execute('DROP TABLE IF EXISTS location_data')

con.execute('CREATE TABLE location_data ()')


