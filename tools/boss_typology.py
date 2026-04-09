#!/usr/bin/env python3
"""
Boss Typology - 老板类型学
实现8维标签系统的老板类型分类和应对策略
"""

import json
import argparse
from enum import Enum
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from pathlib import Path


class ManagementStyle(Enum):
    """管理风格"""
    MICROMANAGER = "micromanager"
    HANDS_OFF = "hands-off"
    COACH = "coach"
    DICTATOR = "dictator"
    LAISSEZ_FAIRE = "laissez-faire"


class DecisionStyle(Enum):
    """决策风格"""
    DATA_DRIVEN = "data-driven"
    GUT_FEELING = "gut-feeling"
    FAST = "fast"
    CAUTIOUS = "cautious"
    CONSENSUS = "consensus"


class CommunicationStyle(Enum):
    """沟通风格"""
    DIRECT = "direct"
    INDIRECT = "indirect"
    STORYTELLER = "storyteller"
    EMOTIONAL = "emotional"


class FeedbackStyle(Enum):
    """反馈风格"""
    BLUNT = "blunt"
    SANDWICH = "sandwich"
    PASSIVE = "passive"
    PUBLIC = "public"


class StressResponse(Enum):
    """压力表现"""
    ANGRY = "angry"
    SILENT = "silent"
    WORRIED = "worried"
    SUPPORTIVE = "supportive"


class TechLevel(Enum):
    """技术程度"""
    SAVVY = "tech-savvy"
    CURIOUS = "tech-curious"
    AGNOSTIC = "tech-agnostic"
    AVERSE = "tech-averse"


@dataclass
class BossProfile:
    """老板画像"""
    name: str
    title: str
    management_style: ManagementStyle
    decision_style: DecisionStyle
    communication_style: CommunicationStyle
    feedback_style: FeedbackStyle
    stress_response: StressResponse
    tech_level: TechLevel
    catchphrases: List[str]
    anger_signals: List[str]
    
    def to_dict(self):
        return {
            "name": self.name,
            "title": self.title,
            "management_style": self.management_style.value,
            "decision_style": self.decision_style.value,
            "communication_style": self.communication_style.value,
            "feedback_style": self.feedback_style.value,
            "stress_response": self.stress_response.value,
            "tech_level": self.tech_level.value,
            "catchphrases": self.catchphrases,
            "anger_signals": self.anger_signals
        }


class BossTypology:
    """老板类型学系统"""
    
    # 管理风格定义
    MANAGEMENT_STYLES = {
        ManagementStyle.MICROMANAGER: {
            "name": "细节控",
            "emoji": "🔍",
            "traits": ["事无巨细都要管", "频繁检查进度", "不信任下属"],
            "communication": "主动高频汇报，提前准备细节，让他感觉'掌控一切'",
            "quotes": ["这个像素偏移了2px", "每2小时同步一次进展", "让我看看代码"],
            "dos": ["主动汇报每一个细节", "提前准备备选方案", "让他参与关键决策"],
            "donts": ["擅自做决定", "隐瞒问题", "说他'管太多'"]
        },
        ManagementStyle.HANDS_OFF: {
            "name": "放手型",
            "emoji": "🙌",
            "traits": ["只关注结果", "过程完全不管", "给很大自由度"],
            "communication": "主动寻求边界和反馈，定期同步关键节点",
            "quotes": ["你看着办", "我只要结果", "过程我不关心"],
            "dos": ["定期同步关键进展", "出问题及时升级", "明确边界和预期"],
            "donts": ["从不汇报", "问题爆炸才说", "过度依赖他决策"]
        },
        ManagementStyle.COACH: {
            "name": "教练型",
            "emoji": "🏃",
            "traits": ["耐心指导", "关注成长", "愿意培养人"],
            "communication": "主动请教，展示学习意愿，接受批评建议",
            "quotes": ["你觉得这样可以改进吗？", "我当年也犯过这个错", "重点是学到什么"],
            "dos": ["主动寻求反馈", "展示学习成果", "接受挑战任务"],
            "donts": ["敷衍了事", "重复犯同样错误", "拒绝成长机会"]
        },
        ManagementStyle.DICTATOR: {
            "name": "独裁型",
            "emoji": "👑",
            "traits": ["一言堂", "不听意见", "要求绝对服从"],
            "communication": "先执行再沟通，用数据改变他的想法，不要当众反驳",
            "quotes": ["按我说的做", "不需要讨论", "这是命令"],
            "dos": ["绝对服从执行", "私下委婉提建议", "准备充分数据"],
            "donts": ["当众质疑", "直接反驳", "拖延执行"]
        },
        ManagementStyle.LAISSEZ_FAIRE: {
            "name": "放任型",
            "emoji": "🌊",
            "traits": ["基本不出现", "团队自我管理", "很少干预"],
            "communication": "主动建立规则，重要决策书面留痕",
            "quotes": ["都行", "你们自己定", "我相信你们"],
            "dos": ["主动建立团队规则", "重要决策书面确认", "定期同步状态"],
            "donts": ["完全不打招呼", "关键决策不确认", "出了问题推诿"]
        }
    }
    
    # 决策风格定义
    DECISION_STYLES = {
        DecisionStyle.DATA_DRIVEN: {
            "name": "数据控",
            "emoji": "📊",
            "traits": ["必须有数据支撑", "相信数字不相信直觉"],
            "persuasion": "准备充分的数据分析报告，A/B测试结果",
            "taboo": ["我觉得...", "凭经验...", "感觉上..."],
            "needs": ["详细的数据表格", "对比分析", "ROI计算"]
        },
        DecisionStyle.GUT_FEELING: {
            "name": "直觉型",
            "emoji": "🎯",
            "traits": ["凭感觉决策", "相信第一印象"],
            "persuasion": "讲案例故事，营造氛围，让他'感觉对'",
            "taboo": ["堆砌大量数据表格", "过度分析", "犹豫不决"],
            "needs": ["成功案例", "视觉展示", "情感共鸣"]
        },
        DecisionStyle.FAST: {
            "name": "闪电型",
            "emoji": "⚡",
            "traits": ["快速决断", "不喜欢犹豫"],
            "persuasion": "准备简洁的1页纸方案，当场给结论",
            "taboo": ["我再想想", "让我考虑几天", "还需要调研"],
            "needs": ["一页纸方案", "清晰的结论", "快速响应"]
        },
        DecisionStyle.CAUTIOUS: {
            "name": "谨慎型",
            "emoji": "🐢",
            "traits": ["反复权衡", "需要很长时间"],
            "persuasion": "提前1-2周铺垫，给足思考时间，准备Plan B",
            "taboo": ["催他快做决定", "突然袭击", "信息不全"],
            "needs": ["充足的时间", "完整信息", "风险评估"]
        },
        DecisionStyle.CONSENSUS: {
            "name": "民主型",
            "emoji": "👥",
            "traits": ["喜欢讨论", "听取多方意见"],
            "persuasion": "提前私下沟通关键人，会上形成共识",
            "taboo": ["突然袭击", "未经沟通就上会", "独断专行"],
            "needs": ["多方意见", "讨论时间", "共识达成"]
        }
    }
    
    # 压力表现定义
    STRESS_RESPONSES = {
        StressResponse.ANGRY: {
            "name": "火山型",
            "emoji": "😤",
            "reaction": "发火、拍桌子、大声骂人",
            "warning": "声音变大、语速加快、表情严肃",
            "coping": "别顶嘴，让他发泄完，事后再沟通",
            "recovery": "通常30分钟内平复"
        },
        StressResponse.SILENT: {
            "name": "冷暴力型",
            "emoji": "🧊",
            "reaction": "不回消息、不见人、冷处理",
            "warning": "已读不回、取消会议、回避眼神",
            "coping": "主动破冰，但不要逼太紧，给他空间",
            "recovery": "可能需要1-2天"
        },
        StressResponse.WORRIED: {
            "name": "焦虑传染型",
            "emoji": "😰",
            "reaction": "不断问'怎么办'，传递焦虑",
            "warning": "频繁询问进展、失眠发朋友圈",
            "coping": "给他确定的答案，'我已经处理了X，正在处理Y'",
            "recovery": "问题解决后立即好转"
        },
        StressResponse.SUPPORTIVE: {
            "name": "战士型",
            "emoji": "🦸",
            "reaction": "更支持你，一起扛事",
            "warning": "'我来协调'、'我们一起想办法'",
            "coping": "感恩，事后一定要表达感谢",
            "recovery": "问题结束即恢复"
        }
    }
    
    # 常见混合类型
    HYBRID_TYPES = {
        "micromanager_data": {
            "name": "细节控+数据控",
            "combination": [ManagementStyle.MICROMANAGER, DecisionStyle.DATA_DRIVEN],
            "description": "要数据还要细节，最难搞但也最好预测",
            "strategy": "准备超级详细的报告，每个数字都要有来源",
            "difficulty": "⭐⭐⭐⭐⭐"
        },
        "coach_fast": {
            "name": "教练型+闪电决策",
            "combination": [ManagementStyle.COACH, DecisionStyle.FAST],
            "description": "快速决定但会解释原因，适合成长",
            "strategy": "抓住机会快速试错，事后认真复盘",
            "difficulty": "⭐⭐"
        },
        "dictator_angry": {
            "name": "独裁型+火山型",
            "combination": [ManagementStyle.DICTATOR, StressResponse.ANGRY],
            "description": "暴君模式，一言不合就发火",
            "strategy": "绝对服从，永远不要当众质疑",
            "difficulty": "⭐⭐⭐⭐⭐"
        },
        "hands_off_cautious": {
            "name": "放手型+谨慎型",
            "combination": [ManagementStyle.HANDS_OFF, DecisionStyle.CAUTIOUS],
            "description": "平时不管，但重大决策超级慢",
            "strategy": "提前很久铺垫，用时间换空间",
            "difficulty": "⭐⭐⭐"
        },
        "gut_passive": {
            "name": "直觉型+暗示型",
            "combination": [DecisionStyle.GUT_FEELING, FeedbackStyle.PASSIVE],
            "description": "凭感觉决策，但不告诉你为什么",
            "strategy": "多观察他的微表情，主动询问真实想法",
            "difficulty": "⭐⭐⭐⭐"
        }
    }
    
    @classmethod
    def classify_boss(cls, profile: BossProfile) -> Dict:
        """
        根据老板画像生成分类报告
        
        Args:
            profile: BossProfile对象
            
        Returns:
            分类报告字典
        """
        report = {
            "basic_info": {
                "name": profile.name,
                "title": profile.title
            },
            "management_style": cls.MANAGEMENT_STYLES.get(profile.management_style, {}),
            "decision_style": cls.DECISION_STYLES.get(profile.decision_style, {}),
            "stress_response": cls.STRESS_RESPONSES.get(profile.stress_response, {}),
            "hybrid_analysis": cls._analyze_hybrid_type(profile),
            "communication_guide": cls._generate_communication_guide(profile),
            "quick_test": cls._generate_quick_test(profile)
        }
        
        return report
    
    @classmethod
    def _analyze_hybrid_type(cls, profile: BossProfile) -> Dict:
        """分析混合类型"""
        # 查找匹配的混合类型
        for key, hybrid in cls.HYBRID_TYPES.items():
            styles = hybrid["combination"]
            matches = sum([
                profile.management_style in styles,
                profile.decision_style in styles,
                profile.stress_response in styles
            ])
            if matches >= 2:
                return hybrid
        
        return {
            "name": "独特型",
            "description": "你的老板有独特的组合，需要个性化分析",
            "strategy": "综合参考各类型的应对策略",
            "difficulty": "⭐⭐⭐"
        }
    
    @classmethod
    def _generate_communication_guide(cls, profile: BossProfile) -> Dict:
        """生成沟通指南"""
        mgmt = cls.MANAGEMENT_STYLES.get(profile.management_style, {})
        decision = cls.DECISION_STYLES.get(profile.decision_style, {})
        
        return {
            "reporting": {
                "frequency": "每天" if profile.management_style == ManagementStyle.MICROMANAGER else "每周",
                "detail_level": "详细" if profile.management_style == ManagementStyle.MICROMANAGER else "摘要",
                "format": "数据表格" if profile.decision_style == DecisionStyle.DATA_DRIVEN else "故事叙述"
            },
            "meeting_strategy": {
                "preparation": decision.get("needs", []),
                "opening": "先给数据" if profile.decision_style == DecisionStyle.DATA_DRIVEN else "先讲背景",
                "avoid": decision.get("taboo", [])
            },
            "escalation": {
                "when": "立即" if profile.stress_response == StressResponse.ANGRY else "整理清楚后",
                "how": "书面" if profile.communication_style == CommunicationStyle.DIRECT else "当面",
                "format": "问题+方案" if profile.decision_style == DecisionStyle.DATA_DRIVEN else "故事+情感"
            }
        }
    
    @classmethod
    def _generate_quick_test(cls, profile: BossProfile) -> List[Dict]:
        """生成快速识别测试"""
        return [
            {
                "question": "他开周会，第一句话通常是？",
                "options": [
                    "数据怎么样？" if profile.decision_style == DecisionStyle.DATA_DRIVEN else None,
                    "我简单说两句..." if profile.communication_style == CommunicationStyle.STORYTELLER else None,
                    "上周那件事谁负责？" if profile.management_style == ManagementStyle.MICROMANAGER else None,
                    "大家有什么想法？" if profile.decision_style == DecisionStyle.CONSENSUS else None
                ]
            },
            {
                "question": "你发消息问'这个方案可以吗？'",
                "options": [
                    "秒回'可以'" if profile.decision_style == DecisionStyle.FAST else None,
                    "2小时后才回'再想想'" if profile.decision_style == DecisionStyle.CAUTIOUS else None,
                    "不回" if profile.feedback_style == FeedbackStyle.PASSIVE else None,
                    "回5条语音分析问题" if profile.management_style == ManagementStyle.MICROMANAGER else None
                ]
            },
            {
                "question": "项目出问题了，他的第一反应是？",
                "options": [
                    "谁的责任？" if profile.stress_response == StressResponse.ANGRY else None,
                    "怎么解决？" if profile.stress_response == StressResponse.SUPPORTIVE else None,
                    "不说话看着你" if profile.stress_response == StressResponse.SILENT else None,
                    "开始焦虑问怎么办" if profile.stress_response == StressResponse.WORRIED else None
                ]
            }
        ]
    
    @classmethod
    def get_all_types(cls) -> Dict:
        """获取所有类型定义"""
        return {
            "management_styles": {k.value: v for k, v in cls.MANAGEMENT_STYLES.items()},
            "decision_styles": {k.value: v for k, v in cls.DECISION_STYLES.items()},
            "stress_responses": {k.value: v for k, v in cls.STRESS_RESPONSES.items()},
            "hybrid_types": cls.HYBRID_TYPES
        }


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(description='老板类型学系统')
    parser.add_argument('--list', action='store_true', help='列出所有类型定义')
    parser.add_argument('--classify', help='分类一个老板JSON文件')
    parser.add_argument('--example', action='store_true', help='显示示例老板画像')
    
    args = parser.parse_args()
    
    if args.list:
        types = BossTypology.get_all_types()
        print(json.dumps(types, ensure_ascii=False, indent=2))
    
    elif args.classify:
        with open(args.classify, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        profile = BossProfile(
            name=data['name'],
            title=data['title'],
            management_style=ManagementStyle(data['management_style']),
            decision_style=DecisionStyle(data['decision_style']),
            communication_style=CommunicationStyle(data['communication_style']),
            feedback_style=FeedbackStyle(data['feedback_style']),
            stress_response=StressResponse(data['stress_response']),
            tech_level=TechLevel(data['tech_level']),
            catchphrases=data.get('catchphrases', []),
            anger_signals=data.get('anger_signals', [])
        )
        
        report = BossTypology.classify_boss(profile)
        print(json.dumps(report, ensure_ascii=False, indent=2))
    
    elif args.example:
        example = BossProfile(
            name="张总",
            title="技术总监",
            management_style=ManagementStyle.MICROMANAGER,
            decision_style=DecisionStyle.DATA_DRIVEN,
            communication_style=CommunicationStyle.DIRECT,
            feedback_style=FeedbackStyle.BLUNT,
            stress_response=StressResponse.ANGRY,
            tech_level=TechLevel.SAVVY,
            catchphrases=["数据呢？", "再想想", "我再说一遍"],
            anger_signals=["我再说一遍", "你听懂了吗"]
        )
        
        print("示例老板画像:")
        print(json.dumps(example.to_dict(), ensure_ascii=False, indent=2))
        print("\n分类报告:")
        report = BossTypology.classify_boss(example)
        print(json.dumps(report, ensure_ascii=False, indent=2))
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
