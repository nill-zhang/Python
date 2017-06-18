import googlemaps
import sys
from collections import OrderedDict
import openpyxl


def get_distances(locations, odometer, gap=2):
    results = OrderedDict()
    pairs = zip(locations[:-1], locations[1:])
    for pair in pairs:
        distance = get_distance(*pair)
        print("{}-->{}".format(*pair))
        distance = float(distance.strip(" km"))
        # todo
        # there is a bug, if I go from one place to another place more than once
        # the old value will be overwritten
        results["{}-->{}".format(*pair)] = [odometer, odometer+distance+gap, distance+gap]
        odometer += distance + 2
    for k, v in results.items():
        v[0], v[1] = "{:5.0f}".format(v[0]), "{:5.0f}".format(v[1])
        v[2] = "{:2.0f}".format(v[2])
        print("{}:\t\t{}\t\t{}\t\t{} km".format(k, *v))
    return results


def get_distance(point_a, point_b):
    gmaps = googlemaps.Client(key="AIzaSyDQLqZkFsK4wvSJ1u33KpE_Nh-u3eYDAZs")
    try:
        gr = gmaps.directions(point_a, point_b, mode="driving", avoid=["tolls", "highways"])
    except:
        return '0'
    if gr:
        return gr[0]["legs"][0]['distance']['text']
    else:
        return '0'


def process_excel(filepath, r):
    f = openpyxl.load_workbook(filepath, read_only=False)
    sheet = f.get_sheet_by_name("June")
    row = 8
    for k, v in r.items():
        # can not write line = [].extend(k.split("-->")+v)
        # because extend method return None
        line = []
        line.extend(k.split("-->") + v)
        for j in range(4, 9):
            sheet.cell(row=row, column=j).value = line[j-4]
        row += 1
    f.save("new.xlsx")

if __name__ == "__main__":
    sys.argv = ["cik", "L3R5G5", "M6P2M5", "L3R5G5", "M1C5B9", "M1T2G8", "L3P4H6", "M6P2M5", "L3S4P2",
                "L3R4P6", "M6P2M5", "L3R5G5", "M1W3N8", "M6P2M5", "M1W3N6", "L3R5G5", "L4S2S7", "M6P2M5",
                "M2H3J5", "M6L2T5", "M2N5H7", "M6P2M5"]
    r = get_distances(sys.argv[1:], 20658)
    process_excel("c:\\users\\admin\\pycharmprojects\\python\\myprograms\\June.xlsx", r)
