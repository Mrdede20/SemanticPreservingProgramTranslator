import ast


class InfixExpressionDividingTransformer(ast.NodeTransformer):
    pass


def InfixExpressionDividing(source_code):
    tree = ast.parse(source_code)
    transformer = InfixExpressionDividingTransformer()
    transformed_tree = transformer.visit(tree)
    new_code = ast.unparse(transformed_tree)
    return new_code

