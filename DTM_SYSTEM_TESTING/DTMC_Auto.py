import subprocess
import glob
import shutil
import os

# Get a list of XML files in the directory
xml_files = glob.glob("ExpectedOperation_*.xml")

# Loop over the XML files
for xml_file in xml_files:
    command1 = f"python3 classifier.py -f {xml_file} -o DTMC_{xml_file[17:-4]}.csv"

    # Run the first command in the terminal
    process1 = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout1, stderr1 = process1.communicate()

    # Check if any error occurred during execution
    if process1.returncode != 0:
        print(f"An error occurred while executing command 1 for {xml_file}:")
        print(stderr1.decode("utf-8"))
    else:
        print(f"Command 1 executed successfully for {xml_file}!")

    # Generate 10 copies of the CSV file
    for i in range(1, 11):
        csv_file = f"DTMC_{xml_file[17:-4]}_{i}.csv"
        shutil.copy(f"DTMC_{xml_file[17:-4]}.csv", csv_file)
        print(f"Copy {i} created: {csv_file}")

    # Get a list of CSV files for the current XML file
    csv_files = glob.glob(f"DTMC_{xml_file[17:-4]}*.csv")

    # Loop over the CSV files and execute command2 to generate simout files
    for csv_file in csv_files:
        simout_file = csv_file.replace(".csv", "_simout.csv")
        command2 = f"python3 TMsim.py -f {csv_file} -e v1 -d n"

        # Run the second command in the terminal
        process2 = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout2, stderr2 = process2.communicate()

        # Check if any error occurred during execution
        if process2.returncode != 0:
            print(f"An error occurred while executing command 2 for {csv_file}:")
            print(stderr2.decode("utf-8"))
        else:
            print(f"Command 2 executed successfully for {csv_file}! Output saved to {simout_file}")

        # Remove the DTMC CSV file
        os.remove(csv_file)
        print(f"DTMC CSV file removed: {csv_file}")
