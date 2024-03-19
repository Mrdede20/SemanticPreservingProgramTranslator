import ast

class ConditionalExpToSingleIfTransformer(ast.NodeTransformer):
    def visit_Assign(self, node):
        # 检查赋值的右侧是否是条件表达式
        if isinstance(node.value, ast.IfExp):
            conditional_exp = node.value
            # 创建新的if语句
            new_if = ast.If(
                test=conditional_exp.test,
                body=[ast.copy_location(ast.Assign(targets=[node.targets[0]], value=conditional_exp.body), conditional_exp.body)],
                orelse=[ast.copy_location(ast.Assign(targets=[node.targets[0]], value=conditional_exp.orelse), conditional_exp.orelse)]
            )
            return ast.copy_location(new_if, node)
        return node

def transform_conditional_exp_to_single_if(source_code):
    tree = ast.parse(source_code)
    transformer = ConditionalExpToSingleIfTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)

# 测试代码
test_code = """
x = 1 if condition else 2
"""

transformed_code = transform_conditional_exp_to_single_if(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
