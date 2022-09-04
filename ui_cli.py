# --------------------------------------------------------------------------------------------------
# IMPORT MODULE
# --------------------------------------------------------------------------------------------------

from data_base import *

# --------------------------------------------------------------------------------------------------
# VARIABLE DECLARATION
# --------------------------------------------------------------------------------------------------


COMMANDS = ["CB", "CT", "ST", "DT", "IR", "DR", "UR", "CR", "EXIT"]
COMMANDS_LIST = [
    {"code": "CB", "description": "Create connection"}, 
    {"code": "CT", "description": "Create table"},
    {"code": "ST", "description": "Show table"},
    {"code": "DT", "description": "Delete table"},
    {"code": "IR", "description": "Insert record"},
    {"code": "DR", "description": "Delete record"},
    {"code": "UR", "description": "Update record"},
    {"code": "CR", "description": "Consult record"},
    {"code": "EXIT", "description": "Exit program"}]


# --------------------------------------------------------------------------------------------------
# FUNCTION DECLARATION 
# --------------------------------------------------------------------------------------------------

#Function to receive commands
def receive_command():
    command = input("\nInsert a command: ").upper()
    while command not in COMMANDS:
        command = input("Invalid command. Please enter a valid command: ").upper()

    return command
    

#Function to initialize program   
def initialize_program():
    print("\nCreate data base with python from command line using Sqlite3")
    print("\nValid commands")
    for command in COMMANDS_LIST:
        print(f'  {command["code"]}: {command["description"]}')

    command = receive_command()
    while command != "EXIT":
        if command == "CB":
            connect_db()      
        elif command == "CT": 
            create_table()
        elif command == "ST": 
            show_table()  
        elif command == "DT": 
            delete_tables()           
        elif command == "IR": 
            insert_records()   
        elif command == "DR": 
            delete_records()
        elif command == "UR": 
            update_records()
        elif command == "CR": 
            consult_record() 
        command = receive_command()    

    print("\nFinished program")






