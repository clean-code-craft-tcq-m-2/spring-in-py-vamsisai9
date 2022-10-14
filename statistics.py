
def calculateStats(numbers):
  numAvg = None
  numMax = None
  numMin = None

  if len(numbers)>0:
    numAvg = sum(numbers)/len(numbers)
    numMin = min(numbers)
    numMax = max(numbers)

  statData = {}
  statData['avg'] = numAvg
  statData['max'] = numMax
  statData['min'] = numMin

  return statData
