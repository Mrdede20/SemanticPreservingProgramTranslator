import os

from Utils import Utils


def main():
    # # 用户输入规则ID
    # RuleId = input("Enter Rule ID: ")
    #
    # # 用户输入根目录路径
    # RootDir = input("Enter the path to the root directory: ")
    #
    # # 用户输入输出目录路径
    # OutputDir = input("Enter the path to the output directory: ")
    RuleId = str(2)
    RootDir = "../../data/Original"
    OutputDir = "../../data/transformed"
    Utils.read_and_transform_files_concurrently(RootDir, OutputDir, RuleId)


# 调用main函数
if __name__ == "__main__":
    main()
