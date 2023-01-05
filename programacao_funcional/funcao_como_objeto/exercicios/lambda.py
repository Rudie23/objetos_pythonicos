data = [
    ('Company A', 400, 6900),
    ('Company B', 500, 3500),
    ('Company C', 500, 5600),
    ('Company D', 200, 9900),
]

print(sorted(data, key=lambda v: (v[1], -v[2])))
