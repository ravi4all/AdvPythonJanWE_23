import pymysql

# connection = pymysql.connect(host="localhost", port=3306, database="ems_db")
connection = pymysql.connect(host="localhost", port=3307, database="ems_db",
                             password="root", user="root", autocommit=True)

cursor = connection.cursor()
emp_name = 'John'
emp_id = 101
emp_dept = "IT"
emp_salary = 45000

query = f"insert into employees values ({emp_id},'{emp_name}','{emp_dept}',{emp_salary});"
print(query)
cursor.execute(query)

print("Data Inserted...")

connection.close()