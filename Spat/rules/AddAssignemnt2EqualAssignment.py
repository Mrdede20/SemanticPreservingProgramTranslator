import ast


class AddAssignmentToEqualAssignmentTransformer(ast.NodeTransformer):
    def visit_AugAssign(self, node):
        # 检查操作符并转换为等号赋值形式
        if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            # 创建新的二元操作表达式
            if isinstance(node.op, ast.Add):
                new_op = ast.Add()
            elif isinstance(node.op, ast.Sub):
                new_op = ast.Sub()
            elif isinstance(node.op, ast.Mult):
                new_op = ast.Mult()
            elif isinstance(node.op, ast.Div):
                new_op = ast.Div()

            new_right = ast.BinOp(left=ast.copy_location(node.target, node), op=new_op, right=node.value)
            # 创建新的等号赋值语句
            new_assign = ast.Assign(targets=[ast.copy_location(node.target, node)], value=new_right)
            return ast.copy_location(new_assign, node)
        return node


def AddAssignment2EqualAssignment(source_code):
    tree = ast.parse(source_code)
    transformer = AddAssignmentToEqualAssignmentTransformer()
    transformed_tree = transformer.visit(tree)
    return ast.unparse(transformed_tree)


# # 测试代码
# test_code = """
# x += 1
# y -= 2
# z *= 3
# w /= 4
# """
#
# transformed_code = AddAssignment2EqualAssignment(test_code)
# print("原始代码:\n", test_code)
# print("转换后的代码:\n", transformed_code)
