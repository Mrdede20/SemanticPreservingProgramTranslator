import ast


class ReverseIfElseTransformer(ast.NodeTransformer):
    def visit_If(self, node):
        # 注意：这里不反转条件，仅交换then和else部分
        new_body = node.orelse if node.orelse else []
        new_orelse = node.body

        # 直接在原节点上修改以保持AST结构的其它部分不变
        node.body = new_body
        node.orelse = new_orelse

        return node


def ReverseIfElse_Wrongly(source_code):
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
# transformed_code = ReverseIfElse_Wrongly(test_code)
# print("原始代码:\n", test_code)
# print("转换后的代码:\n", transformed_code)
