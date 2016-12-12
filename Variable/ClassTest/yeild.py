def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 3, 2, 4, 5]
b = list(dedupe(a))
print(b)