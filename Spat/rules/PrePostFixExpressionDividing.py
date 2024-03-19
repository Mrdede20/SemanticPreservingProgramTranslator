import ast

class IncrementDecrementTransformer(ast.NodeTransformer):
    def visit_AugAssign(self, node):
        # 处理增量和减量赋值操作
        if isinstance(node.op, ast.Add):
            # 将 `i += 1` 转换为 `i = i + 1`
            return ast.copy_location(
                ast.Assign(
                    targets=[node.target],
                    value=ast.BinOp(left=node.target, op=ast.Add(), right=node.value)
                ),
                node
            )
        elif isinstance(node.op, ast.Sub):
            # 将 `i -= 1` 转换为 `i = i - 1`
            return ast.copy_location(
                ast.Assign(
                    targets=[node.target],
                    value=ast.BinOp(left=node.target, op=ast.Sub(), right=node.value)
                ),
                node
            )
        return node

def PrePostFixExpressionDividing(source_code):
    tree = ast.parse(source_code)
    transformer = IncrementDecrementTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)

# # 测试代码
# test_code = """
# i = 0
# i += 1
# j = 0
# j -= 1
# """
#
# transformed_code = PrePostFixExpressionDividing(test_code)
# print("原始代码:\n", test_code)
# print("转换后的代码:\n", transformed_code)
