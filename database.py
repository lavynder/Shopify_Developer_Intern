# -*- coding: utf-8 -*-


import sqlite3 
from dataclasses import dataclass

# =============================================================================
# THIS MODULE DEFINES THE CLASSES THAT INTERACT WITH THE SQlite3 DATABASE SYSTEM
# =============================================================================

@dataclass
class Database:
# =============================================================================
#     THIS CLASS DEFINES HOW THE MAIN FILE WILL INTERACT WITH THE DATABASE
#     USING THE SQlite3 MODULE.
#
#     THE commit() COMMAND ISN'T NEEDED WITH THE PYTHON COMMAND with TO STORE
#     INFORMATION WITHIN THE DATABASE.
#     
#     THE CONNECTIONS ARE OPEN AND CLOSED LOCALLY WITHIN THE FUNCTIONS FOR 
#     BETTER PRIVACY AND SECURITY.
#
#     ADDITIONALLY, ALL THE METHODS ARE PROTECTED SO THAT THEY CANNOT BE ACCESSED
#     FROM OUTSIDE THE METHOD, BUT CAN STIL BE INHERITED.
# =============================================================================

    
    
    def _createTable(self, databaseName):       
# =============================================================================
#         THIS METHOD DEFINES HOW THE MODULE CREATES THE TABLES WITHIN THE DATABASE.
#         
#         THREE TABLES ARE CREATED: 
#             - THE inventory TABLE HOLDS THE ITEM SERIAL NUMBER AND THE
#             ITEM DESCRIPTION. ALL ITEMS MUST BE UNIQUE, SO serial IS THE 
#             PRIMARY KEY
#             - THE locations TABLE HOLDS THE AVAILABLE LOCATIONS, AND A DESCRIPTION
#             OF THE LOCATION. ALL LOCATIONS MUST BE UNIQUE, SO location IS THE
#             PRIMARY KEY 
#             - THE stocks TABLE CARRIES HOLDS THE AVAILABLE LOCATIONS AND THE 
#             CORRESPONDING ITEMS, AND VICE VERSA. IT ALSO HOLDS THE AMOUNT OF 
#             ITEMS ARE AT THE CORRESPONDING LOCATION. BOTH serial AND location
#             ARE FOREIGN KEYS, CORRESPONDING TO THE inventory AND locations
#             TABLES RESPECTIVELY
# =============================================================================
        
        
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()

        with conn:            
            # CREATES THE serial TABLE WITHIN THE DATABASE
            try:
                c.execute('''CREATE TABLE inventory(        
                            item text,
                            desc text,
                            PRIMARY KEY(item)
                            )''')
            
            # IF THE TABLE ALREADY EXISTS, THEN THE USER WILL BE NOTIFIED
            except sqlite3.OperationalError:
                print('THE inventory DATABASE TABLE ALREADY EXISTS')   
            
            # IF THE TABLE CANNOT BE CREATED, THEN THE USER IS NOTIFIED
            except:
                print('AN ERROR OCCURED WHEN CREATING THE inventory DATABASE TABLE')
                print('PLEASE ASK FOR HELP')
            
            # CREATES THE locations TABLE WITHIN THE DATABASE
            try:
                c.execute('''CREATE TABLE locations(        
                                location text,
                                desc text,
                                PRIMARY KEY(location)
                                )''')
            
            # IF THE TABLE ALREADY EXISTS, THEN THE USER WILL BE NOTIFIED
            except sqlite3.OperationalError:
                print('THE locations DATABASE TABLE ALREADY EXISTS')   
            
            # IF THE TABLE CANNOT BE CREATED, THEN THE USER IS NOTIFIED
            except:
                print('AN ERROR OCCURED WHEN CREATING THE locations DATABASE TABLE')
                print('PLEASE ASK FOR HELP')
            
            try:
                c.execute('''CREATE TABLE stock(        
                            item text,
                            location text,
                            stock integer,
                            FOREIGN KEY (item) REFERENCES inventory(item),
                            FOREIGN KEY (location) REFERENCES inventory(locations)
                            )''')
            
            # IF THE TABLE ALREADY EXISTS, THEN THE USER WILL BE NOTIFIED
            except sqlite3.OperationalError:
                print('THE stock DATABASE TABLE ALREADY EXISTS')   
            
            # IF THE TABLE CANNOT BE CREATED, THEN THE USER IS NOTIFIED
            except:
                print('AN ERROR OCCURED WHEN CREATING THE locations DATABASE TABLE')
                print('PLEASE ASK FOR HELP')
                
                
                
                
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
    
    
    
    def _add_item(self, item, desc, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW THE Database CLASS ADDS A NEW ITEM TO THE inventory
#         TABLE WITHIN THE SPECIFIED DATABASE.
#         
#         TWO VALUES ARE SAVED IN THE TABLE: 
#             - THE ITEM'S SERIAL NUMBER/NAME
#             - THE ITEM'S DESCRIPTION
#             
#         THE ARGUMENTS PASSED THROUGH SHOULD ALL BE IN STRING FORMAT
# =============================================================================

        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        
        with conn:
            # ADDS THE PASSED VALUES INTO THE inventory TABLE
            c.execute('''INSERT INTO inventory VALUES(
                        :item,
                        :desc
                        )''', {
                        'item': item,
                        'desc': desc
                        })
    
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
          
    def _add_location(self, location, desc, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW THE Database CLASS ADDS A NEW LOCATION TO THE 
#         location TABLE WITHIN THE SPECIFIED DATABASE.
#         
#         TWO VALUES ARE SAVED IN THE TABLE:
#             - THE LOCATION'S NAME
#             - THE LOCATION'S DESCRIPTION
#             
#         THE ARGUMENTS PASSED THROUGH SHOULD ALL BE IN STRING FORMAT
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            # ADDS THE PASSED VALUES INTO THE inventory TABLE
            c.execute('''INSERT INTO locations VALUES(
                        :location,
                        :desc
                        )''', {
                        'location': location, 
                        'desc': desc
                        })
    
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
        
    def _add_itemLocation(self, item, location, stock, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW AN EXISTING ITEM IS ADDED TO AN EXISTING LOCATION.
#         THIS INFORMATION IS SAVED IN THE stock TABLE WITHIN THE SPECIFIED DATABASE.
#         
#         THREE VALUES ARE SAVED IN THE TABLE:
#             - ITEM SERIAL NUMBER/NAME
#             - LOCATION
#             - ITEM'S STOCK AT GIVEN LOCATION
#             
#         THE item, location, AND databaseName PARAMETERS SHOULD BE STRINGS. 
#         THE stock PARAMETER MUST BE AN INTEGER.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            # ADDS THE PASSED VALUES INTO THE inventory TABLE
            c.execute('''INSERT INTO stock VALUES(
                        :item,
                        :location,
                        :stock
                        )''', {
                        'item': item,
                        'location': location,
                        'stock': stock
                        })
    
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
                 
    def _update_item(self, desc, item, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW THE Database CLASS UPDATES ITEM INFORMATION.
#         
#         THE INFORMATION THAT CAN BE UPDATED IS THE ITEM'S DESCRIPTION.
#         
#         ALL ARGUMENTS SHOULD BE PASSED AS STRINGS.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            # UPDATES THE inventory TABLE WITHIN THE SPECIFIED DATABASE
            c.execute('''UPDATE inventory SET desc = :desc 
                      WHERE item = :item''', {
                                'desc': desc,
                                'item': item})
                      
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
            
    def _update_location(self, desc, location, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW THE Database CLASS UPDATES LOCATION INFORMATION.
#         
#         THE INFORMATION THAT CAN BE UPDATED IS THE LOCATION'S DESCRIPTION.
#         
#         ALL ARGUMENTS SHOULD BE PASSED AS STRINGS.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            # UPDATES THE locations TABLE WITHIN THE SPECIFIED DATABASE 
            c.execute('''UPDATE locations SET desc = :desc 
                      WHERE location = :location''', {
                    'desc': desc,
                    'location': location})
    
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
                      
    def _update_itemLocation(self, stock, item, location, databaseName):
# =============================================================================
#         THIS METHOD UPDATES THE INFORMATION FOUND WITHIN THE stock TABLE WITHIN
#         THE SPECIFIED DATABASE. 
#         
#         THE INFORMATION BEING UPDATED IS THE ITEM'S STOCK AT A SPECIFIED LOCATION.
#         
#         ALL ARGUMENTS SHOULD BE PASSED AS STRINGS, EXCEPT FOR stock, WHICH MUST
#         BE PASSED AS AN INTEGER.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            # UPDATES THE stock INFORMATION IN THE stock TABLE
            # USES BOTH item AND location TO FIND THE CORRECT ROW TO UPDATE
            c.execute('''UPDATE stock SET stock = :stock
                      WHERE item = :item AND location = :location''', {
                'stock': stock,
                'item': item,
                'location': location})
                      
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
    
    def _view_item(self, item, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW A USER CAN VIEW A SPECIFIC ITEM'S INFORMATION.
#         THIS METHOD CAN ALSO BE USED TO VERIFY IF THE ITEM IS WITHIN THE 
#         DATABASE'S INVENTORY.
#         
#         THE METHOD RETURNS THE INFORMATION IN THE FORM OF A TUPLE.
#         IF NO ITEM IS FOUND, THEN THE DATA TYPE None IS RETURNED. 
#         
#         ALL THE PARAMETERS SHOULD BE IN STRING FORMAT.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        # FINDS THE DATASET
        c.execute('''SELECT * FROM inventory 
                  WHERE item = :item 
                  ''',
                  {'item': item})
        
        # SAVES THE TUPLE LOCALLY
        dataSet =  c.fetchone()
    
        # CLOSES CONNECTION TO THE DATABASE
        conn.close()
        
        # IF A DATASET IS FOUND, THE dataSet RETURNS A TUPLE
        # ELSE IT RETURNS None
        return dataSet
    
    def _view_location(self, location, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW A USER CAN VIEW A SPECIFIC LOCATION'S INFORMATION.
#         THIS METHOD CAN ALSO BE USED TO VERIFY IF THE LOCATION IS WITHIN THE 
#         DATABASE'S locations TABLE.
#         
#         THE METHOD RETURNS THE INFORMATION IN THE FORM OF A TUPLE.
#         IF NO ITEM IS FOUND, THEN THE DATA TYPE None IS RETURNED. 
#         
#         ALL THE PARAMETERS SHOULD BE IN STRING FORMAT.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        # FINDS THE DATASET
        c.execute('''SELECT * FROM locations 
                  WHERE location = :location 
                  ''',
                  {'location': location})
        
        # SAVES THE TUPLE LOCALLY
        dataSet =  c.fetchone()
    
        # CLOSES CONNECTION TO THE DATABASE
        conn.close()
        
        # IF A DATASET IS FOUND, THE dataSet RETURNS A TUPLE
        # ELSE IT RETURNS None
        return dataSet
    
    
    def _view_itemLocation(self, item, location, databaseName):
# =============================================================================
#         THIS METHOD DEFINES HOW A USER CAN VIEW A SPECIFIC ITEM'S STOCK AT A
#         SPECIFIED LOCATION.
#         THIS METHOD CAN ALSO BE USED TO VERIFY IF THE ITEM CAN BE FOUND AT  
#         THAT LOCATION.
#         
#         THE METHOD RETURNS THE INFORMATION IN THE FORM OF A TUPLE.
#         IF NO ITEM IS FOUND, THEN THE DATA TYPE None IS RETURNED. 
#         
#         ALL THE PARAMETERS SHOULD BE IN STRING FORMAT.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        # FINDS THE DATASET
        c.execute('''SELECT * FROM stock
                  WHERE item = :item 
                  AND location = :location 
                  ''',
                  {'item': item,
                   'location': location})
        
        # SAVES THE TUPLE LOCALLY
        dataSet =  c.fetchone()
    
        # CLOSES CONNECTION TO THE DATABASE
        conn.close()
        
        # IF A DATASET IS FOUND, THE dataSet RETURNS A TUPLE
        # ELSE IT RETURNS None
        return dataSet
    
    
    def _view_all_inventory(self, databaseName):
# =============================================================================
#         THIS METHOD IS USED TO RETURN ALL INVENTORY INFORMATION WITHIN THE inventory TABLE.
#         THE INFORMATION IS SORTED WITHIN THE FUNCTION, AND IS RETURNED AS
#         TUPLES NESTED WITHIN A LIST. 
#         
#         FOR EXAMPLE: [('ITEM1', 'DESC1'), ('ITEM2', 'DESC2')]
#         
#         IF THERE IS NO INVENTORY, THEN None IS RETURNED. 
#         
#         ALL PARAMETERS SHOULD BE IN STRING FORMAT. 
# =============================================================================
        
        
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        # FINDS ALL ITEMS IN THE inventory TABLE AND SORTS THEM 
        # ALPHABETICALLY ACCORDING TO ITEM SERIAL NUMBER
        c.execute('''SELECT * FROM inventory 
                  ORDER BY item''')
        
        # SAVES THE LIST LOCALLY
        dataSet =  c.fetchall()
        
        # RETURNS THE DATASET. IF THERE ARE NO ITEMS, THEN None IS RETURNED
        return dataSet
    
    
    def _view_all_locations(self, databaseName):
# =============================================================================
#         THIS METHOD IS USED TO RETURN ALL LOCATION INFORMATION WITHIN THE locations TABLE.
#         THE INFORMATION IS SORTED WITHIN THE FUNCTION, AND IS RETURNED AS
#         TUPLES NESTED WITHIN A LIST. 
#         
#         FOR EXAMPLE: [('LOCATION1', 'DESC1'), ('LOCATION2', 'DESC2')]
#         
#         IF THERE ARE NO AVAILABLE LOCATIONS, THEN None IS RETURNED. 
#         
#         ALL PARAMETERS SHOULD BE IN STRING FORMAT.
# =============================================================================
        
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        
        # FINDS ALL ITEMS IN THE locations TABLE AND SORTS THEM 
        # ALPHABETICALLY ACCORDING TO LOCATION
        c.execute('''SELECT * FROM locations 
                  ORDER BY location''')
        
        # SAVES THE LIST LOCALLY
        dataSet =  c.fetchall()
        
        # RETURNS THE DATASET. IF THERE ARE NO LOCATIONS, THEN None IS RETURNED
        return dataSet
                      
    
        
    def _del_item(self, item, databaseName):
# =============================================================================
#         THIS METHOD DELETES A SPECIFIED ITEM WITHIN THE DATABASE IN BOTH THE 
#         inventory AND stock TABLES. 
#         
#         ALL PARAMETERS SHOULD BE PASSED AS STRINGS.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            
            # DELETES THE item FROM THE inventory TABLE
            c.execute('''DELETE FROM inventory WHERE item = :item''', 
                                                      {'item': item})
            
            # DELETES THE item FROM THE stock TABLE
            c.execute('''DELETE FROM stock WHERE item = :item''',
                                                  {'item': item})
        
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
        
    def _del_location(self, location, databaseName):
# =============================================================================
#         THIS METHOD DELETES A SPECIFIED LOCATION WITHIN THE DATABASE IN BOTH THE 
#         locations AND stock TABLES. 
#         
#         ALL PARAMETERS SHOULD BE PASSED AS STRINGS.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            
            # DELETES THE location FROM THE locations TABLE
            c.execute('''DELETE FROM locations WHERE location = :location''', 
                                                      {'location': location})
            
            # DELETES THE location FROM THE stock TABLE
            c.execute('''DELETE FROM stock WHERE location = :location''',
                                                  {'location': location})
        
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
        
    def _del_itemLocation(self, item, location, databaseName):
# =============================================================================
#         THIS METHOD DELETES A SPECIFIED ITEM AT ONE LOCATION WITHIN THE DATABASE IN 
#         stock TABLE. 
#         
#         ALL PARAMETERS SHOULD BE PASSED AS STRINGS.
# =============================================================================
        
        # CREATES THE FILE NAME BASED ON WHAT IS PASSED THROUGH
        database_name = databaseName + '.db'
        
        # OPENS THE CONNECTION TO THE DATABASE
        conn = sqlite3.connect(database_name)        
        c = conn.cursor()
        
        with conn:
            
            # DELETES THE item AND location COMBINATION FROM THE stock TABLE
            c.execute('''DELETE FROM stock WHERE item = :item AND
                                                      location = :location''', 
                                                      {'item': item, 
                                                       'location': location})
        
        # CLOSES THE CONNECTION TO THE DATABASE
        conn.close()
        