
Parameters:

'-l', '--link', help="URL to your web page", required=True </br>
'-t', '--time', type=int, help="Time interval between checks (seconds)", default=60 </br>
'-d', '--id', help="id of interesing web part. By default checks entire website" </br>
'-v', '--verbose', type=bool, help="output stuff", choices=[False,True], default=False </br>
'-f', '--file', help="name of file. Default: last_visit.txt"



Example:
Checks if reddit's main page has changed compared to the previous state 10 seconds ago. If something changed pop-up will appear:

    ./auto_tracking.py -l www.reddit.com -t 10

Same thing with verbose turned on:

    ./auto_tracking.py -l www.reddit.com -t 10 -v True


Checks if id element called "siteTable" has changed compared to the state 5 seconds ago:

    ./auto_tracking.py -l www.reddit.com -d siteTable -t 10
