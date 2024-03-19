import ast

class StatementsOrderRearrangementTransformer(ast.NodeTransformer):
    def __init__(self):
        self.forbidden_statements = (
            ast.Continue,
            ast.Break,
            ast.Return,
            ast.Call
        )

    def visit_FunctionDef(self, node):
        # 先递归处理子节点
        self.generic_visit(node)

        statements = node.body
        i = 0
        while i < len(statements) - 1:
            current_stmt = statements[i]
            next_stmt = statements[i + 1]

            # 如果当前或下一个语句是禁止重排的语句，跳过
            if isinstance(current_stmt, self.forbidden_statements) or isinstance(next_stmt, self.forbidden_statements):
                i += 1
                continue

            # 示例中未展示具体的canSwitch逻辑，这里我们假设所有非禁止的语句都可以互换
            # 实际应用中，您需要根据变量的依赖关系来判断是否可以互换
            statements[i], statements[i + 1] = next_stmt, current_stmt
            i += 2

        return node

def transform_statements_order(source_code):
    tree = ast.parse(source_code)
    transformer = StatementsOrderRearrangementTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)

# 测试代码
test_code = """
def example():
    a = 1
    b = 2
    return a + b
"""

transformed_code = transform_statements_order(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
