# Created by Keith Hill
# May 2017

# Need Python 2.7 and speedtest-cli and smtplib packages

# Description: Run a speed test and record the results in a CSV file
#               send an email if the speed is too low

import speedtest
import SpeedTestLogging
import os
import ConfigParser
import sys
import time

results = speedtest.SpeedtestResults

Logging = SpeedTestLogging
myPath = os.path.dirname(os.path.abspath(__file__))

# get config info
try :
        config = ConfigParser.ConfigParser()
        config.read(myPath + "/config.ini")
        maxSize = int(config.get('file','size')) * 1000  #size in bytes
        loggingEnabled = config.get('options','loggingEnabled').lower()
        emailEnabled = config.get('options','emailEnabled').lower()
        minDownload = int(config.get('options','mindownload'))
        minUpload = int(config.get('options','minupload'))
        rerunInterval = int(config.get('options','rerunInterval'))
        extendedLoggingEnabled = config.get('options','extendedLoggingEnabled').lower()
        maxConsecutive = int(config.get('options','maxConsecutive'))

except : 
        print ("error accessing the config file.  Ensure file titled 'config.ini' exists.")
        raise

try :
        version = config.get('options','version')
except :
        print ("unable to find version number in config file.  Ensure version is 2")
        raise

# check config version is 2
if version != "2" :
    print("Incorrect version nmber in the config file.  Expecting version 2")
    os.system("pause")
    sys.exit()
    


#start by running the upload and download test
results = Logging.executeTest()


#log the results into a local file
if loggingEnabled == "true" :
    Logging.logResults (results, "standard", 0)


#email the results if below a certain threshhold
if ((results.download < minDownload or results.upload < minUpload) and emailEnabled) == "true" :
    Logging.emailResults(results)


#if the results are below the threshhold, continue to run and log
if ((results.download < minDownload or results.upload < minUpload) and extendedLoggingEnabled) == "true" :
    print("Results below threshhold. Beginning extended logging")
    count = 0
    done = False


    while not done :
        # perform the test again
        results = Logging.executeTest()
        
        # log the results
        Logging.logResults (results, "extended", count)

        # increment and see if we should break the loop
        count += 1
        if (count >= maxConsecutive or (results.download >= minDownload and results.upload >= minUpload)) :
            done = True
            print("Results exceeded threshhold or consecutive max has been hit")
        else :
            print("Results continue to be under threshhold.  Waiting for " + str(rerunInterval) + " seconds")
            time.sleep(30)
            


    