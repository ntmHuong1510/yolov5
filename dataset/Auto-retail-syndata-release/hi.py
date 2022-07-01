
import json
label = dict()
te = []
label["CATEGORIES"] = []
with open('labels.txt') as fp:
    for anno in fp:
        cate = {}
        anno = anno.split(',')
        anno[1] = anno[1][:-1]
        cate["id"] = int(anno[1])
        cate["name"] = anno[0]
        te.append(anno[0])
        cate["supercategory"] = "object"
        label["CATEGORIES"].append(cate)

print(te)
