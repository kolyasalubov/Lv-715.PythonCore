#hm

philosophy_str = "Beautiful is better than ugly. Explicit is better than implicit.Simple is better than complex.Errors should never pass silently.Now is better than never ."
philosophy_str1 = philosophy_str.split()
n1 = philosophy_str1.count("better")
n2 = philosophy_str1.count("never")
n3 = philosophy_str1.count("is")
print(f"There are {n1} \"better\" , {2} \"never\" and {3} \"is\" in this string .")
print("Display all text in upper case :\n",philosophy_str.upper())
print("Replace all occurrences of the symbol “and” with “&” :\n", philosophy_str.replace("i" , "&"))
#task 2.1
number = int(input("Enter a 4-digit number: "))
n1 = number % 10
n2 = (number // 10) % 10
n3 = (number // 100) % 10
n4 = (number // 1000) % 10
print("Result : " ,n1*n2*n3*n4)

#task 2.2
number = str(input("Enter a number : "))
print(number[::-1])

# task 2.3
number = list((input("Enter a number : ")))
print(sorted(number))