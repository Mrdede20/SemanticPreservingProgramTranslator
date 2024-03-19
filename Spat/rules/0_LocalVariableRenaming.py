import ast
import random
import string


class LocalVariableRenaming(ast.NodeTransformer):
    def __init__(self):
        super().__init__()
        # 记录已经遍历过的变量名称和它们的新名称
        self.renamed_vars = {}
        # Python内置名称列表，避免重命名这些名称
        self.builtin_names = dir(__builtins__)

    def visit_FunctionDef(self, node):
        # 每进入一个新的函数定义，清空已重命名变量记录，因为新的作用域开始了
        self.renamed_vars = {}
        self.generic_visit(node)
        return node

    def visit_Assign(self, node):
        # 对于每一个赋值语句，尝试重命名变量（如果是变量赋值的话）
        if isinstance(node.targets[0], ast.Name):
            var_name = node.targets[0].id
            if var_name not in self.builtin_names:
                new_name = self._get_new_name(var_name)
                node.targets[0].id = new_name
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        # 对于每一个变量名的使用，如果该变量已被重命名，则更新为新名称
        if node.id in self.renamed_vars:
            node.id = self.renamed_vars[node.id]
        return node

    def _get_new_name(self, old_name):
        # 如果变量已经被重命名，直接返回新名称
        if old_name in self.renamed_vars:
            return self.renamed_vars[old_name]

        # 生成一个新的随机变量名，并确保它不与已有的变量名冲突
        while True:
            new_name = ''.join(random.choices(string.ascii_letters, k=8))
            if new_name not in self.renamed_vars.values() and new_name not in self.builtin_names:
                self.renamed_vars[old_name] = new_name
                break
        return new_name


def rename_local_variables(code):
    tree = ast.parse(code)
    transformer = LocalVariableRenaming()
    new_tree = transformer.visit(tree)
    return ast.unparse(new_tree)


# 示例使用
code = """
def example_function(x):
    y = x + 1
    return y
x = 1
"""
new_code = rename_local_variables(code)
print(new_code)
