import ast


class SingleIfToConditionalExpTransformer(ast.NodeTransformer):
    def visit_If(self, node):
        # 检查是否有一个`else`部分和`if`和`else`都只有一个语句
        if isinstance(node.body, list) and len(node.body) == 1 and isinstance(node.body[0], ast.Assign) and \
                isinstance(node.orelse, list) and len(node.orelse) == 1 and isinstance(node.orelse[0], ast.Assign) and \
                node.body[0].targets[0].id == node.orelse[0].targets[0].id:
            # 构造条件表达式
            conditional_exp = ast.IfExp(test=node.test, body=node.body[0].value, orelse=node.orelse[0].value)

            # 创建新的赋值语句
            new_assign = ast.Assign(targets=node.body[0].targets, value=conditional_exp)
            return ast.copy_location(new_assign, node)

        return node


def transform_code_with_conditional_exp(source_code):
    tree = ast.parse(source_code)
    transformer = SingleIfToConditionalExpTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)


# 测试代码
test_code = """
if condition:
    x = 1
else:
    x = 2
"""

transformed_code = transform_code_with_conditional_exp(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
