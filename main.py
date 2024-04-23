class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def constant(value):
    return lambda _: value


def operator(op):
    return lambda x, y: op(x(), y())


def evaluate_expression(node):
    if node.left is None and node.right is None:
        return node.value()

    left_value = evaluate_expression(node.left)
    right_value = evaluate_expression(node.right)

    return node.value(left_value, right_value)


# Пример использования
# Создаем ленивое дерево выражения: (5 * 2) + (4 - 1)
root = Node(operator(lambda x, y: x + y))
root.left = Node(operator(lambda x, y: x * y))
root.left.left = Node(constant(5))
root.left.right = Node(constant(2))
root.right = Node(operator(lambda x, y: x - y))
root.right.left = Node(constant(4))
root.right.right = Node(constant(1))

result = evaluate_expression(root)
print(f"Результат вычисления: {result}")
