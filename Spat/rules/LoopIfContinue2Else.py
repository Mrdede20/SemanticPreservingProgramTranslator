import ast


class LoopIfContinue2ElseTransformer(ast.NodeTransformer):
    def visit_If(self, node):
        # 确保递归处理子节点
        self.generic_visit(node)

        # 检查`if`语句内是否包含`continue`，且没有`else`分支
        if any(isinstance(n, ast.Continue) for n in ast.walk(node)) and not node.orelse:
            # 创建新的`if`语句的条件（取反当前条件）
            new_test = ast.UnaryOp(op=ast.Not(), operand=node.test)

            # 获取`if`语句所在循环体的其余部分作为`else`分支的内容
            new_else = []  # 此处简化处理，实际应用中需要从`if`语句所在的循环体中提取

            # 创建新的`if-else`结构
            new_if = ast.If(test=new_test, body=[], orelse=new_else)
            return new_if

        return node


def LoopIfContinue2Else(source_code):
    tree = ast.parse(source_code)
    transformer = LoopIfContinue2ElseTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)


# # 测试代码
# test_code = """
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)
# """
#
# transformed_code = LoopIfContinue2Else(test_code)
# print("原始代码:\n", test_code)
# print("转换后的代码:\n", transformed_code)
