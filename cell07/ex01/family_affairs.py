def find_the_redheads(family):
    return list(
        map(
            lambda item: item[0],
            filter(lambda item: item[1] == "red", family.items())
        )
    )

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
