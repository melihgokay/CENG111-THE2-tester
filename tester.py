import time
t1 = time.time()
import os
import sys


correct_values = 0
progress = 0


os.system("python3 the2.py <inputs.txt> your_outputs.txt")


with open("your_outputs.txt") as your_outputs, open("outputs.txt") as correct_outputs:
    for your_output, correct_output in zip(your_outputs, correct_outputs):

        progress += 1

        if your_output == correct_output:
            correct_values += 1

        else:
            print("Correct output:", correct_output, end='')
            print("Your output:", your_output)


sys.stdout.write("\n")
os.remove("your_outputs.txt")


t2 = time.time()


print(str(progress) + ' test cases implemented')
print("Execution time is:", str(t2 - t1) + ' seconds')
print(str(correct_values) + " out of 160000 outputs are correct")