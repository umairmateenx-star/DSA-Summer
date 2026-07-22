class applications:

    def __init__(self, company, role, status):
        self.company = company
        self.role = role
        self.status = status

    def __str__(self):
        return f"{self.company} - {self.role} - {self.status}"
    
class apptracker:

    def __init__(self):
        self.applications = []

    def add(self, company, role, status = "Applied"):
        app = applications(company, role, status)
        self.applications.append(app)
        print(f"Added {company} - {role} - {status}")

    def display(self):
        print("All Applications")
        print("-"*20)
        for n in self.applications:
            print(n)           
    
    def count(self, status):
        c = 0
        for n in self.applications:
            if n.status.lower() == status.lower():
                c += 1
        print(f"Number of Applied: {c}")

    def remove(self, company):     
        found = False
        for n in self.applications:
            if n.company.lower() == company.lower():
                self.applications.remove(n)
                print(f"{company} Removed!")
                found = True
                break
            if not found:
                print("Not Found!")      

t1 = apptracker()

t1.add("Google", "SWE Intern", "Applied")
t1.add("Microsoft", "Backend Developer", "Interview")
t1.add("Amazon", "ML Engineer", "Applied")
t1.add("Apple", "Frontend Developer", "Rejected")

while True:
 print("Menu")
 print("-"*20)
 print("1. Display All")
 print("2. Add New Applications")
 print("3. Check Applied Status")
 print("4. Remove")
 print("5. Exit")
 print("-" * 20) 
 n =input("Enter Key between (1-5):")

 if n == "1":
    t1.display()
 
 elif n == "2":       
    c = input("Enter Company: ")
    r = input("Enter Role: ")
    s = input("Enter Status: ")

    t1.add(c,r,s)
 elif n == "3":
        t1.count("Applied")
 elif n == "4":
        x = input("Enter Name: ") 
        t1.remove(x)    
 elif n == "5":
        break
 else:
     print("Enter Again From 1-5")
