ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
     "name": "petja",
     "age": 16,
}],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
     "age": 21,
    }, {
     "name": "pavel",
      "age": 15,
}],
}


emps = [ivan, darja]

for i in emps:
    report = i["children"]
    for j in report:
        if j["age"] > 18:
            print(i["name"])
            break

