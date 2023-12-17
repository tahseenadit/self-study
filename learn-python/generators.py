"""
Use case 1: 

Reading large files: You can use a generator function
to read a large file line by line without loading the 
whole file into memory.

----------------------------------------------------
"""

def csv_read(file_name):
    file = open(file_name)
    for row in file:
        yield row

"""
Use case 2: 

Infinite sequences: You can use a generator function
to generate infinite sequence of numbers.

----------------------------------------------------
"""

def infiniteSequence():
    n = 1
    while n:
        yield n
        n = n+1

if __name__ == "__main__":

    # Use case 1

    file = "../test_resources/data.csv"
    csv_generator_obj = csv_read(file)
    for row in csv_generator_obj:
        print(row)

    # Use case 2

    infinite_sequence_gen_obj = infiniteSequence()

    for item in infinite_sequence_gen_obj:
        print(item)



