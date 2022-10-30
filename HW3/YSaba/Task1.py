#HW2 , task 1
philosophy_str = "Beautiful is better than ugly. Explicit is better than implicit.Simple is better than complex.Errors should never pass silently.Now is better than never ."
philosophy_str1 = philosophy_str.split()
n1 = philosophy_str1.count("better")
n2 = philosophy_str1.count("never")
n3 = philosophy_str1.count("is")
print(f"There are {n1} \"better\" , {2} \"never\" and {3} \"is\" in this string . \n")
print("Display all text in upper case :\n",philosophy_str.upper())
print("Replace all occurrences of the symbol “and” with “&” :\n", philosophy_str.replace("i" , "&"))
