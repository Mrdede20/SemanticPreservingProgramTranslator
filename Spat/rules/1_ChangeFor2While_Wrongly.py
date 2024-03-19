import ast

class ChangeFor2WhileTransformer(ast.NodeTransformer):
    def visit_For(self, node):
        # 根据Java逻辑，将for循环转换为while循环
        # 注：Java示例中未完全处理初始化表达式(initexpressions)和更新表达式(updexpressions)
        # 这里我们将忽略for循环的初始化和更新部分，仅转换基本结构
        test = node.iter  # 使用iter部分作为while的条件，这里简化处理，实际转换可能需要不同处理

        # 创建新的while循环节点
        while_node = ast.While(
            test=test,
            body=node.body,
            orelse=[]
        )

        return ast.copy_location(while_node, node)

def transform_for_to_while(source_code):
    tree = ast.parse(source_code)
    transformer = ChangeFor2WhileTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)

# 测试代码
test_code = """
for i in range(5):
    print(i)
"""

transformed_code = transform_for_to_while(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
