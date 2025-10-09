# Written by: Jurriaan Schreuder

import json

def openeye_file_to_xy(path: str)-> List[Tuple[int,int]]:
  """Convert an OpenEye eye tracking recording datafile to x,y coordinates in pixels on the video, one per frame.

  Args:
    path: The file path to the OpenEye Datafile.

  Returns:
    List with [ (x,y), ... ] gaze locations, one for each video frame
  """

  eye_locs = []
  lines = read_lines(path)
  for line in lines:
    try:
      if not get_event_type(line) == "eyetracking":
          continue # not an eye tracking event, skip

      parts = get_event_parts(line)
      js = json.loads(parts[2])

      rx = js["pupil_rel_pos_x"]
      ry = js["pupil_rel_pos_y"]

      x, y = to_720p(rx, ry)
      eye_locs.append((x, y))
    except Exception as e:
        print("error processing event from line:")
        print(line)
   
  return eye_locs
  

def xy_file_to_openeye(arr: list):
  print("todo")
  return True


def read_lines(path: str):
  with open(path, "r") as f:
    lines = [line.strip() for line in f]
  return lines

def save_lines(lines: list, path: str):
  with open(path, "w") as f:
    f.write("\n".join(lines))

def get_event_type(line):
  p0 = get_event_parts(line)[0]
  return p0.rsplit("/", 1)[-1]

def get_event_parts(line):
  # event type, timestamp, json
  parts = line.strip().split(" ", 2)
  return parts

def to_720p(rx, ry):
  x = 640 - int((rx) * 640.0)
  y = 360 + int((ry) * 360.0)
  return x, y

def from_720p(x, y):
  rx = (640 - x) / 640.0 
  ry = (y - 360) / 360.0
  return rx, ry
