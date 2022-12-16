class BookStore:
    NoOfBooks=0
    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        #print(self.NoOfBooks)
        BookStore.NoOfBooks += 1
    def Display(self):
        print(self.Name,self.Author)

Name=(input("Enter the name:"))
Author=(input("Name of Author:"))
obj1=BookStore(Name,Author)
obj1.Display()
print("No of Books",obj1.NoOfBooks)
Name=(input("Enter the name:"))
Author=(input("Name of Author:"))
obj2=BookStore(Name,Author)
obj2.Display()
print("No of Books",obj2.NoOfBooks)