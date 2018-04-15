if __name__ == '__main__':
    # Initialize list
    list = []
    # Get the number of commands that we have to run
    number_of_commands = input()
    # Iterate through the inputs line by line
    # The underscore here is just a throaway variable
    # You could use the usual i variable but it won't change anything
    for _ in range(int(number_of_commands)):
        # Get the input, split method returns a list
        # Ex. ['insert', '0', '5']
        stringInput = input().split()
        # Get the first item in the stringInput variable
        command = stringInput[0]
        # Get the arguments from index 1 to end
        arguments = stringInput[1:]
        # Self explanatory
        if command != 'print':
            # Combine the command with arguments
            # The join method takes a list of strings
            # and combines it with a sepator which
            # in this case is ","
            command += "(" + ",".join(arguments) + ")"
            # Execute the formed command
            # The eval method takes a string to execute
            eval("list." + command)
        else:
            print(list)