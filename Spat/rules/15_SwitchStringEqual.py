import ast

class SwitchStringMethodCallsTransformer(ast.NodeTransformer):
    def visit_Call(self, node):
        # 确保递归处理所有子节点
        self.generic_visit(node)

        # 检查是否是特定的字符串方法调用
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Str):
            method_name = node.func.attr
            # 假设我们关注的方法是'find'，你可以根据需要调整
            if method_name in ['find']:
                if len(node.args) == 1 and isinstance(node.args[0], ast.Str):
                    # 构造新的方法调用
                    new_call = ast.Call(
                        func=ast.Attribute(value=node.args[0], attr=method_name, ctx=ast.Load()),
                        args=[node.func.value],
                        keywords=[]
                    )
                    return ast.copy_location(new_call, node)
        return node

def transform_switch_string_method_calls(source_code):
    tree = ast.parse(source_code)
    transformer = SwitchStringMethodCallsTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)

# 测试代码
test_code = """
result = "hello world".find("world")
"""

transformed_code = transform_switch_string_method_calls(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
