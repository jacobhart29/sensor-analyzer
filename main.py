import csv

readings = []
first_reading = None
last_reading = None
min_reading = None
max_reading = None
unusual_count = 0

def calculate_average(readings):
    if len(readings) == 0:
        return 0
    return sum(readings) / len(readings)

with open('/Robot_Sensor_Readings_1000.csv', 'r') as f:
    reader = csv.reader(f)
    
    next(reader)

    for row in reader:
        print(type(row[2]))
        readings.append(float(row[2]))

for reading in readings:
    if reading < 20:
        unusual_count += 1
        print(reading)
        print("20")
    elif reading > 60:
        unusual_count += 1
        print(reading)
        print("60")

for start in range(0, len(readings), 100):
    group = readings[start:start + 100]
    print("Group:", start + 1, "to", start + len(group), "Average:", calculate_average(group))

print("Unusual readings:", unusual_count)
percentage = (unusual_count / len(readings)) * 100
print("Unusual percentage:", str(percentage) + "%")

first_reading = readings[0]
last_reading = readings[-1]
min_reading = min(readings)
max_reading = max(readings)
print("Number of readings:", len(readings))
print("First reading:", first_reading)
print("Last reading:", last_reading)
print("Minimum reading:", min_reading)
print("Maximum reading:", max_reading)

print("Average reading:", calculate_average(readings))