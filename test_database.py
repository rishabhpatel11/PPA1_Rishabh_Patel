import pytest
import CommandLineApp
from mock import Mock, patch
import doubles

# doubles.expect(and Mocks) are mocks and doubles.allow are stubs

#Mock
def test_database_connection():
    # configuration for database from the commandlineapp file
    config=CommandLineApp.Config()
    # Mocking database connection function
    doubles.expect(config).connectDatabase
    config.connectDatabase()

#Stub
def test_bmi_insert():
    connection=CommandLineApp.Connection(0,0,0)
    feet=5
    inches=10
    weight=200
    output=[29.4,'Overweight']
    entry=[{'feet':int(feet),'inches':int(inches),'weight':float(weight),'BMI':output[0],'category':output[1]}]
    # Stubbing execute of an insert to the table
    doubles.allow(connection).insertDatabase.with_args(entry)
    # Testing the stubbed function still works
    assert connection.insertDatabase(entry) == None

#Stub
def test_bmi_query():
    connection=CommandLineApp.Connection(0,0,0)
    # Stubbing query function
    doubles.allow(connection).queryTable.with_args('bmi_table').and_return([{'feet': 5, 'inches': 10, 'weight': 200.0, 'BMI': 29.4, 'category': 'Overweight'}])
    assert connection.queryTable('bmi_table') == [{'feet': 5, 'inches': 10, 'weight': 200.0, 'BMI': 29.4, 'category': 'Overweight'}]

def test_bmi_dummy_database():
    connection=CommandLineApp.Connection(0,0,0)
    # testdb is just an empty array I created in commandlineapp.py for testing purposes
    connection.testdb.append({'feet': 5, 'inches': 10, 'weight': 200.0, 'BMI': 29.4, 'category': 'Overweight'})
    # check new entry is in test database
    assert {'feet': 5, 'inches': 10, 'weight': 200.0, 'BMI': 29.4, 'category': 'Overweight'} in connection.testdb

#Stub
def test_distances_insert():
    connection=CommandLineApp.Connection(0,0,0)
    output=[5,6,7,8,2.82843]
    entry=[{'x1':output[0],'y1':output[1],'x2':output[2],'y2':output[3],'distance':output[4]}]
    # Stubbing execute of an insert to the table
    doubles.allow(connection).insertDatabase.with_args(entry)
    # Testing the stubbed function still works
    assert connection.insertDatabase(entry)== None

#Stub
def test_distances_query():
    connection=CommandLineApp.Connection(0,0,0)
    # Stubbing query function
    doubles.allow(connection).queryTable.with_args('distances_table').and_return([{'x1':5,'y1':6,'x2':7,'y2':8,'distance':2.82843}])
    assert connection.queryTable('distances_table') == [{'x1':5,'y1':6,'x2':7,'y2':8,'distance':2.82843}]

def test_distances_dummy_database():
    connection=CommandLineApp.Connection(0,0,0)
    # testdb is just an empty array I created in commandlineapp.py for testing purposes
    connection.testdb.append({'x1':5,'y1':6,'x2':7,'y2':8,'distance':2.82843})
    # check new entry is in test database
    assert {'x1':5,'y1':6,'x2':7,'y2':8,'distance':2.82843} in connection.testdb
    
#Mock
def test_bmi_table_missing_attribute():
    # Creating mock database entry missing an attribute( bmi category in this case) to test for retrieve failure
    # Could happen if the database was accessed and altered outside this program
    m=Mock()
    m.feet=5
    m.inches=10
    m.weight=200
    m.BMI=29.4
    del m.category
    m.created_at='2019-10-15 03:55:03'
    query=[m]
    with pytest.raises(AttributeError):
        CommandLineApp.printDatabase('bmi_table',['feet','inches','weight','BMI','category','created_at'],query)

#Mock
def test_distances_table_missing_attribute():
    # Creating mock database missing an attribute( y2 in this case) to test for retrieve failure
    # Could happen if the database was accessed and altered outside this program
    m=Mock()
    m.x1=5
    m.y1=6
    m.x2=7
    del m.y2
    m.distance=2.82843
    m.created_at='2019-10-15 03:55:03'
    query=[m]
    with pytest.raises(AttributeError):
        CommandLineApp.printDatabase('distances_table',['x1','y1','x2','y2','distance','created_at'],query)

