from task3.parser import parse_string


def create_boolean_string(_search):
    _search = _search.split(" ")
    _search = [s.strip() for s in _search]
    return str.join(" AND ", _search)


def parse_inverted_index(filename):
    _inverted_index = dict()
    with open("../task3/data/" + str(filename) + ".txt", "r", encoding="UTF-8") as f:
        for line in f:
            word = line[:line.find(' ')]
            array = line[line.find(' '):]
            array = array[2:-2].split(',')
            array = [s.strip() for s in array]
            _inverted_index[word] = set(array)
    return _inverted_index


def parse_sites(filename):
    _sites = dict()
    with open("../task1/data/" + str(filename) + ".txt", "r", encoding="UTF-8") as f:
        for line in f:
            sites_array = line.split(' - ')
            _sites[sites_array[0]] = sites_array[1]
    return _sites


def get_list_urls(_set, _sites):
    _urls = list()
    if _set is None:
        return _urls

    for item in _set:
        _urls.append(_sites[item])
    return _urls


def search_by_query(search_string):
    inverted_index = parse_inverted_index("inverted_index_snapshot")
    sites = parse_sites("index")

    boolean_search_line = create_boolean_string(search_string)

    result = parse_string(boolean_search_line, inverted_index)
    urls_list = get_list_urls(result, sites)
    return urls_list
