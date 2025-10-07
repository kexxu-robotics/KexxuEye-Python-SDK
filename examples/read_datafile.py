# Written by: Jurriaan Schreuder

from kexxu_eye_sdk.format import openeye_file_to_xy

path = "examples/example-openeye-datafile.json"
eye_locs = openeye_file_to_xy(path)

print("example output:")
print()
for i in range(20):
    print(eye_locs[i])
print()
print("number of eye locations loaded:", len(eye_locs))


