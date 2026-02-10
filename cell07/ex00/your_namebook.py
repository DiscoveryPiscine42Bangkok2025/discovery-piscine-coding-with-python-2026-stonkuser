def array_of_names(persons):
    result = []
    for first_name, last_name in persons.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        result.append(full_name)
    return result

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
