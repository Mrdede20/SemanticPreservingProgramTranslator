import ast

class VarDeclarationDividingTransformer(ast.NodeTransformer):
    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Tuple) and isinstance(node.value, ast.Tuple) and len(node.targets[0].elts) == len(node.value.elts):
            new_nodes = []
            for target, value in zip(node.targets[0].elts, node.value.elts):
                new_assign = ast.Assign(targets=[ast.copy_location(target, node)], value=ast.copy_location(value, node))
                ast.fix_missing_locations(new_assign)
                new_nodes.append(new_assign)
            return new_nodes
        return node

def transform_var_declaration_dividing(source_code):
    tree = ast.parse(source_code)
    transformer = VarDeclarationDividingTransformer()
    transformed_tree = transformer.visit(tree)
    ast.fix_missing_locations(transformed_tree)  # 更新所有新节点的位置信息
    return ast.unparse(transformed_tree)

# 测试代码
test_code = """
a, b = 5, 10
"""

transformed_code = transform_var_declaration_dividing(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
