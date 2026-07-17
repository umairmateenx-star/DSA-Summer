applications=[
    {"company":"Google", "role":"SWE", "status":"Applied"},
    {"company":"Amazon", "role":"ML", "status":"Applied"},
    {"company":"Apple", "role":"Front Eng", "status":"No"},
    {"company":"X", "role":"Backend Eng", "status":"Applied"}
]

for n in applications:
    print(f"{n['company']} - {n['role']} - {n['status']}")

count=0
for n in applications:
    if 'Applied' in n["status"]:
     count += 1
print(f"Number of companies Applied to {count}")

c = input("Enter Company: ")
r = input("Enter Role: ")
s = input("Enter Status: ")

n = {"company": c, "role": r, "status": s}
applications.append(n)

for n in applications:
    print(f"{n['company']} - {n['role']} - {n['status']}")
