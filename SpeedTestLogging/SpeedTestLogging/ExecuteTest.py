# Created by Keith Hill
# May 2017

# Need Python 2.7 and speedtest-cli and smtplib packages

# Description: Run a speed test and record the results in a CSV file
#               send an email if the speed is too low

import speedtest
import SpeedTestLogging

results = speedtest.SpeedtestResults

Logging = SpeedTestLogging


#start by running the upload and download test
results = Logging.executeTest()


#log the results into a local file
Logging.logResults (results)


#email the results if below a certain threshhold
Logging.emailResults(results)