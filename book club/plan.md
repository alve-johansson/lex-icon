"Build a Python program called libary.py that manages a book club’s library using MongoDB and pymongo through a text-based menu.
 
Members should have a name and a unique email address. Books should have a title, author, genres, and number of copies. Members should be able to borrow books for 14 days and review books they have previously borrowed and returned.
 
Start by describing your database design in a comment, explaining and justifying which data you choose to embed and which data you choose to reference.
 
Add schema validation, indexes, and a menu option for generating test data.
 
The program should allow users to search for books, borrow and return books, view member profiles, and display overdue loans.
 
A member may borrow a maximum of 3 books at a time and must not be allowed to borrow any additional books if they have an overdue loan. The number of available copies must never become negative, and you must ensure this using a single database update operation.
 
Use MongoDB aggregation pipelines to generate reports, such as the most frequently borrowed books and the average rating for each book.
 
The program must handle invalid user input without crashing, and user input must never be inserted directly into a database query filter."


## PLAN 

I will try to reuse code, for both menu and DB.

As for the structure of the DB, I'm thinking that the main collections should probably be that of Members, Books and Loans. This is the logic of the webshop we used in the NOSQL assignments. Which makes it easy to recycle code.

### MEMBERS
The Members collection should have name and as defined a unique email. This could thus be used as a id.

### BOOKS
The Books collection should include title, author(s), genre(s), and copies. Neither of these is a unique value, and thus some kind of _id is needed.

### LOANS
For each instance in the Loans collection, to be included should be ONE reference to one member (unique) and ONE reference to an instance in the Books collection.

### RATINGS
The rating references just as Loans, ONE reviewer(a Member) and ONE reviewed(a Book).Embedded information could be a rating 0-5 stars, and a text comment section. A review is as much a part of the reviewer as the reviewee.

##### MODULES:

## MAIN
For interface: menu, input and output, etc.

## DB
For communications with MongoDB.

## LOGICS
For bussiness logics. For example checks if member is allowed more loans, if there are loans over due. Validates data before sending it to DB.