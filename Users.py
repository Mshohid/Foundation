Current_Users = ["Jake", "Forever101", "Legend3", "Ement", "DragonSlayer22"]
New_Users = ["jake", "Jakkson", "Wander", "Reckless", "HiroWiro"]

Current_Users_lower = []
for user in Current_Users:
   Current_Users_lower.append(str.lower(user))

New_Users_lower = []
for new_user in New_Users:
    New_Users_lower.append(str.lower(new_user))

for New_User in New_Users_lower:
    if New_User in Current_Users_lower:
       print(" Sorry Please Enter A New Username.\n The Username " + New_User + " Has Been Taken.")
    else:
       print("The Username " + New_User + " Is available for use.")