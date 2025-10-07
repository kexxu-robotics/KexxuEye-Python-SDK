# Written by: Jurriaan Schreuder

from pathlib import Path

from kexxu_eye_sdk.format import openeye_file_to_xy
from kexxu_eye_sdk.format import xy_file_to_openeye

# Test reading in an openeye file and getting the eye x,y coords
def test_openeye_file_to_xy():
    data_dir = Path(__file__).parent / "data"
    test_file_path = data_dir / "example-openeye-datafile.json"
    eye_locs = openeye_file_to_xy(test_file_path)
    assert len(eye_locs) == 691


def test_xy_to_openeye():
    # TODO
    abc = xy_file_to_openeye([])
    assert abc
