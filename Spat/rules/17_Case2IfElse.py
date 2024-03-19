import ast
import astor
import copy


class MatchToIfElseTransformer(ast.NodeTransformer):
    def visit_Match(self, node):
        if_cases = []
        else_body = []
        for case in node.cases:
            if isinstance(case.pattern, ast.MatchAs) and case.pattern.name is None:  # 默认情况
                else_body = case.body
            else:
                # 处理条件
                if isinstance(case.pattern, ast.MatchValue):
                    if_condition = ast.Compare(
                        left=copy.deepcopy(node.subject),
                        ops=[ast.Eq()],
                        comparators=[copy.deepcopy(case.pattern.value)]
                    )
                else:
                    # 对于其他模式匹配类型，这里简化处理，实际使用时需要更复杂的逻辑
                    continue

                new_if = ast.If(test=if_condition, body=case.body, orelse=[])
                if_cases.append(new_if)

        # 将if语句链接起来
        for i in range(len(if_cases) - 2, -1, -1):
            if_cases[i].orelse = [if_cases[i + 1]]
        if if_cases:
            if_cases[-1].orelse = else_body
            return if_cases[0]
        else:
            return else_body


def transform_match_to_if_else(source_code):
    tree = ast.parse(source_code, mode='exec')
    transformer = MatchToIfElseTransformer()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)
    return astor.to_source(new_tree)


# 测试代码
test_code = """
match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")
"""

transformed_code = transform_match_to_if_else(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
