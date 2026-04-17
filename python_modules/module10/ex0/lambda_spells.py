#!/usr/bin/env python3


# def artifact_sorter(artifacts: list[dict]) -> list[dict]
artifact = [
    {'name': "artifact3", "power": 3, 'art_type': "type1"},
    {'name': "artifact2", "power": 2, 'art_type': "type2"},
    {'name': "artifact6", "power": 6, 'art_type': "type3"},
    {'name': "artifact1", "power": 1, 'art_type': "type4"},
    {'name': "artifact4", "power": 4, 'art_type': "type5"},
]

sorted_list = list(sorted(artifact, key=lambda x: x['power'], reverse=True))
for dictx in sorted_list:
    print(dictx)
