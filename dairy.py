#!/usr/bin/env python3
from peewee import * 
import sys 
from collections import OrderedDict  # its a library that holds extra container types .. like dicts , sets , list .. etc 
import datetime
db= SqliteDatabase('dairy1.db')


class Entry(Model):
    content=TextField()
    timestamp=DateTimeField(default=datetime.datetime.now)
     
    
    
 
    
    class Meta:
        database = db 
        

        
def initialize():
    """Create the database and the table if they dont exist."""

    db.connect()
    db.create_tables([Entry], safe=True)
    
    
def menu_loop():
    """Show the menu"""
    choice = None 
    
    while choice != 'q':
        print("enter 'q' to quit ")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()
        
        if choice in menu:
            menu[choice]()   # we get the value from the coice taken ..
                            #where the value is a function name .. and here using the () we run it
    
    
def add_entry():
    """Add an entry"""
    print("enter your entry , press ctrl + d when finished . ")
    data = sys.stdin.read().strip()
    
    if data:
        if input('Save entry? [Yn]').lower() !='n':
            Entry.create(content=data)
            print("saved sucessfully! ")
            
    
    
    
def view_entries():
    """view previous entries"""
    entries = Entry.select().order_by(entry.timestamp.desc())

    for entry in entries:
	timestamp = entry.timestamp.strftime('%A %B %d %Y %I:%M%p')  # refer the strtime() in the docs to understand what the %A %d ...etc actually is
	print(timesamp)
	print('='+len(timestamp))
	print('N) next entry')
	print('q) return to main menu')

	next_action = input('action: [nq] ').lower().strip()
	if next_action =='q'
	    break

        
def delete_entry(entry):
    """Delete an entry"""
    
menu = OrderedDict([
        ('a', add_entry),
        ('v', view_entries),
    ])
    
    
if __name__ == '__main__':
    initialize()
    menu_loop()
