application = [
    "Google - System Design",
    "Amazon - AI Integration",
    "Microsoft - Backend Dev",
    "X - Frountend dev",
    "Golden Seacs - Devops"
]
print("MY JOB APPLICATIONS: ")
print("-"*30)

for n in application:
  print(f". {n}")

new = input("Enter New Application: ")
application.append(new)

re = input("Enter Application That you want to remove(Full name): ")

found = None
for app in application:
  if app.lower()== re.lower():
    found = app
    break
  
if found:
  application.remove(re)
else:    
  print("Not Found!")

count=0
for n in application:
  if "Google" in n:
     count +=1
print(f"Google Application in List is {count}")

print("Final Total List: ")
for n in application:
  print(f". {n}")

