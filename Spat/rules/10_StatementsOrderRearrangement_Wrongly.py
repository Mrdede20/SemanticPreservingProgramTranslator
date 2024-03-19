import ast


class StatementsOrderRearrangementTransformer(ast.NodeTransformer):
    def visit_Module(self, node):
        self.generic_visit(node)  # 递归处理所有子节点

        for body in node.body:
            if isinstance(body, ast.FunctionDef) or isinstance(body, ast.ClassDef):
                self.rearrange_statements(body)
        return node

    def rearrange_statements(self, body_container):
        """重新排列函数或类定义体内的语句"""
        statements = body_container.body
        i = 0
        while i < len(statements) - 1:
            current_stmt = statements[i]
            next_stmt = statements[i + 1]
            # 简化逻辑：假设所有语句都可以互换
            statements[i], statements[i + 1] = next_stmt, current_stmt
            i += 2


def transform_statements_order_rearrangement(source_code):
    tree = ast.parse(source_code)
    transformer = StatementsOrderRearrangementTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)


# 测试代码
test_code = """
def example():
    a = 1
    print(a)
    b = 2
    print(b)
"""

transformed_code = transform_statements_order_rearrangement(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
