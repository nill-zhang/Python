import googlemaps
import sys
from collections import OrderedDict


def get_distances(locations, odometer, gap=2):
    results = OrderedDict()
    pairs = zip(locations[:-1], locations[1:])
    for pair in pairs:
        distance = get_distance(*pair)
        distance = float(distance.strip(" km"))
        results["{}-->{}".format(*pair)] = [odometer, odometer+distance+gap, distance+gap]
        odometer += distance + 2
    for k, v in results.items():
        print("{}:\t\t{:5.0f}\t\t{:5.0f}\t\t{:2.0f} km".format(k, *v))
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




if __name__ == "__main__":
    sys.argv = ["cik", "L3R5G5", "M6P2M5", "L3R5G5", "M1C5B9", "M1T2G8", "L3P4H6", "M6P2M5", "L3S4P2",
                "L3R4P6", "M6P2M5", "L3R5G5", "M1W3N8", "M6P2M5", "M1W3N6", "L3R5G5", "L4S2S7", "M6P2M5",
                "M2H3J5", "M6L2T5", "M2N5H7", "M6P2M5"]
    get_distances(sys.argv[1:], 20658)
