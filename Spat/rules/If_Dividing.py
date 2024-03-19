import ast


class IfDividingTransformer(ast.NodeTransformer):
    def visit_If(self, node):
        # 先递归处理子节点
        self.generic_visit(node)

        # 检查if条件是否是逻辑与操作
        if isinstance(node.test, ast.BoolOp) and isinstance(node.test.op, ast.And):
            # 创建外层if语句，条件为逻辑与操作的左侧表达式
            outer_if = ast.If(test=node.test.values[0], body=[], orelse=[])
            # 创建内层if语句，条件为逻辑与操作的右侧表达式
            inner_if = ast.If(test=node.test.values[1], body=node.body, orelse=node.orelse)
            # 将内层if语句作为外层if语句的执行体
            outer_if.body.append(inner_if)
            return ast.copy_location(outer_if, node)
        return node


def IfDividing(source_code):
    tree = ast.parse(source_code)
    transformer = IfDividingTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)


# # 测试代码
# test_code = """
# if a and b:
#     print("Both a and b are True")
# """
#
# transformed_code = IfDividing(test_code)
# print("原始代码:\n", test_code)
# print("转换后的代码:\n", transformed_code)
