# home work 5, task 2

finish_number = int(input("Please type your finish number for Sequence of Fibonacci "))
sequence_of_fibonacci = [0, 1, ]

while sequence_of_fibonacci[-1] < finish_number:
    sum = sequence_of_fibonacci[-1] + sequence_of_fibonacci[-2]
    sequence_of_fibonacci.append(sum)

sequence_of_fibonacci.pop(-1)
print(sequence_of_fibonacci)