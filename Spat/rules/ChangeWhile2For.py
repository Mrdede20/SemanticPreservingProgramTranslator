import ast
import astor


class WhileToForTransformer(ast.NodeTransformer):
    def visit_While(self, node):
        # 创建一个无限迭代的生成器函数
        infinite_iter = ast.parse("iter(int, 1)").body[0].value
        # 创建for循环的迭代变量
        iter_var = ast.Name(id="_", ctx=ast.Store())

        # 将while循环条件转换为for循环内的if语句，并在条件不满足时使用break退出循环
        if_break_stmt = ast.If(
            test=ast.UnaryOp(op=ast.Not(), operand=node.test),
            body=[ast.Break()],
            orelse=[]
        )

        # 构造新的for循环体，首先检查条件，然后执行原while循环体中的语句
        new_for_body = [if_break_stmt] + node.body

        # 构建新的for循环
        new_for_loop = ast.For(
            target=iter_var,
            iter=infinite_iter,
            body=new_for_body,
            orelse=[]
        )

        return ast.copy_location(new_for_loop, node)


def While2For(source_code):
    tree = ast.parse(source_code)
    transformer = WhileToForTransformer()
    new_tree = transformer.visit(tree)
    return astor.to_source(new_tree)


# # 测试代码
# test_code = """
# i=0
# while i<5:
#     print("This will print once.")
#     i = i+1
# """
#
# transformed_code = While2For(test_code)
# print("原始代码:\n", test_code)
# print("转换后的代码:\n", transformed_code)
