#!/usr/bin/env
# by sfzhang 2016.11.24
import json
import pprint
import itertools
from collections import defaultdict
import re
from operator import itemgetter


def get_json_objects(json_file_dir):
    with open(json_file_dir, encoding="utf-8") as json_file:
        for each_obj in json_file:
            if each_obj.strip():
                yield json.loads(each_obj.strip())
        json_file.close()


def get_object_features(input_dict, dict_keys):
    features_tuple = (input_dict.get(i, '') for i in dict_keys)
    features_str = ' '.join(features_tuple)
    normalized_str = features_str.strip().lower().replace("_", "-")
    keyword_list = re.split(r"\W+", normalized_str)
    return set(keyword_list)


def get_matching_objects():

    for listing_obj in get_json_objects("listings.txt"):
        result_objects = {}
        feature_matching_cnt = 0
        listing_features = get_object_features(listing_obj, ("manufacturer", "title"))
        for product_obj in list(get_json_objects("products.txt")):
            product_features = get_object_features(product_obj, ("manufacturer", "model", "family"))
            features_intersection = listing_features & product_features
            if len(features_intersection) > feature_matching_cnt:
                matching_product = product_obj
                feature_matching_cnt = len(features_intersection)

        if feature_matching_cnt >= 3:
            # yield matching_product["product_name"], listing_obj
            result_objects["product_name"] = matching_product["product_name"]
            result_objects["listings"] = [listing_obj]
            yield result_objects


def get_result_objects():
    result_objects = defaultdict(list)
    for i, j in get_matching_objects():
        result_objects[i].append(j)
    #pprint.pprint(result_objects)
    for i, j in result_objects:
       #print(i, j)
       yield dict(zip(("product_name", "listings"), (i, j)))


# listings_objects = (i for i in get_json_objects("listings.txt"))
# sorted_listings_objects = sorted(listings_objects, key=lambda x: x["manufacturer"].lower())
# temp = itertools.groupby(sorted_listings_objects, key=lambda x: x["manufacturer"].lower())
# #grouped_listings_objects = {name: list(objects) for name, objects in temp}
# for name, objects in temp:
#     print(name, ":")
#     pprint.pprint(list(objects))
#
# products_objects = (j for j in get_json_objects("products.txt"))
#
#
# def get_result_object():
#     for product_object in products_objects:
#         results_objects = defaultdict(list)
#         keyword_set = set(product_object.keys()) - set(["product_name", "announced-date"])
#         product_feature_set = {product_object[i].lower() for i in keyword_set}
#         potential_listing = grouped_listings_objects.get(product_object["manufacturer"].lower(), [])
#         results_objects["product_name"] = product_object["product_name"]
#         for item in potential_listing:
#             listings_feature_set = set(item.get("title", '').lower().split())
#             if product_feature_set & listings_feature_set == product_feature_set:
#                 results_objects["listings"].append(item)
#
#         if "listings" not in results_objects.keys():
#             results_objects["listings"]
#         pprint.pprint(results_objects, indent=4, width=100)
#         yield results_objects


def save_result_object(result_file_dir):
    with open(result_file_dir, "w", encoding="utf-8") as result_file:
        for each_obj in get_result_objects():
            json.dump(each_obj, result_file)
            result_file.write("\n")
        result_file.close()


if __name__ == "__main__":
    #save_result_object("results.txt")
    get_result_objects()
