import ast
import copy
import astor

class ForToWhileTransformer(ast.NodeTransformer):
    def visit_For(self, node):
        # 检查迭代器是否为range函数调用
        if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name) and node.iter.func.id == 'range':
            init_stmt = None
            test_expr = None
            update_stmt = None

            range_args = node.iter.args
            if len(range_args) == 1:
                # range(stop)
                init_stmt = ast.Assign(targets=[copy.deepcopy(node.target)], value=ast.Num(n=0))
                test_expr = ast.Compare(left=copy.deepcopy(node.target), ops=[ast.Lt()],
                                        comparators=[copy.deepcopy(range_args[0])])
                update_stmt = ast.AugAssign(target=copy.deepcopy(node.target), op=ast.Add(), value=ast.Num(n=1))
            elif len(range_args) == 2:
                # range(start, stop)
                init_stmt = ast.Assign(targets=[copy.deepcopy(node.target)], value=copy.deepcopy(range_args[0]))
                test_expr = ast.Compare(left=copy.deepcopy(node.target), ops=[ast.Lt()],
                                        comparators=[copy.deepcopy(range_args[1])])
                update_stmt = ast.AugAssign(target=copy.deepcopy(node.target), op=ast.Add(), value=ast.Num(n=1))
            elif len(range_args) == 3:
                # range(start, stop, step)
                init_stmt = ast.Assign(targets=[copy.deepcopy(node.target)], value=copy.deepcopy(range_args[0]))
                test_expr = ast.Compare(left=copy.deepcopy(node.target), ops=[ast.Lt()],
                                        comparators=[copy.deepcopy(range_args[1])])
                update_stmt = ast.AugAssign(target=copy.deepcopy(node.target), op=ast.Add(),
                                            value=copy.deepcopy(range_args[2]))

            # 构建while循环
            while_body = node.body
            if update_stmt:
                while_body.append(update_stmt)
            while_loop = ast.While(test=test_expr, body=while_body, orelse=[])

            if init_stmt:
                return [init_stmt, while_loop]
            else:
                return while_loop
        else:
            # 如果不是基于range的for循环，则不转换
            return node


def transform_for_to_while(source_code):
    tree = ast.parse(source_code)
    transformer = ForToWhileTransformer()
    new_tree = transformer.visit(tree)
    return astor.to_source(new_tree)


# 测试代码
test_code = """
for i in range(0, 5):
    print(i)
"""

transformed_code = transform_for_to_while(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
