applications=[
    {"company":"Google", "role":"SWE", "status":"Applied"},
    {"company":"Amazon", "role":"ML", "status":"Applied"},
    {"company":"Apple", "role":"Front Eng", "status":"No"},
    {"company":"X", "role":"Backend Eng", "status":"Applied"}
]
# Menu
while True:
 print("Menu")
 print("-"*20)
 print("1. Display All")
 print("2. Check Applied Status")
 print("3. Search Company")
 print("4. Add New Applications")
 print("5. Total Application")
 print("6. Exit")
 print("-" * 20)

 v= input("Enter Your Choice (1-6): ")

 if v == "1":
 # Display all
  for n in applications:
   print(f"{n['company']} - {n['role']} - {n['status']}")

  print("-"*30)
 elif v == "2":
  # check Applied Status
  count=0
  for n in applications:
    if 'Applied' in n["status"]:
     count += 1
     print(f"Applied to {n['company']}")
    else:
       print(f"Company Not Applied to {n['company']}") 
  print(f"Number of companies Applied to {count}")
 elif v=="3":
  #Search Company
  print("-"*30)                  
  x=input("Search Company Name (Y/N)")
  if x.lower() == 'y':
   search = input("Company: ")
  found = False
  for n in applications:
    if search.lower() in n["company"].lower():
       print(f"{n['company']} - {n['role']} - {n['status']}")
       found = True
       print(f" No company found with '{search}'")
    else:
        print("Search cancelled")

 elif  v=="4":
 #Add new applications
  c = input("Enter Company: ")
  r = input("Enter Role: ")
  s = input("Enter Status: ")

  n = {"company": c, "role": r, "status": s}
  applications.append(n)
  print(f"Added: {c} - {r} - {s}")
 elif  v=="5":
 #Total Application
  total=0
  print("-"*30)
  for n in applications:
    total +=1
    print(f"{n['company']} - {n['role']} - {n['status']}")

  print(f"Total Applications: {total}")
 elif  v=="6":
    break
 else:
    print("Enter Again")