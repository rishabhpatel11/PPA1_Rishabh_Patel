import RetirementCalculator
import SplitTipCalculator
import BMICalculator
import DistanceCalculator
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from prettytable import PrettyTable

class Config:
    def get(self,info):
        if(info=='user'):
            return 'root'
        if(info=='password'):
            return 'password'
        if(info=='host'):
            return 'localhost'
        if(info=='port'):
            return 3308
        if(info=='database'):
            return 'ppa2'
    def connectDatabase(self):
        user = self.get('user')
        password = self.get('password')
        host = self.get('host')
        port = self.get('port')
        name = self.get('database')
        engine = db.create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{name}')
        # Making connection
        connection = engine.connect()
        # Getting metadata of the whole database
        metadata = db.MetaData(bind=engine)
        return engine,connection,metadata
        

class Connection:
    testdb=[]
    def __init__(self,engine,connection,metadata):
        self.engine=engine
        self.connection=connection
        self.metadata=metadata
    def queryTable(self,tableName):
        # Making a session
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        session = Session()
        self.metadata.reflect(only=[tableName])
        global table
        # Getting metadata of the specific table
        table = self.metadata.tables[tableName]
        # Querying all entires in the table
        query=session.query(table)
        return query.all()

    # Insert entry into the database
    def insertDatabase(self,entry):
        self.connection.execute(table.insert(),entry)

# Printing current state of the database table
def printDatabase(tableName,tableAttributes,query):
    # Setting up PrettyTable(used for printing formatted data) column names
    currentTable=PrettyTable(tableAttributes)
    # Looping through each entry in the table
    for row in query:
        # Adding entry to the PrettyTable
        if(tableName=='bmi_table'):
            currentTable.add_row([row.feet,row.inches,row.weight,row.BMI,row.category,row.created_at])
        if(tableName=='distances_table'):
            currentTable.add_row([row.x1,row.y1,row.x2,row.y2,row.distance,row.created_at])
    # Printing table
    print(currentTable)
    return currentTable

def main():
    while(True):
        print('Enter a number to select a function from the list:')
        print('1. Body Mass Index Calculator')
        print('2. Retirement Age Calculator')
        print('3. Shortest Distance Calculator')
        print('4. Split the Tip')
        print('5. Exit')
        choice=(int)(input("-->"))
        if(choice == 1):
            # Printing current state of the database table
            query=c.queryTable('bmi_table')
            printDatabase('bmi_table',['feet','inches','weight','BMI','category','created_at'],query)

            feet=input("Enter the feet part of your total height as a whole number: \n")
            inches=input("Enter the inches part of your total height as a whole number: \n")
            weight=input("Enter your weight in pounds as a number: \n")
            output=BMICalculator.bmi(feet,inches,weight)
            print("Your Body Mass Index is: " + str(output[0]))
            print("Your Body Mass Index falls under the category: " + output[1])

            # Create new entry in database
            entry=[{'feet':int(feet),'inches':int(inches),'weight':float(weight),'BMI':output[0],'category':output[1]}]
            c.insertDatabase(entry)
            
        if(choice == 2):
            age=input("Enter your age as a whole number: \n")
            salary=input("Enter your annual salary as a number: \n")
            saved=input("Enter the percent of your salary you plan on saving yearly as a number: \n")
            goal=input("Enter your desired retirement savings goal as a number: \n")
            output=RetirementCalculator.retirement(age,salary,saved,goal)
            if(output[1] == -1):
                print(output[0])
            else:
                print(output[0] + str(output[1]))

        if(choice == 3):
            # Printing current state of the database table
            query=c.queryTable('distances_table')
            printDatabase('distances_table',['x1','y1','x2','y2','distance','created_at'],query)

            print("\n\n\nRefer to the 2 points as: (x1,y1) and (x2,y2)")
            x1=input("Enter x1: \n")
            y1=input("Enter y1: \n")
            x2=input("Enter x2: \n")
            y2=input("Enter y2: \n")
            output=DistanceCalculator.distance(x1,y1,x2,y2)
            print("The shortest distance between the points is: " + str(output[4]))

            # Create new entry in database
            entry=[{'x1':output[0],'y1':output[1],'x2':output[2],'y2':output[3],'distance':output[4]}]
            c.insertDatabase(entry)

        if(choice == 4):
            print("Calculator adds a 15% tip rounded to the nearest cent")
            total=input("Enter the total of the bill as a number without any $ signs: \n")
            guests=input("Enter the number of guests you want to split the bill for: \n")
            output=SplitTipCalculator.splitTip(total,guests)
            print("Total with tip: " + str(output[len(output)-1]))
            for i in range(len(output)-1):
                print("guest"+str(i)+"-"+str(output[i]))

        if(choice == 5):
            print("Exiting command line app. The web app will continue to run until you crtl+c out")
            exit()

if __name__ == "__main__":
    # Defining database configuration per mysql requirements and initial database properties from docker
    config = Config()
    engine,connection,metadata=config.connectDatabase()
    global c
    c=Connection(engine,connection,metadata)
    main()