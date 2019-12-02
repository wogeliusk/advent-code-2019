import math

def main():

    infile = open("input.dat", "r")
    masses = infile.readlines()
    fuel_needed = 0

    for item in masses:
        result = math.floor(int(item) / 3) - 2
        fuel_needed += result 

    print(fuel_needed)

if __name__ == "__main__":
    main()
