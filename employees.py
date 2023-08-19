import pymysql
try:
    con=pymysql.connect(host='mysql',database='employees',user='root',passwd='password')
    cursor=con.cursor()
    print("Connection Established with database")
    #employees table has already been created. 
    #If you want to create new table uncomment following line
    cursor.execute("CREATE TABLE IF NOT EXISTS employees (eno int(10) primary key,ename varchar(20),esal double(10,2),eaddr varchar(50))")
    option ='y'
    while option.lower()!='n':
        eno=input("Enter employee number:")
        ename=input("Enter employee name:")
        esal=float(input("Enter employee salary:"))
        eaddr=input("Enter employee address:")
        query = "INSERT INTO employees (eno, ename, esal, eaddr) VALUES (%s, %s, %s, %s)"
        params = (eno, ename, esal, eaddr)
        cursor.execute(query, params)
        con.commit()
        print("Records inserted successfully")
        option=input("Do you want to add more emploees, [Y/N]:")
        
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("there is a problem", e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


