basename = "Station"
filenames = []

print(basename)
print(filenames)

for number in range(20):
    filenames.append(f"{basename}_{number}.txt")
    
print(filenames)