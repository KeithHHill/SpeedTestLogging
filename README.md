# SpeedTestLogging
This python application will run a network speedtest using speedtest.net.  Results are logged in a CSV file and can optionally trigger an email if the results are below a configured threshhold.

## Requirements:

* Python 2.7
* Libs needed:
  * smtplib
  * speedtest-cli

## Instructions

Once installed follow instructions in the configFile.ini file.  To run, execute 'ExecuteTest.py'.  Results are stored in the 'logging' folder.
