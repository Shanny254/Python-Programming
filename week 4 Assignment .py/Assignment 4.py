# Ask the user for both the input filename and the output filename
input_filename = input("Enter the filename to read: ")
output_filename = input("Enter the filename to save modified content: ")

try:
    # Open and read the file
    with open(input_filename, 'r') as f:
        content = f.read()

    # Modify content (e.g., make all text uppercase)
    modified = content.upper()

    # Write the modified content to the user-specified output file
    with open(output_filename, 'w') as f:
        f.write(modified)

    print(f"✅ File read successfully and modified content saved in '{output_filename}'.")

except FileNotFoundError:
    print("❌ File not found. Please check the filename and try again.")
except Exception as e:
    print("❌ An error occurred:", e)
