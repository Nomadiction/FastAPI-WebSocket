def extraction(data):
    extracted_data = [(item['name'], item['age']) for item in data]
    return extracted_data


def permute_name(name, age):
    name_list = list(name)
    intermediate_results = []

    for i in range(age):
        intermediate_results.append(''.join(name_list))
        name_list = [name_list[-1]] + name_list[:-1]

    return intermediate_results, ''.join(name_list)


