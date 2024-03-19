import ast
import random
import string

class LocalVariableRenamingTransformer_Wrongly(ast.NodeTransformer):
    def __init__(self):
        super().__init__()
        self.name_bindings = {}

    def visit_Name(self, node):
        # 根据Java版本，我们将收集所有变量名，但不区分它们的具体用途（定义或引用）
        if isinstance(node.ctx, ast.Load) or isinstance(node.ctx, ast.Store):
            if node.id not in self.name_bindings:
                self.name_bindings[node.id] = []
            self.name_bindings[node.id].append(node)
        return node

    def generic_visit(self, node):
        super().generic_visit(node)
        # 在遍历完所有节点后进行重命名
        if isinstance(node, ast.Module):
            for names in self.name_bindings.values():
                new_name = self._generate_new_name(8)
                for name in names:
                    name.id = new_name
        return node

    def _generate_new_name(self, length):
        # 生成一个长度为length的随机字符串
        return ''.join(random.choices(string.ascii_lowercase, k=length))

def transform_code_with_renaming(source_code):
    tree = ast.parse(source_code)
    transformer = LocalVariableRenamingTransformer_Wrongly()
    transformed_tree = transformer.visit(tree)
    new_code = ast.unparse(transformed_tree)
    return new_code

# 测试代码
test_code = """
x = 1
y = x + 2
print(x, y)
"""

transformed_code = transform_code_with_renaming(test_code)
print("原始代码:\n", test_code)
print("转换后的代码:\n", transformed_code)
