# -*- coding: utf-8 -*-

# MODULES CREATED AND IMPORTED
from baseFunctions import InputFunctions as bf
from database import Database as db

# PRE-BUILT MODULES IMPORTED
from dataclasses import dataclass

@dataclass
class main(bf, db):
# =============================================================================
#     THIS METHOD DEFINES THE MAIN FLOW AND LOGIC OF THE PROGRAM. IT INHERITS THE 
#     Database AND InputFuctions CLASSES FROM THE IMPORTED MODULES, WHICH WERE ALSO
#     CREATED. 
#     
#     THE MODULE dataclasses IS ALSO USED.  
# =============================================================================
    
    
    def main(self):
        # CREATES THE TABLES WITHIN THE INVENTORY SYSTEM
        # IF THE FILE DOESN'T EXIST, THEN A FILE IS CREATED
        db()._createTable('inventory')
        
        # INFORMS THE USER THAT THE PROGRAM HAS STARTED
        print('INVENTORY SYSTEM')
        
        # PUTS THE USER WITHIN A WHILE LOOP FOR THE MAIN MENU SYSTEM
        while True:
            
            # PRINTS THE OPTIONS FOR THE USER TO CHOOSE FROM
            print(
                '''MENU:
    1. ADD NEW ITEM/LOCATION
    2. UPDATE ITEM/LOCATION
    3. VIEW ITEM/LOCATION
    4. DELETE ITEM/LOCATION
    5. EXIT''')

            # ASKS THE USER TO CHOOSE AN OPTION            
            menuInput = bf().integerInput('MENU NUMBER')
            
            # MAIN MENU OPTION TO BRING USER TO 'ADD MENU'
            if menuInput == 1:
                
                
                while True:
                    # SHOWS THE USER THE POSSIBLE OPTIONS WITHIN THIS MENU
                    print(
                '''MENU:
    1. ADD ITEM
    2. ADD LOCATION
    3. ADD ITEM AT SPECIFIC LOCATION
    ''')
    
                    # ASK THE USER TO CHOOSE AN OPTION
                    addInput = bf().integerInput('MENU OPTION')
                
                    # ADD MENU OPTION TO ADD A NEW ITEM
                    if addInput == 1: 
                        while True:
                            
                            # ASKS FOR ITEM INFORMATION
                            item = bf().dataInput('ITEM SERIAL NUMBER').upper() 
                            desc = bf().baseInput('ITEM DESCRIPTION').upper()
                            
                            # SHOWS THE USER THE INFORMATION THAT THEY ENTERED
                            print('INFO ENTERED:')
                            print('ITEM SERIAL NUMBER:', item)
                            print('ITEM DESCRIPTION:', desc)
                            
                            # IF THE USER CONFIRMS THE INFORMATION, THEN THE ITEM IS ADDED
                            if bf().infoConfirmation():
                                db()._add_item(item, desc, 'inventory')
                               
                                # RETURNS THE USER TO THE MAIN MENU
                                break
                            
                            # IF THE USER DOES NOT WANT TO TRY AGAIN, NOTHING IS ADDED
                            # THE USER IS THEN SENT BACK TO THE MAIN MENU
                            elif not bf().tryAgain():
                                
                                # RETURNS THE USER TO THE MAIN MENU
                                break
                        
                        # RETURNS THE USER TO THE MAIN MENU     
                        break
                        
                    # ADD MENU OPTION TO ADD A NEW LOCATION
                    elif addInput == 2:
                        while True:
                            
                            # ASKS FOR LOCATION INFORMATION
                            location = bf().dataInput('LOCATION').upper() 
                            desc = bf().baseInput('LOCATION DESCRIPTION').upper()
                            
                            # SHOWS THE USER THE INFORMATION THEY ENTERED
                            print('INFO ENTERED:')
                            print('LOCATION:', location)
                            print('LOCATION DESCRIPTION:', desc)
                            
                            # IF THE USER CONFIRMS THE INFORMATION, THEN THE LOCATION IS ADDED
                            if bf().infoConfirmation():
                                db()._add_location(location, desc, 'inventory')
                                break
                            
                            # IF THE USER DOES NOT WANT TO TRY AGAIN, NOTHING IS ADDED
                            # THE USER IS THEN SENT BACK TO THE MAIN MENU
                            elif not bf().tryAgain():
                                break
                        
                        # RETURNS THE USER TO THE MAIN MENU
                        break
                    
                    # ADD MENU OPTION TO ADD AN EXISTING ITEM TO AN EXISTING LOCATION
                    elif addInput == 3:
                        # ASKS THE USER FOR THE ITEM
                        item = bf().dataInput('ITEM').upper()
                        
                        # CHECK IF THE ITEM EXISTS
                        item_check = db()._view_item(item, 'inventory')
                        if item_check == None:
                            
                            # IF THE ITEM DOES NOT EXIST, THEN THE USER IS NOTIFIED
                            # THEN THEY ARE SENT BACK TO THE MAIN MENU
                            print('THIS ITEM IS NOT ON THE INVENTORY LIST')
                            print('PLEASE ADD THE ITEM FIRST USING MENU OPTION 1')
                        
                        # CONTINUES TO ASK FOR LOCATION INFORMATION
                        else:
                            # ASKS USER FOR THE LOCATION
                            location = bf().dataInput('LOCATION').upper()
                            
                            # CHECKS TO SEE IF THE LOCATION EXISTS
                            location_check = db()._view_location(location, 'inventory')
                            if location_check == None:
                                
                                # IF THE LOCATION DOES NOT EXIST, THEN THE USER IS NOTIFIED
                                # THEN THEY ARE SENT BACK TO THE MAIN MENU 
                                print('THIS ITEM IS NOT ON THE LOCATION LIST')
                                print('PLEASE ADD THE LOCATION FIRST USING MENU OPTION 1')
                                
                            # CONTINUES TO FINAL CHECK
                            else:
                                
                                # CHECKS TO SEE IF THE ITEM ALREADY EXISTS IN THIS LOCATION
                                itemLocation_check = db()._view_itemLocation(item, location, 'inventory')
                                if itemLocation_check != None:
                                    # IF IT DOES ALREADY EXIST, THEN THE USER IS NOTIFIED AND SENT BACK TO THE MAIN MENU
                                    print('THIS ITEM HAS ALREADY BEEN ADDED TO THIS LOCATION')
                                    print('IF THE STOCK HAS CHANGED, PLEASE UPDATE THE INFORMATION '
                                          'THROUGH MAIN MENU OPTION 1')
                                
                                # IF ALL THE CHECKS ARE SUCCESFUL, THEN THE INFORMATION IS STORED
                                else:
                                    # ASKS THE USER FOR THE STOCK INFORMATION
                                    stock = bf().integerInput('ITEM STOCK AT LOCATION')                                
                                    
                                    # ADDS THE INFORMATION TO THE DATABASE
                                    db()._add_itemLocation(item, location, stock, 'inventory')  
                        
                        # RETURNS THE USER TO THE MAIN MENU
                        break
                    
                    # IF THE USER ENTERS AN INVALID INPUT                
                    else:
                        print('INVALID INPUT! PLEASE ENTER 1, 2, OR 3')
            
            # MAIN MENU OPTION TO BRING USER TO UPDATE MENU
            elif menuInput == 2:
                
                while True: 
                    # SHOWS USER THE POTENTIAL OPTIONS
                    print(
                '''MENU:
    1. UPDATE ITEM
    2. UPDATE LOCATION
    3. UPDATE ITEM STOCK AT SPECIFIC LOCATION
    ''')
                    # ASK USER FOR MENU CHOICE
                    updateInput = bf().integerInput('MENU OPTION')
                    
                    
                    # UPDATE MENU OPTION TO UPDATE AN ITEM DESCRIPTION
                    if updateInput == 1:
                        # ASKS USER WHICH ITEM'S INFORAMTION THEY WANT TO UPDATE
                        item = bf().dataInput('ITEM YOU WISH TO UPDATE').upper()
                        
                        # CHECKS TO SEE IF THE ITEM EXISTS
                        item_check = db()._view_item(item, 'inventory')
                        if item_check == None:
                            # IF IT DOES NOT EXIST, THE USER IS NOTIFIED AND SENT TO THE MAIN MENU
                            print('THIS ITEM IS NOT ON THE INVENTORY LIST')
                            print('PLEASE ADD THE ITEM FIRST USING MENU OPTION 1')
                            
                        
                        # IF THE ITEM DOES EXIST, THE INFORMATION IS UPDATED
                        else:
                            # ASKS THE USER FOR THE UPDATED ITEM DESCRIPTION
                            desc_updated = bf().dataInput('PLEASE ENTER THE NEW DESCRIPTION')
                            
                            # UPDATES THE INFORMATION
                            db()._update_item(desc_updated, item, 'inventory')
                            
                            # TELLS USER THAT THE ITEM HAS BEEN UPDATED
                            print('THIS ITEM\'S DESCRIPTION HAS BEEN UPDATED')
                        
                        # RETURNS THE USER TO THE MAIN MENU
                        break
                    
                    # UPDATE MENU OPTION TO UPDATE LOCATION DESCRIPTION INFORMATION
                    elif updateInput == 2:
                        # ASKS USER WHICH LOCATION'S INFORAMTION THEY WANT TO UPDATE
                        location = bf().dataInput('LOCATION YOU WISH TO UPDATE').upper()
                        
                        # CHECKS TO SEE IF THE LOCATION EXISTS
                        location_check = db()._view_location(location, 'inventory')
                        if location_check == None:
                            
                            # IF THE LOCATION DOES NOT EXIST, THEN THE USER IS NOTIFIED
                            # THE USER IS THEN SENT BACK TO THE MAIN MENU
                            print('THIS ITEM IS NOT ON THE LOCATION LIST')
                            print('PLEASE ADD THE LOCATION FIRST USING MENU OPTION 1')
                            
                        # IF THE LOCATION EXISTS, THEN THE INFORMATION IS UPDATED   
                        else:
                            # ASKS THE USER FOR THE NEW LOCATION DESCRIPTION
                            desc_updated = bf().dataInput('PLEASE ENTER THE NEW DESCRIPTION')
                            
                            # UPDATES THE LOCATION INFORMATION
                            db()._update_location(desc_updated, location, 'inventory')
                            
                            # NOTIFIES THE USER THAT 
                            print('THIS LOCATION\'S DESCRIPTION HAS BEEN UPDATED')
                       
                        # RETURNS THE USER TO THE MAIN MENU
                        break
                        
                    
                    # MENU OPTION TO UPDATE STOCK OF AN EXISTING ITEM AT A SPECIFIED EXISTING LOCATION
                    elif updateInput == 3:
                        # ASKS USER WHICH ITEM'S STOCK THEY WANT TO UPDATE
                        item = bf().dataInput('ITEM YOU WISH TO UPDATE').upper()
                        
                        # CHECKS TO SEE IF THE ITEM EXISTS
                        item_check = db()._view_item(item, 'inventory')
                        if item_check == None:
                            # IF THE ITEM DOES NOT EXIST, THE USER IS NOTIFIED AND SENT TO THE MAIN MENU
                            print('THIS ITEM IS NOT ON THE INVENTORY LIST')
                            print('PLEASE ADD THE ITEM FIRST USING MENU OPTION 1')
                            
                        # ELSE, THE LOCATION VALIDITY ID CHECKED
                        else:
                            # ASKS USER FOR THE LOCATION
                            location = bf().dataInput('LOCATION YOU WISH TO UPDATE').upper()
                            
                            # CHECK IF LOCATION EXISTS
                            location_check = db()._view_location(location, 'inventory')
                            if location_check == None:
                                #IF IT DOES NOT EXIST, THE USER IF NOTIFIED AND SENT BACK TO THE MAIN MENU
                                print('THIS ITEM IS NOT ON THE LOCATION LIST')
                                print('PLEASE ADD THE LOCATION FIRST USING MENU OPTION 1')
                                
                            
                            # CONTINUES TO FINAL CHECK
                            else:
                                
                                # CHECKS TO SEE IF THE ITEM EXISTS IN THIS LOCATION
                                itemLocation_check = db()._view_itemLocation(item, location, 'inventory')
                                if itemLocation_check == None:
                                    # IF IT DOES NOT EXIST, THEN THE USER IS NOTIFIED AND SENT BACK TO THE MAIN MENU
                                    print('THIS ITEM DOES NOT IN THIS LOCATION')
                                    print('PLEASE ADD THE ITEM FIRST THROUGH MAIN MENU OPTION 1')
                                
                                # IF ALL THE CHECKS ARE SUCCESFUL, THEN THE INFORMATION IS UPDATED
                                else:
                                    # ASKS USER FOR UPDATED STOCK
                                    stock_updated = bf().dataInput('PLEASE ENTER THE STOCK')
                                    
                                    # UPDATES THE INFORMATION
                                    db()._update_itemLocation(stock_updated, item, location, 'inventory')
                        
                        # RETURNS THE USER TO THE MAIN MENU
                        break
                    
                    # IF THE USER ENTERS INVALID INPUT
                    else:
                        print('INVALID INPUT! PLEASE ENTER 1, 2, OR 3')
                        
            # MAIN MENU OPTION TO BRING USER TO THE VIEW MENU            
            elif menuInput == 3:
                
                while True:
                    # SHOWS THE USER THE AVAILABLE OPTIONS
                    print(
                '''MENU:
    1. VIEW ITEM
    2. VIEW LOCATION
    3. VIEW ITEM STOCK AT SPECIFIC LOCATION
    4. VIEW ALL ITEMS
    5. VIEW ALL LOCATIONS
    ''')
                    # ASKS THE USER TO CHOOSE AN OPTION
                    viewInput = bf().integerInput('MENU OPTION')
                    
                    # MENU OPTION TO VIEW AN ITEM IN THE INVENTORY 
                    if viewInput == 1:
                        
                        # ASKS THE USER WHICH ITEM THEY WISH TO VIEW
                        item = bf().dataInput('ITEM YOU WISH TO VIEW').upper()
                        
                        # RETIREVES INFORMATION
                        item_set = db()._view_item(item, 'inventory')
                        
                        # IF THE ITEM DOESN'T EXIST, THE USER IF NOTIFIED AND SENT ABCK TO THE MAIN MENU
                        if item_set == None:
                            print('THIS ITEM IS NOT ON THE INVENTORY LIST')
                            print('PLEASE ADD THE ITEM FIRST USING MENU OPTION 1')
                            
                        # ELSE THE INFORMATION IS PRINTED   
                        else:
                            print('ITEM SERIAL NUMBER:', item_set[0])
                            print('ITEM DESCRIPTION:', item_set[1])
                        
                        # RETURNS USER TO MAIN MENU
                        break
                     
                    # MENU OPTION TO VIEW AN EXISTING LOCATION
                    elif viewInput == 2:
                        
                        # ASKS USER WHICH LOCATION THEY WISH TO VIEW
                        location = bf().dataInput('LOCATION YOU WISH TO VIEW').upper()
                        
                        # RETRIEVES INFORMATION
                        location_set = db()._view_location(location, 'inventory')
                        
                        # IF THE LOCATION DOESN'T EXIST, THE USER IS NOTIFIED
                        # THEN THEY ARE SENT BACK TO THE MAIN MENU
                        if location_set == None:
                            print('THIS LOCATION IS NOT ON THE LIST OF LOCATIONS')
                            print('PLEASE ADD THE LOCATION FIRST USING MENU OPTION 1')
                            
                        # ELSE THE INFORMATION IS DISPLAYED   
                        else:
                            print('LOCATION:', location_set[0])
                            print('LOCATION DESCRIPTION:', location_set[1])
                        
                        # RETURNS USER TO MAIN MENU
                        break
                            
                    # MENU OPTION TO SEE STOCK OF ITEM AT A SPECIFIED EXISTING LOCATION        
                    elif viewInput == 3:
                        
                        # ASKS USER FOR THE ITEM THEY WISH TO VIEW
                        item = bf().dataInput('ITEM YOU WISH TO VIEW').upper()
                        
                        # CHECKS IF THE ITEM EXISTS
                        item_check = db()._view_item(item, 'inventory')
                        if item_check == None:
                            
                            # IF IT'S NOT IN THE INVENTORY, THE USER IS NOTIFIED AND SENT TO THE MAIN MENU
                            print('THIS ITEM IS NOT ON THE INVENTORY LIST')
                            print('PLEASE ADD THE ITEM FIRST USING MENU OPTION 1')
                        
                        # CONTINUES TO THE LOCATION CHECK
                        else:
                            # ASKS USER FOR THE LOCATION
                            location = bf().dataInput('LOCATION OF THE ITEM').upper()
                            
                            # IF THE LOCATION DOES NOT EXIST, THE USER IS NOTIFIED
                            # THEY ARE THEN SENT BACK TO THE MAIN MENU
                            location_check = db()._view_location(location, 'inventory')
                            if location_check == None:
                                print('THIS LOCATION IS NOT ON THE LOCATION LIST')
                                print('PLEASE ADD THE LOCATION FIRST USING MENU OPTION 1')
                            
                            # BOTH CHECKS ARE PASSED, RETIREVES INFORMATION FROM stock TABLE
                            else:
                                
                                # RETRIEVES INFORMATION
                                stock_set = db()._view_itemLocation(item, location, 'inventory')
                                
                                # IF THERE IS NO INFORMATION, THE USER IS NOTIFIED AND SENT BACK TO TEH MAIN MENU
                                if stock_set == None:
                                    print('ITEM DOES NOT EXIST IN THIS LOCATION')
                                    print('TO ADD THIS ITEM TO THIS LOCATION, USE MENU OPTION 1')
                                
                                # ELSE THE INFORMATION IS PRINTED
                                else:
                                    print('ITEM SERIAL NUMBER:', stock_set[0])
                                    print('LOCATION:', stock_set[1])
                                    print('STOCK:', stock_set[2])
                        
                        # RETURNS USER TO MAIN MENU
                        break
                    
                    # MENU OPTION TO SEE ALL ITEMS IN THE INVENTORY
                    elif viewInput == 4:
                        
                        # RETRIEVES ALL AVAILABLE INVENTORY INFORMATION
                        all_inventory = db()._view_all_inventory('inventory')
                
                        # IF THE INVENTORY IS EMPTY, THE USER IS NOTIFIED AND SENT BACK TO THE MAIN MENU
                        if all_inventory == None:
                            print('THE DATABASE IS EMPTY')
                        
                        # ELSE THE INFORMATION IS PRINTED
                        else:
                            item_list = [item[0] for item in all_inventory]
                            desc_list = [item[1] for item in all_inventory]
                            
                            for i in range(len(item_list)):
                                print(f'- {item_list[i]}\t\tDESCRIPTION: {desc_list[i]}')
                                
                        # RETURNS USER TO MAIN MENU
                        break
                                
                    # MENU OPTION TO SEE ALL LOCATION AVAILABLE            
                    elif viewInput == 5:
                        
                        # RETIREVES ALL AVAILABLE LOCATION INFORMATION
                        all_locations = db()._view_all_locations('inventory')
                
                        # IF THE TABLE IS EMPTY, THEN THE USER IS NOTIFIED AND SENT ABCK TO THE MAIN MENU
                        if all_locations == None:
                            print('THE DATABASE IS EMPTY')
                          
                        # ELSE THE INFORMATION IS PRINTED
                        else:
                            location_list = [item[0] for item in all_locations]
                            desc_list = [item[1] for item in all_locations]
                            
                            for i in range(len(location_list)):
                                print(f'- {location_list[i]}\t\tDESCRIPTION: {desc_list[i]}')
                                
                        # RETURNS USER TO MAIN MENU
                        break
                    
                    # IF THE USER ENTERS INVALID INPUT
                    else:
                        print('INVALID INPUT! PLEASE ENTER 1, 2, 3, 4, OR 5')
                
            # MAIN MENU OPTION TO BRING USER TO THE DELETE MENU
            elif menuInput == 4:
                
                while True:
                    
                    # SHOWS USER WHAT THEIR OPTIONS ARE
                    print('WHAT WOULD YOU LIKE TO DELETE?')
                    print(
                '''MENU:
    1. DELETE ITEM
    2. DELETE LOCATION
    3. DELETE ITEM AT SPECIFIC LOCATION
    ''')
    
                    # ASKS USER TO CHOOSE AN OPTION                
                    deleteInput = bf().integerInput('MENU OPTION')
                    
                    # TO DELETE AN ITEM
                    if deleteInput == 1:
                       # ASKS USER WHICH ITEM THEY WANT TO DELETE
                       item = bf().dataInput('ITEM SERIAL NUMBER').upper()
                       
                       # DELETES ITEM
                       db()._del_item(item, 'inventory')
                       
                       # NOTIFIES USER
                       print('ITEM HAS BEEN DELETED')
                       
                       # RETURNS USER TO MAIN MENU
                       break
                       
                    elif deleteInput == 2:
                        # ASKS USER WHICH LOCATION THEY WISH TO DELETE
                        location = bf().dataInput('LOCATION').upper()
                        
                        # DELETES LOCATION
                        db()._del_location(location, 'inventory')
                        
                        # NOTIFIES USER
                        print('LOCATION HAS BEEN DELETED')
                        
                        # RETURNS USER TO MAIN MENU
                        break
                        
                    elif deleteInput == 3:
                        # ASKS USER WHICH ITEM AT WHICH LOCATION THEY WISH TO DELETE 
                        item = bf().dataInput('ITEM SERIAL NUMBER').upper()
                        location = bf().dataInput('AT WHICH LOCATION').upper()
                        
                        # DELETES THE INFORMATION
                        db()._del_itemLocation(item, location, 'inventory')
                        
                        # NOTIFIES THE USER
                        print('ITEM AT SPECIFIED LOCATION HAS BEEN DELETED')
                        
                        # RETURNS USER TO MAIN MENU
                        break
                    
                    # FOR INVALID USER INPUT
                    else:
                        print('INVALID INPUT, TRY AGAIN')
                
            # IF THE USER WISHES TO END THE PROGRAM
            elif menuInput == 5:
                print('EXITING PROGRAM')
                break
            
            # IF THE USER ENTERS INVALID INPUT
            else:
                print('INVALID INPUT, TRY AGAIN')
                        
                        
# TEST OBJECT CREATED       
test = main()
test.main()