#!/usr/bin/env
import json
import pprint
import itertools
from collections import defaultdict


def get_json_objects(json_file_dir):
    with open(json_file_dir, encoding="utf-8") as json_file:
        for eachobj in json_file:
            if eachobj.strip("\n"):
                yield json.loads(eachobj.strip("\n"))
        json_file.close()

listings_objects = (i for i in get_json_objects("listings.txt"))
sorted_listings_objects = sorted(listings_objects, key=lambda x: x["manufacturer"].lower())
temp = itertools.groupby(sorted_listings_objects, key=lambda x: x["manufacturer"].lower())
grouped_listings_objects = {name: list(objects) for name, objects in temp}
# for name, objects in temp:
#     print(name, ":")
#     pprint.pprint(list(objects))

products_objects = (j for j in get_json_objects("products.txt"))


def get_result_object():
    for product_object in products_objects:
        results_objects = defaultdict(list)
        keyword_set = set(product_object.keys()) - set(["product_name", "announced-date"])
        product_feature_set = {product_object[i].lower() for i in keyword_set}
        potential_listing = grouped_listings_objects.get(product_object["manufacturer"].lower(), [])
        results_objects["product_name"] = product_object["product_name"]
        for item in potential_listing:
            listings_feature_set = set(item.get("title", '').lower().split())
            if product_feature_set & listings_feature_set == product_feature_set:
                results_objects["listings"].append(item)

        if "listings" not in results_objects.keys():
            results_objects["listings"]
        pprint.pprint(results_objects, indent=4, width=100)
        yield results_objects


def save_result_object(result_file_dir):
    with open(result_file_dir, "w", encoding="utf-8") as result_file:
        for eachobj in get_result_object():
            json.dump(eachobj, result_file)
            result_file.write("\n")
        result_file.close()


if __name__ == "__main__":
    save_result_object("results.txt")

