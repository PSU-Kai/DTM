# DTM
In this folder there are all of the codes that you will need to run the DTMC system automatically. 
But, the CDTA_auto.py and the merger.py are located in this folder just incase the script got lost. 

## ExpectedOperation_01,02,and03

in these 3 ExpectedOperation .xml files, it contains 3 different xml messages from 3 different actors.
all 3 of these actors are : GSP, DCM, DER.


##DTMC_Auto.py

This script will automate the process of the DTMC system from taking xml file and process it through the classifier.py
and the TMsim.py and as a result it will have SimOut.csv file. 

For this script, i modify the script where it will make 10 copies of each of the xml message. Then run it through the MVoT calculation, which is the 
TMsim.py, at the end of the calculation then it will delete the csv file after the classifer.py but saving the SimOut.csv
starting from "DTMC__01_SimOut" (This is your initial SimOut file from the first ExpectedOperation_01.xml message) 
to "DTMC__01_9_SimOut.csv" (This is the 10th copy).

"DTMC_02_***_SimOut" -- 02 meaning it is the ExpectedOperation_02.xml message

"DTMC_03_***_SimOut" -- 03 meaning it is the ExpectedOperation_03.xml message
