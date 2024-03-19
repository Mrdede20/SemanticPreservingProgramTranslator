# 导入所有规则
from Spat.rules.LocalVariableRenaming import LocalVarRenaming
from Spat.rules.LocalVariableRenaming_Wrongly import LocalVarRenaming_Wrongly
from Spat.rules.ChangeFor2While import For2While
from Spat.rules.ChangeFor2While_Wrongly import For2While_Wrongly
from Spat.rules.ChangeWhile2For import While2For
from Spat.rules.ReveseIf_Else import ReverseIfElse
from Spat.rules.ReveseIf_Else2_Wrongly import ReverseIfElse_Wrongly
from Spat.rules.SingleIf2ConditionalExp import SingleIF2ConditionalExp
from Spat.rules.ConditionalExp2SingleIF import ConditionalExp2SingleIF
from Spat.rules.PP2AddAssignment import PP2AddAssignment
from Spat.rules.AddAssignemnt2EqualAssignment import AddAssignment2EqualAssignment
from Spat.rules.InfixExpressionDividing import InfixExpressionDividing
from Spat.rules.If_Dividing import IfDividing
from Spat.rules.StatementsOrderRearrangement import StatementsOrderRearrangement
from Spat.rules.StatementsOrderRearrangement_Wrongly import StatementsOrderRearrangement_Wrongly
from Spat.rules.LoopIfContinue2Else import LoopIfContinue2Else
from Spat.rules.VarDeclarationMerging import VarDeclarationMerging
from Spat.rules.VarDeclarationDividing import VarDeclarationDividing
from Spat.rules.SwitchEqualSides import SwitchEqualSides
from Spat.rules.SwitchStringEqual import SwitchStringEqual
from Spat.rules.PrePostFixExpressionDividing import PrePostFixExpressionDividing
from Spat.rules.Case2IfElse import Case2IfElse

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
    def create(source_code: str, rule_id: str):
        if rule_id == "0":
            return LocalVarRenaming(source_code)
        elif rule_id == "1":
            return For2While(source_code)
        elif rule_id == "2":
            return While2For(source_code)
        elif rule_id == "3":
            return ReverseIfElse(source_code)
        elif rule_id == "4":
            return SingleIF2ConditionalExp(source_code)
        elif rule_id == "5":
            return ConditionalExp2SingleIF(source_code)
        elif rule_id == "6":
            return PP2AddAssignment(source_code)
        elif rule_id == "7":
            return AddAssignment2EqualAssignment(source_code)
        elif rule_id == "8":
            return InfixExpressionDividing(source_code)
        elif rule_id == "9":
            return IfDividing(source_code)
        elif rule_id == "10":
            return StatementsOrderRearrangement(source_code)
        elif rule_id == "11":
            return LoopIfContinue2Else(source_code)
        elif rule_id == "12":
            return VarDeclarationMerging(source_code)
        elif rule_id == "13":
            return VarDeclarationDividing(source_code)
        elif rule_id == "14":
            return SwitchEqualSides(source_code)
        elif rule_id == "15":
            return SwitchStringEqual(source_code)
        elif rule_id == "16":
            return PrePostFixExpressionDividing(source_code)
        elif rule_id == "17":
            return Case2IfElse(source_code)
        elif rule_id == "-1":
            return For2While_Wrongly(source_code)
        elif rule_id == "-3":
            return ReverseIfElse_Wrongly(source_code)
        elif rule_id == "-10":
            return StatementsOrderRearrangement_Wrongly(source_code)
        elif rule_id == "-99":
            return LocalVarRenaming_Wrongly(source_code)
        else:
            raise ValueError("No rule belongs to this id!")

