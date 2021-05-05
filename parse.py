import csv
from collections import defaultdict
from pprint import pprint

TYPES_GET_INFO = [
    "twitter_username", "facebook_page_url", "facebook_personal_url", "party_ppc_page_url", "homepage_url",
    "wikipedia_url", "linkedin_url", "blog_url", "instagram_url", "youtube_profile"]
TYPES_OTHER = ["email", "image_url", "gender", "birth_date", "wikidata_id"]
TYPES = TYPES_GET_INFO + TYPES_OTHER

regions = defaultdict(lambda: defaultdict(int))
with open("candidates-2021-05-06.csv") as f:
    for line in csv.DictReader(f):
        region_count = regions[line["NUTS1"]]
        region_count["candidates"] += 1
        for typ in TYPES:
            region_count[typ] += 1 if line[typ] else 0
        region_count["can_get_info"] += 1 if any(line[typ] for typ in TYPES_GET_INFO) else 0

pprint(regions)

for region_name, region_count in regions.items():
    print(region_name)
    print("    images=%.2f" % (region_count["image_url"] / float(region_count["candidates"])))
    print("    info_avail=%.2f" % (region_count["can_get_info"] / float(region_count["candidates"])))

with open("map.template") as f:
    template = f.read()

percentfmt = lambda value: "%d%%" % int(round(value * 100))
imagescolor = lambda value: "hsl(30, %d%%, 50%%)" % max(min((value * 300 - 50), 100), 0)
with open("map-images.svg", "w") as f:
    data = {
        "title1": "Percentage of",
        "title2": "candidates with",
        "title3": "images",
        "title4": "",
    }
    for region_name, region_count in regions.items():
        name = region_name.replace(" (England)", "")
        ratio = region_count["image_url"] / float(region_count["candidates"])
        data[name] = imagescolor(ratio)
        data["text" + name] = percentfmt(ratio)
    f.write(template % data)

infocolor = lambda value: "hsl(200, %d%%, 50%%)" % max(min((value * 300 - 50), 100), 0)
with open("map-has-info.svg", "w") as f:
    data = {
        "title1": "Percentage of",
        "title2": "candidates with",
        "title3": "social media",
        "title4": "or email",
    }
    for region_name, region_count in regions.items():
        name = region_name.replace(" (England)", "")
        ratio = region_count["can_get_info"] / float(region_count["candidates"])
        data[name] = infocolor(ratio)
        data["text" + name] = percentfmt(ratio)
    f.write(template % data)
