import ast


class SwitchEqualSidesTransformer(ast.NodeTransformer):
    def visit_Compare(self, node):
        # 确保递归遍历所有子节点
        self.generic_visit(node)

        # 检查比较操作是否只有一个操作符，且该操作符为等号==
        if len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq):
            # 检查是否有两个比较元素（左侧和右侧）
            if len(node.comparators) == 1:
                left = node.left
                right = node.comparators[0]

                # 交换左右操作数
                node.left = right
                node.comparators = [left]

        return node


def transform_switch_equal_sides(source_code):
    tree = ast.parse(source_code)
    transformer = SwitchEqualSidesTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)


# 测试代码
test_code = """
if a == b:
    print("a equals b")
"""

transformed_code = transform_switch_equal_sides(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
