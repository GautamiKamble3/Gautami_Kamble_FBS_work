# Convert the time entered in hh,min and sec into seconds.

hour = int(input("Enter hour: "))
min  = int(input("Enter Minutes: "))
sec = int(input("Enter seconds: "))

total_seconds = ((hour * 3600) + (min * 60) + sec)

print(f"Total converted seconds is : {total_seconds}")
