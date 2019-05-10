import sqlite3
import sys

def load_csv(csv_file,con, cur):
    relations = []
    data = open(csv_file, 'r')

    tablename = data.readline().strip()

    for line in data:
        line = line.strip()
        if line=='office' or line=='agency' or line=='manage' or line=='agreements':
            for item in relations:

                query = "INSERT " + "INTO " + tablename + " VALUES " + '(' + item + ' ); '
                cur.execute(query)
            tablename = line
            relations =[]
        else:
            relations.append(line)

    data.close()

    for item in relations:
        query = "INSERT " + "INTO " + tablename + " VALUES " + '(' + item + ' ); '
        cur.execute(query)

def insert(con, cur):

    query = input("Enter SQL Insert Statement :")

    if "Insert" or "insert" in query:
        try:
            cur.execute(query)
        except sqlite3.Error:
            print("Erro. Insert statement is invalid")
            return
        print ("\nData successfully inserted")
    else:
        print("Not Insert command. Returning to main menu.")

def delete_row(con, cur):

    query = input("Enter SQL Delete Statement :")

    if "Delete" or "delete" in query:
        try:
            cur.execute(query)
        except sqlite3.Error:
            print("Error. Delete statement is invalid")
            return
        print ("\nData successfully deleted")
    else:
        print("Not delete command. Returning to main menu.")

def select(con, cur):

    query = input("Enter SQL Select Statement :")

    
    if "Select" or "select" in query:
        try:
            cur.execute(query)
        except sqlite3.Error:
            print("Error. Select statement is invalid")
            return
        data = cur.fetchall()
        print ("The results are: ")
        for rec in data:
            print ()
            for field in rec:
                print (field, end=" ")
        print("\n")
    else:
        print("Not Select command. Returning to main menu.")


def erase(con, cur):
    print ("Tables are: office, agency, manage, agreements")
    table = input("Enter table you would like to erase: ")
    query = "DELETE FROM " + table
    tables= ["office","agency","manage","agreements"]

    if table not in tables:
        print("Error. Table not found. Returning to main menu")
        return

    cur.execute(query)

    print("Data in " + table + " has been erased\n")




def action(choice, con, cur):

    if choice == "select":
        select(con,cur)
    elif choice == "insert":
        insert(con,cur)
    elif choice == "delete":
        delete_row(con,cur)
    elif choice == "erase":
        erase(con,cur)
    elif choice == "load csv":
        csv_file = input("Enter the csv file you would like to load\n")
        load_csv(csv_file, con,cur)
        print ("\nData successfully loaded\n")




def main():
    con = sqlite3.connect("soap.db")
    cur = con.cursor()
    choice = ""
    menu="Enter what you would like to do? \n 1. select \n 2. insert \n 3. delete \n 4. erase \n 5. load csv \n 6. quit \n"

    while choice != "quit":
        choice = input(menu)
        if(choice is  "quit"):
            break
        action(choice, con, cur)

    con.commit()
    con.close()

    sys.exit(1)

main()