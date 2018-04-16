import subprocess
import traceback
from datetime import datetime
from json import loads
from sys import argv

formatString = '%Y-%m-%dT%H:%M:%S%z'
since = "2018-03-01"

onTimes = {}
offTimes = {}

if len(argv) > 1:
  since = argv[1]

proc = subprocess.Popen(['journalctl', '--no-pager', '--output-fields=', '-o', 'json', '--since', since], stdout=subprocess.PIPE)

previousDay = None
previousDate = None

while True:
  line = proc.stdout.readline()
  if not line:
    break

  currentDate = None
  currentDay = None

  jsonData = loads(line)
  timestamp = int(jsonData.get("__REALTIME_TIMESTAMP", 0)) / 1000000
  if not timestamp:
    continue

  currentDate = datetime.fromtimestamp(timestamp)
  currentDay = currentDate.strftime("%d.%m.%Y")

  if not previousDate:
    previousDate = currentDate
    previousDay = currentDay
    onTimes[currentDay] = currentDate.strftime("%H:%M")
    continue

  if previousDay != currentDay:
    offTimes[previousDay] = previousDate.strftime("%H:%M")
    onTimes[currentDay] = currentDate.strftime("%H:%M")

  previousDate = currentDate
  previousDay = currentDay

data = ["%s - %s %s" % (onTime, offTimes.get(day, "-"), day) for day, onTime in onTimes.items()]

print("\n".join(data))
