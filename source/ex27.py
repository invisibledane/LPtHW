print("Let's look at some conditionals.")

evaluation_statements = [ "1 != 0", "1 != 1", "0 != 1", 
 "0 != 0", "1 == 0", "1 == 1", "0 == 1", "0 == 0" ]

for statement in evaluation_statements:
    print(f"Does {statement}? Answer: {eval(statement)}")

print("\nDone. Press any key to continue ...")
input()