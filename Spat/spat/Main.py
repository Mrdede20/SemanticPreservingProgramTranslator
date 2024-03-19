import ast
import os
from typing import List
import argparse

# 导入自定义的模块（这些模块在后面创建）
from RuleSelector import RuleSelector
from utils import Utils

def parse(file_content: str, output_dir: str, rule_id: str) -> None:
    # 将字符串转换为AST
    tree = ast.parse(file_content)
    # 创建一个修改后的AST的访问者
    visitor = RuleSelector.create(rule_id, tree, output_dir)
    # 应用规则
    visitor.visit(tree)
    # 将修改后的AST转换回字符串
    modified_code = Utils.ast_to_code(tree)
    # 保存修改后的代码
    Utils.save_code_to_file(modified_code, output_dir)

def parse_files_in_dir(dir_path: str, output_dir: str, rule_id: str) -> None:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                output_file_path = Utils.sublize_output(file_path, dir_path, output_dir)
                with open(file_path, "r") as source_file:
                    file_content = source_file.read()
                    try:
                        parse(file_content, output_file_path, rule_id)
                    except Exception as e:
                        print(f"Transformation failed for {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Apply semantic-preserving transformations to Python code.")
    parser.add_argument("rule_id", type=str, help="The ID of the transformation rule to apply.")
    parser.add_argument("dir_path", type=str, help="The directory path of the source files.")
    parser.add_argument("output_dir", type=str, help="The output directory for the transformed files.")
    args = parser.parse_args()

    parse_files_in_dir(args.dir_path, args.output_dir, args.rule_id)

if __name__ == "__main__":
    main()
