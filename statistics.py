

import math
def calculateStats(numbers):
  numAvg = math.nan
  numMax = math.nan
  numMin = math.nan

  if len(numbers)>0:
    numAvg = sum(numbers)/len(numbers)
    numMin = min(numbers)
    numMax = max(numbers)

  statData = {}
  statData['avg'] = numAvg
  statData['max'] = numMax
  statData['min'] = numMin

  return statData
