# Top-Fortigate-Apps-from-Session-Dump

Use this python3 script to analyse the session dump of a fortigate, and find out the top used apps in the network by users .

This python reads as input : the session dump file, and a json app file (that has mapping between app id and app name)

I already provided a 2023 version of app-id file in the repo, you can download to use, 

if you think its outdated, you can generate the json file your self, (from fortigate get app status to dump list of app ids and names)


# how to use :

clone the repo, or download  top-N.py , appjson.txt, 

get your session dump file from fortigate, lets say its session-dump.txt


to run :

python3 top-N.py   // it will interactively ask you for fields.

NOTE: you might need to install some libraries , like matplotlib.
