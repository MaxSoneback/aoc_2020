from utils import import_data, submit


def part_1(data: []) -> int:
    def pre_process(data: []) -> {}:
        ascendant_dict = {}
        for rule in data:
            split_rule = rule.split(' bags contain ', 1)
            children = split_rule[1].split(', ')
            parent = split_rule[0]
            for child in children:
                if 'no other bags' in child:
                    continue
                else:
                    child = ' '.join(child.split(' ')[1:3])
                    if child in ascendant_dict:
                        ascendant_dict[child].append(parent)
                    else:
                        ascendant_dict[child] = [parent]
        return ascendant_dict

    def traverse_bags(node_name: str, b_map: {}, node_set: set) -> None:
        node_set.add(node_name)

        if node_name not in b_map:
            return

        for node in b_map[node_name]:
            traverse_bags(node, b_map, node_set)
        b_map.pop(node_name, None)

        return

    data = pre_process(data)
    start_node = 'shiny gold'
    node_set = set()
    traverse_bags(start_node, data, node_set)
    return len(node_set) - 1  # -1 b/c of the shiny gold bag itself


def part_2(data: {}) -> int:
    def pre_process(data: []) -> {}:
        descendant_dict = {}
        for rule in data:
            split_rule = rule.split(' bags contain ', 1)
            children = split_rule[1].split(', ')
            parent = split_rule[0]
            for child in children:
                if 'no other bags' in child:
                    descendant_dict[parent] = None
                else:
                    amount = child.split(' ')[0]
                    child = ' '.join(child.split(' ')[1:3])
                    if parent in descendant_dict:
                        descendant_dict[parent].append((child, int(amount)))
                    else:
                        descendant_dict[parent] = [(child, int(amount))]
        return descendant_dict

    def traverse_bags(node_name: str, b_map: {}) -> int:
        children = b_map[node_name]
        counter = 0

        if children is None:
            return counter

        for child in children:
            counter += child[1] + child[1] * traverse_bags(child[0], b_map)
        return counter


    data = pre_process(data)
    start_node = 'shiny gold'
    count = traverse_bags(start_node, data)

    return count


if __name__ == "__main__":
    data = import_data(7, __file__, True)
    count = part_1(data)
    print(count)

    count = part_2(data)
    print(count)
    res, status = submit(7, 2, count)
    #print(f"Status code: {status}")
    #if status == 200:
    #    print(res)
