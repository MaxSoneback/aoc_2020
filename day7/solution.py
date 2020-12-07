from utils import import_data, submit
import networkx as nx


def part_1(data: []) -> int:
    def pre_process(data: []) -> {}:
        rule_dict = {}
        for rule in data:
            split_rule = rule.split(' contain ', 1)
            inner_bags = split_rule[1].split(', ')
            outer_bag = split_rule[0][:-5]
            for bag in inner_bags:
                if bag.find('no other bags') != -1:
                    amount = None
                    bag = None
                else:
                    amount = int(bag.split(' ', 1)[0])
                    bag = ' '.join(bag.split(' ')[1:-1])
                if outer_bag in rule_dict:
                    rule_dict[outer_bag].append((bag, amount))
                else:
                    rule_dict[outer_bag] = [(bag, amount)]
        return rule_dict

    bag_set = set()
    data = pre_process(data)

    for rule in data:
        if rule[1].find('shiny gold') != -1:
            bag_set.add(rule[0])
    return len(bag_set)


if __name__ == "__main__":
    data = import_data(7, __file__, True)
    count = part_1(data)
    print(count)
    #res, status = submit(7, 1, count)
    #print(f"Status code: {status}")
    #if status == 200:
    #    print(res)
