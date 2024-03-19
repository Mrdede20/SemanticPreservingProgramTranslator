import ast


# 导入所有规则的模块（后续需要创建）
from ..rules import *

class RuleSelector:
    # 定义所有可能的规则
    rules = {
        "0": "LocalVarRenaming",
        "1": "For2While",
        "2": "While2For",
        "3": "ReverseIfElse",
        "4": "SingleIF2ConditionalExp",
        "5": "ConditionalExp2SingleIF",
        "6": "PP2AddAssignment",
        "7": "AddAssignment2EqualAssignment",
        "8": "InfixExpressionDividing",
        "9": "IfDividing",
        "10": "StatementsOrderRearrangement",
        "11": "LoopIfContinue2Else",
        "12": "VarDeclarationMerging",
        "13": "VarDeclarationDividing",
        "14": "SwitchEqualSides",
        "15": "SwitchStringEqual",
        "16": "PrePostFixExpressionDividing",
        "17": "Case2IfElse",
        "-3": "ReverseIfElse_Wrongly",
        "-1": "For2While_Wrongly",
        "-10": "StatementsOrderRearrangement_Wrongly",
        "-99": "LocalVarRenaming_Wrongly"
    }

    @staticmethod
    def create(rule_id: str, tree: ast.AST, output_dir: str):
        # 将Java中的switch-case逻辑转换为Python中的if-elif-else
        if rule_id == "0":
            return rename_local_variables(tree, output_dir)
        elif rule_id == "1":
            return For2While(tree, output_dir)
        elif rule_id == "2":
            return While2For(tree, output_dir)
        elif rule_id == "3":
            return ReverseIfElse(tree, output_dir)
        # 添加更多规则匹配...
        else:
            raise ValueError("No rule belongs to this id!")

