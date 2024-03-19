import os
from concurrent.futures import ThreadPoolExecutor
from RuleSelector import RuleSelector

class Utils:
    @staticmethod
    def transform_file(input_dir, output_dir, filename, rule_id):
        if filename.endswith(".py"):  # 确保处理Python文件
            # Create a new directory inside output_dir with the name _<rule_id>
            specific_output_dir = os.path.join(output_dir, f"_{rule_id}")
            os.makedirs(specific_output_dir, exist_ok=True)  # This will create the directory if it doesn't exist

            input_path = os.path.join(input_dir, filename)
            # Save the file in the new _<rule_id> directory
            output_path = os.path.join(specific_output_dir, os.path.splitext(filename)[0] + "_transformed.py")

            # 读取原始代码
            with open(input_path, "r", encoding="utf-8") as file:
                source_code = file.read()

            # 转换代码
            transformed_code = RuleSelector.create(source_code, rule_id)

            # 写入新文件
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(transformed_code)

    @staticmethod
    def read_and_transform_files_concurrently(input_dir, output_dir, rule_id, max_workers=5):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for filename in os.listdir(input_dir):
                executor.submit(Utils.transform_file, input_dir, output_dir, filename, rule_id)
