# --------------------------------------------------------------------------------------------------
# IMPORT MODULE
# --------------------------------------------------------------------------------------------------

import sqlite3
from sqlite3 import Error
import re
from tabulate import tabulate


# --------------------------------------------------------------------------------------------------
# VARIABLE DECLARATION
# --------------------------------------------------------------------------------------------------

connection = None


# --------------------------------------------------------------------------------------------------
# FUNCTION DECLARATION 
# --------------------------------------------------------------------------------------------------


#Create connection and database        
def connect_db():
    global connection
    try:
        connection = sqlite3.connect('base.db')
        print("\nSuccessful connection")
        return connection
    except:
        Error

    
#Create table        
def create_table():
    connection
    create_cursor = connection.cursor()
    create_cursor.execute(
        """CREATE TABLE IF NOT EXISTS parques_de_escalada 
        (Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Name text NOT NULL, Country text NOT NULL, 
        Town text NOT NULL, Rock_type text NOT NULL)"""
    )
    connection.commit()
    print("\nTable created successfully")


#Print table's name   
def show_name():
    connection
    create_cursor = connection.cursor()
    create_cursor.execute(
        """SELECT name FROM sqlite_master 
        WHERE type = 'table' AND name = 'parques_de_escalada'"""
    )
    print("\n", create_cursor.fetchall())


#Show total records on table
def show_table():
        connection
        create_cursor = connection.cursor()
        create_cursor.execute("SELECT * FROM parques_de_escalada;")
        records = create_cursor.fetchall()
        show_name()
        print("\n", tabulate(records, headers=["ID", "Name", "Country", "Town", "Rock type"]))    
        print("\nNumber of records: ", len(records))


#Delete tables
def delete_tables():
    try:
        connection
        create_cursor = connection.cursor()
        create_cursor.execute("DROP TABLE IF EXISTS parques_de_escalada")
        connection.commit()
        print("\nTable deleted")
    except:
        print("Table does not exists. Please create a table")
    

#Insert records
def insert_records(): 
    try:
        connection
        text_1 = "Validated string: {}"
        text_2 = "Invalid string: {}"
        r1 = input("\nInsert name:").capitalize()
        r2 = input("Insert country:").capitalize()
        r3 = input("Insert town:").capitalize()
        r4 = input("Insert rock type:").capitalize()
        pattern = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"

        if(re.match(pattern, r1)):
            print("\n", text_1.format(r1))
            sql = (
                """INSERT INTO parques_de_escalada
                (Name, Country, Rock_type) VALUES(?, ?, ?, ?)"""
            )
            data = (r1, r2, r3, r4)
            create_cursor = connection.cursor()
            create_cursor.execute(sql, data)
            connection.commit()
            print("\nNumber of records entered: ", create_cursor.rowcount) 
        else:
            print(text_2.format(r1))
            print("\nThe record could not be entered. Please try again")
    except:
        print("No connection available. Please create connection")


#Delete records
def delete_records():
    try:
        connection
        text_1 = "Validated id: {}"
        text_2 = "Invalid id: {}"
        r0 = input("\nInsert id number:")
        pattern = "[0-9]"

        if(re.match(pattern, r0)):
            print("\n", text_1.format(r0))
            sql = ("DELETE from parques_de_escalada where id = ?")
            data = (r0)
            create_cursor = connection.cursor()
            create_cursor.execute(sql, data)
            connection.commit()
            print("\nThe record has been deleted")
        else:
            print(text_2.format(r0))
            print("\nThe record could not be deleted. Please try again")
    except:
        print("No connection available. Please create connection")


#Update records
def update_records():
    try:
        connection
        text_1 = "Validated string: {}"
        text_2 = "Invalid string: {}"
        r0 = input("\nInsert id number:")
        r1 = input("\nInsert name update:").capitalize()
        r2 = input("Insert country update:").capitalize()
        r3 = input("Insert town update:").capitalize()
        r4 = input("Insert rock type update:").capitalize()
        pattern = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"

        if(re.match(pattern, r1)):
            print("\n", text_1.format(r1))
            sql = (
                """UPDATE parques_de_escalada SET 
                Name = ?, Country = ?, Town = ?, Rock_type = ? where id = ?"""
            )
            data = (r1, r2, r3, r4, r0)
            create_cursor = connection.cursor()
            create_cursor.execute(sql, data)
            connection.commit()
            print("\nNumber of records updated: ", create_cursor.rowcount) 
        else:
            print("\n", text_2.format(r1))
            print("\nThe record could not be updated. Please try again")
    except:
        print("No connection available. Please create connection")


#Show an specific record
def consult_record():
    try:
        connection
        text_1 = "Validated id: {}"
        text_2 = "Invalid id: {}"
        r0 = input("\nInsert id number:")
        pattern = "[0-9]"

        if(re.match(pattern, r0)):
            print("\n", text_1.format(r0))
            sql = ("SELECT * FROM parques_de_escalada where id = ?")
            data = (r0)
            create_cursor = connection.cursor()
            create_cursor.execute(sql, data)
            records = create_cursor.fetchall()
            for row in records:
                print("\nName:", row[1])
                print("Country:", row[2])
                print("Rock type:", row[3]) 
        else:
            print(text_2.format(r0))
    except:
        print("No connection available. Please create connection")



 
