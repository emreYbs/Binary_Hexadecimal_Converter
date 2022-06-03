#!/bin/bash
#EmreYbs
#Binary_Hexadecimal_Converter

from halo import Halo
import time

spinner = Halo(text="Binary/Hexadecimal Converter App",spinner="dots",color="cyan")
spinner.start("\n Beginning...")
time.sleep(1)
spinner.stop()

#Get user input and generate lists.
spinner.text = 'Welcome to the Binary/Hexadecimal Converter App'
max_value = int(input("\tLet's compute the binary and hexadecimal values up to the following decimal number:  "))
decimal = list(range(1, max_value+1))
binary = []
hexadecimal = []

for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Generating lists...")
spinner.succeed("\nFinished....")


spinner.info("\n\tSlicing index from user...")
spinner.text = "\nUsing slices, we will now show a portion of each list.\n"
lower_range = int(input("\n\tWhat decimal number would you like to start at: \n"))
upper_range = int(input("\tWhat decimal number would you like to stop at: "))


spinner.info("\n\tNow...Slicing through each list individually...")
print("\nDecimal values from " + str(lower_range) + " to " + str(upper_range) + ":")

for num in decimal[lower_range-1:upper_range]:
    print(num)

print("\nBinary values from " + str(lower_range) + " to " + str(upper_range) + ":")

for num in binary[lower_range-1:upper_range]:
    print(num)

print("\nHexadecimal values from " + str(lower_range) + " to " + str(upper_range) + ":")

for num in hexadecimal[lower_range-1:upper_range]:
    print(num)


spinner.start("\nOutputting the whole list to the screen...\n")
time.sleep(1)
spinner.stop()
input("\nPress Enter to see all values from 1 to " + str(max_value) + ".")
spinner.start()
print ("\nProcessing your request in this order: Decimal - Binary -Hexadecimal")
time.sleep(2)
spinner.stop()
spinner.succeed("Finished....")
print("\nDecimal----Binary----Hexadecimal\n")
print("------------------------------------")


for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d) + "----------" + str(b) + "----------" + str(h))

spinner.start()
spinner.info("Converted...")
spinner.succeed("Finished all tasks.")
time.sleep(1)
spinner.succeed("A Simple Binary/Hexadecimal Converter App by EmreYbs")
spinner.stop()

