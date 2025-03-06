def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"
    finally:
        ("Finished reading file.")

"""Imagine you have a function that reads data from a file and then 
divides two numbers provided within that file. There are some faults in
it that you can catch with exceptions."""
def faulty_read_and_divide(filename):
	with open(filename, 'r') as file:
		data = file.readlines()
		num1 = int(data[0])
		num2 = int(data[1])
		return num1 / num2
# To address these potential issues, you can add the appropriate 
# exception handling illustrated below:

def enhanced_read_and_divide(filename):
     try:
          with open(filename, "r") as file:
               data = file.readlines()
          #Ensure there are at least two lines in the file
          if len(data) < 2:
               raise ValueError("Not enough data in the file.")
          
          num1 = int(data[0])
          num2 = int(data[1])

          # check if second number is zero
          if num2 == 0:
               raise ZeroDivisionError("The denominator is zero.")
          return num1 / num2
     except FileNotFoundError:
          return "Error: The file was not found."
     except ValueError as ve:
          return f"Value error: {ve}"
     except ZeroDivisionError as zde:
          return f"Division error: {zde}"

