import ast


class ReverseIfElseTransformer(ast.NodeTransformer):
    def visit_If(self, node):
        # 构建新的反转条件
        new_test = ast.UnaryOp(op=ast.Not(), operand=node.test)

        # 交换then和else块
        new_body = node.orelse if node.orelse else []
        new_orelse = node.body

        # 更新node属性而不是创建新的节点
        node.test = new_test
        node.body = new_body
        node.orelse = new_orelse

        return node


def ReverseIfElse(source_code):
    tree = ast.parse(source_code)
    transformer = ReverseIfElseTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)


# # 测试代码
# test_code = """
# if condition:
#     print("Condition is true")
# else:
#     print("Condition is false")
# """
#
# transformed_code = ReverseIfElse(test_code)
# print("原始代码:\n", test_code)
# print("转换后的代码:\n", transformed_code)
