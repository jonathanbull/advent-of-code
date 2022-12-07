all_nodes = []

class Node(object):
    def __init__(self, name, type, filesize = 0):
        self.name = name
        self.type = type
        self.filesize = filesize
        self.parent = None
        self.children = []
        all_nodes.append(self)


    def add_child(self, node):
        if self.type != 'dir':
            raise Exception('Can only add a child to a directory.')

        if node not in self.children:
            node.parent = self
            self.children.append(node)

            # Traverse up its parent directories, inflating the filesize of each
            parent = node.parent
            while parent is not None:
                parent.filesize += node.filesize
                parent = parent.parent


    def find_child(self, node_name, node_type):
        for node in self.children:
            if node.name == node_name and node.type == node_type:
                return node

        return None


    def __str__(self):
        return 'Node "{}" is a {} with {} children and a total filesize of {}.'.format(self.name, self.type, len(self.children), self.filesize)


def get_total_filesize_of_all_dir_nodes(ignore_sizes_greater_than = None):
    total_filesize = 0
    for node in all_nodes:
        if node.type != 'dir' or node.filesize > ignore_sizes_greater_than:
            continue
        print(' - Adding dir node {} with a total filesize of {}'.format(node.name, node.filesize))
        total_filesize += node.filesize

    return total_filesize


def print_all_nodes():
    for node in all_nodes:
        print(node)


root_node = Node('root', 'dir')
current_node = root_node

with open('input.txt') as input_file:
    for line in input_file:
        print(' - Current node: ' + str(current_node))
        line = line.strip()
        print(line)
        if line.startswith('dir '):
            # Directory
            print(' - is directory')
            node = Node(line[4:], 'dir')
            print(' - ' + str(node))
            current_node.add_child(node)
        elif line[0].isdigit():
            # File
            print(' - is file')
            size_str, name_str = line.split(' ')
            node = Node(name_str, 'file', int(size_str))
            print(' - ' + str(node))
            current_node.add_child(node)
        elif line.startswith('$ cd'):
            # Command
            print(' - is command')
            destination = line.split('$ cd ')[1]
            print(' - destination: ' + destination)
            if destination == '..':
                current_node = current_node.parent
            elif destination == '/':
                # Do nothing
                pass
            else:
                target_node = current_node.find_child(destination, 'dir')
                current_node = target_node


print_all_nodes()
max_filesize = 100000
total_filesize = get_total_filesize_of_all_dir_nodes(max_filesize)

print('-' * 50)
print('Total number of nodes: {}'.format(len(all_nodes)))
print('Total sum of nodes with size greater than {}: {}'.format(max_filesize, total_filesize))
