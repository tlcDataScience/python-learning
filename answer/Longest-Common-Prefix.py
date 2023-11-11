# Input array of strings
strs = ["flower", "flow", "flight"]

# Check if the input array is empty
if not strs:
    common_prefix = ""
else:
    # Sort the strings to make it easier to find the common prefix
    strs.sort()

    # Take the first and last string in the sorted array
    first_str = strs[0]
    last_str = strs[-1]

    # Find the common prefix between the first and last string
    common_prefix = []
    for i in range(len(first_str)):
        # Check if the current character is the same in both strings
        if i < len(last_str) and first_str[i] == last_str[i]:
            # Add the current character to the common prefix
            common_prefix.append(first_str[i])
        else:
            # If characters are not the same, break out of the loop
            break

# Join the characters in the common prefix list into a single string
result = ''.join(common_prefix)

# Print the result
print(result)
