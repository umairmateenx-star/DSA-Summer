def show_all(appl):
   print("-"*20)
   for n in appl:
      print(f"{n['company']} - {n['role']} - {n['status']}")

def add_ap(appl):
   print("-"*20)
   c=input("Enter Company: ")
   r=input("Enter Role: ")
   s=input("Enter Status: ")
   n={"company":c, "role": r, "status": s}
   appl.append(n)

   print(f"Added: {c} - {r} - {s}")

def remove(appl):
   print("-"*20)
   r=input("Enter Company to Remove: ")
   found=False
   for n in appl:
    if n["company"].lower() == r.lower():
      appl.remove(n)
      print(f"Remove: {r["company"]}")
      found=True
      break
   if not found:
      print("Company not found!") 

def status(appl, status):
   count=0
   for n in appl:
     if n["status"] == "Applied":      
      count += 1
   print(f"Total Companies Applied to: {count}")


  
def main():
    applications = [
        {"company": "Google", "role": "SWE", "status": "Applied"},
        {"company": "Amazon", "role": "ML", "status": "Applied"},
        {"company": "Apple", "role": "Front Eng", "status": "No"},
        {"company": "X", "role": "Backend Eng", "status": "Applied"}
    ]
    while True:
        print("-"*20)
        print("Application Tracker")
        print("1. Display All Applications")
        print("2. Add New Applications")   
        print("3. Remove Application")
        print("4. Count by Status")
        print("5. Exit")
        print("-"*20)

        choice = input("Enter Your Choice (1-5):")

        if choice == "1":
         show_all(applications)  
        elif choice == "2":
         add_ap(applications)
        elif choice == "3":
         remove(applications)
        elif choice == "4":
         status(applications,"Applied")
        elif choice == "5":
         break
        else:
           print("Invalid Choice! Enter Again from 1-5.") 
                            
if __name__ == "__main__":
    main()