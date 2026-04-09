#!/usr/bin/env python3
"""
Scenario Engine
场景模拟引擎 - 模拟老板在不同场景下的反应
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import argparse


@dataclass
class BossProfile:
    """老板档案"""
    slug: str
    name: str
    title: str
    tags: Dict
    mgmt_content: str
    persona_content: str
    patterns: Dict


class ScenarioEngine:
    """场景模拟引擎"""
    
    # 场景类型
    SCENARIOS = ['review', '1on1', 'emergency', 'speech']
    
    # 怒火等级评估因素
    ANGER_FACTORS = {
        'p0_bug': 40,
        'p1_bug': 25,
        'p2_bug': 15,
        'user_impact_100k+': 20,
        'user_impact_10k+': 10,
        'user_impact_1k+': 5,
        'sensitive_period': 20,
        'repeat_issue': 20,
        'no_solution': 15,
        'delayed_report': 10,
        'has_solution': -10,
        'proactive_report': -10,
    }
    
    def __init__(self, bosses_dir: str = None):
        """初始化引擎"""
        if bosses_dir is None:
            self.bosses_dir = Path(__file__).parent.parent / "bosses"
        else:
            self.bosses_dir = Path(bosses_dir)
        
        self.templates_dir = Path(__file__).parent.parent / "templates"
    
    def load_boss(self, slug: str) -> Optional[BossProfile]:
        """加载老板档案"""
        boss_dir = self.bosses_dir / slug
        config_file = self.bosses_dir / ".config.json"
        
        if not boss_dir.exists():
            return None
        
        # 加载配置
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                boss_info = config.get("bosses", {}).get(slug, {})
        else:
            return None
        
        # 加载文件
        mgmt_file = boss_dir / boss_info.get('files', {}).get('mgmt', f'{slug}_mgmt.md')
        persona_file = boss_dir / boss_info.get('files', {}).get('persona', f'{slug}_persona.md')
        patterns_file = boss_dir / boss_info.get('files', {}).get('patterns', f'{slug}_patterns.json')
        
        mgmt_content = self._load_file(mgmt_file)
        persona_content = self._load_file(persona_file)
        patterns = self._load_json(patterns_file) or {}
        
        return BossProfile(
            slug=slug,
            name=boss_info.get('name', slug),
            title=boss_info.get('title', ''),
            tags=boss_info.get('tags', {}),
            mgmt_content=mgmt_content or '',
            persona_content=persona_content or '',
            patterns=patterns
        )
    
    def _load_file(self, filepath: Path) -> Optional[str]:
        """加载文本文件"""
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        return None
    
    def _load_json(self, filepath: Path) -> Optional[Dict]:
        """加载JSON文件"""
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    def simulate_review(self, boss: BossProfile, content: str, context: str = '') -> str:
        """方案汇报预审模拟"""
        # 解析管理风格
        mgmt_style = boss.tags.get('management_style', 'Hands-off')
        comm_style = boss.tags.get('communication_style', 'Direct')
        decision_style = boss.tags.get('decision_style', 'Analytical')
        
        # 生成质疑问题
        questions = self._generate_review_questions(
            content, decision_style, boss.patterns
        )
        
        # 生成准备建议
        preparations = self._generate_preparations(decision_style, mgmt_style)
        
        # 生成强调建议
        emphasis = self._generate_emphasis_points(boss)
        
        # 生成避坑建议
        pitfalls = self._generate_pitfalls(decision_style, comm_style)
        
        # 计算通过概率
        pass_probability = self._calculate_pass_probability(
            content, decision_style, questions
        )
        
        # 组装输出
        output = f"""
🎩 【{boss.name}视角的方案预审】

═══ 方案概要 ═══
{content[:200]}{'...' if len(content) > 200 else ''}

═══ 可能的质疑 ═══
"""
        
        for i, q in enumerate(questions[:8], 1):
            output += f"""
{i}. 「{q['question']}」
   潜台词：{q['subtext']}
   建议回答：{q['suggestion']}
"""
        
        output += "\n═══ 需要准备 ═══\n"
        for prep in preparations:
            output += f"✓ {prep['item']} - 原因：{prep['reason']}\n"
        
        output += "\n═══ 建议强调 ═══\n"
        for point in emphasis:
            output += f"• {point['point']} - 理由：{point['reason']}\n"
        
        output += "\n═══ 可能踩雷 ═══\n"
        for pitfall in pitfalls:
            output += f"✗ {pitfall['action']} - 后果：{pitfall['consequence']}\n"
        
        output += f"""
═══ 通过概率 ═══

{self._render_progress_bar(pass_probability)}
当前概率：{pass_probability}%

提升建议：
1. 准备{decision_style}型老板关注的数据支撑
2. 准备至少3个备选方案对比
3. 提前思考风险控制和Plan B
"""
        
        return output
    
    def _generate_review_questions(self, content: str, decision_style: str, 
                                   patterns: Dict) -> List[Dict]:
        """生成审查问题"""
        questions = []
        
        # 根据决策风格生成基础问题
        if decision_style == 'Data-driven':
            questions.extend([
                {
                    'question': '数据呢？这个结论的数据支撑是什么？',
                    'subtext': '质疑数据可信度',
                    'suggestion': '准备详细的数据来源和计算逻辑'
                },
                {
                    'question': '有没有对照数据？benchmark是什么？',
                    'subtext': '需要对比分析',
                    'suggestion': '准备行业数据或历史数据作为对比'
                },
            ])
        elif decision_style == 'Gut-feeling':
            questions.extend([
                {
                    'question': '你的直觉是什么？',
                    'subtext': '想听听直观判断',
                    'suggestion': '给出明确的倾向性意见'
                },
            ])
        elif decision_style == 'Cautious':
            questions.extend([
                {
                    'question': '最坏的情况是什么？',
                    'subtext': '关注风险控制',
                    'suggestion': '准备详细的风险清单和应对措施'
                },
            ])
        else:  # Analytical, Fast, Consensus
            questions.extend([
                {
                    'question': '还有别的方案吗？',
                    'subtext': '需要对比选择',
                    'suggestion': '准备至少2-3个备选方案'
                },
            ])
        
        # 通用问题
        questions.extend([
            {
                'question': '这个投入产出比是多少？',
                'subtext': '关注ROI',
                'suggestion': '准备量化的ROI测算'
            },
            {
                'question': '需要多少资源？timeline是什么？',
                'subtext': '关注执行可行性',
                'suggestion': '准备详细的资源需求和时间表'
            },
        ])
        
        return questions
    
    def _generate_preparations(self, decision_style: str, mgmt_style: str) -> List[Dict]:
        """生成准备建议"""
        preparations = [
            {
                'item': '详细的数据支撑材料',
                'reason': f'{decision_style}型老板需要数据依据'
            },
            {
                'item': '至少3个方案对比',
                'reason': '老板需要选择空间'
            },
            {
                'item': '风险评估和Plan B',
                'reason': '展示风险意识'
            },
        ]
        
        if mgmt_style == 'Micromanager':
            preparations.append({
                'item': '详细的执行细节',
                'reason': 'Micromanager关注执行过程'
            })
        
        return preparations
    
    def _generate_emphasis_points(self, boss: BossProfile) -> List[Dict]:
        """生成强调建议"""
        return [
            {
                'point': '量化成果和数据',
                'reason': '用数字说话更有说服力'
            },
            {
                'point': '风险控制和应对措施',
                'reason': '展示全面的思考'
            },
            {
                'point': '与当前战略的契合度',
                'reason': '证明方案的战略价值'
            },
        ]
    
    def _generate_pitfalls(self, decision_style: str, comm_style: str) -> List[Dict]:
        """生成避坑建议"""
        pitfalls = []
        
        if decision_style == 'Data-driven':
            pitfalls.append({
                'action': '用"我觉得"、"我认为"开头',
                'consequence': '会被打断要求提供数据'
            })
        
        if comm_style == 'Direct':
            pitfalls.append({
                'action': '绕弯子、铺垫太多',
                'consequence': '会被打断要求直接说重点'
            })
        
        pitfalls.extend([
            {
                'action': '只说好的方面，不提风险',
                'consequence': '被认为思考不全面'
            },
        ])
        
        return pitfalls
    
    def _calculate_pass_probability(self, content: str, decision_style: str, 
                                    questions: List) -> int:
        """计算通过概率"""
        base = 50
        
        # 内容长度影响
        if len(content) < 50:
            base -= 10
        elif len(content) > 500:
            base += 5
        
        # 决策风格影响
        if decision_style == 'Fast':
            base += 10
        elif decision_style == 'Cautious':
            base -= 10
        
        return max(10, min(95, base))
    
    def _render_progress_bar(self, percentage: int) -> str:
        """渲染进度条"""
        filled = int(percentage / 10)
        return '█' * filled + '░' * (10 - filled)
    
    def simulate_1on1(self, boss: BossProfile, topic: str, context: str = '') -> str:
        """1on1沟通模拟"""
        # 判断话题类型
        topic_type = self._detect_topic_type(topic)
        difficulty = self._calculate_difficulty(topic_type, boss.tags)
        
        # 生成反应
        reactions = self._generate_1on1_reactions(topic_type, boss)
        
        output = f"""
🎩 【{boss.name}的1on1模拟】

═══ 话题分析 ═══
类型：{topic_type}
难度等级：{'⭐' * difficulty}
最佳时机：周一上午（刚完成项目时最佳）

═══ 老板可能的反应 ═══

【第一反应】
{reactions['first']}
潜台词：{reactions['subtext']}

【最终决策预测】
• 接受 - 概率：{reactions['probabilities']['accept']}%
• 有条件接受 - 概率：{reactions['probabilities']['conditional']}%
• 拒绝/拖延 - 概率：{reactions['probabilities']['reject']}%

═══ 建议话术 ═══

【开场】
{boss.name}，想跟您聊聊我的职业发展。

【核心论据】
1. 用数据说话，展示具体成果
2. 说明对团队的价值贡献
3. 表达未来的承诺和规划

【收尾】
希望能听听您的建议。

═══ 最佳实践 ═══

✓ 应该做的：
  - 带数据来，用事实说话
  - 准备备选方案
  - 展现对团队的价值

✗ 不应该做的：
  - 不要情绪化或威胁
  - 不要只谈个人需求
  - 不要 unprepared
"""
        
        return output
    
    def _detect_topic_type(self, topic: str) -> str:
        """检测话题类型"""
        topic_lower = topic.lower()
        
        if any(word in topic_lower for word in ['加薪', '涨薪', 'salary']):
            return '加薪'
        elif any(word in topic_lower for word in ['晋升', '升职', 'promotion']):
            return '晋升'
        elif any(word in topic_lower for word in ['困难', '问题', 'problem']):
            return '困难求助'
        elif any(word in topic_lower for word in ['离职', '辞职', 'quit']):
            return '离职'
        else:
            return '一般沟通'
    
    def _calculate_difficulty(self, topic_type: str, tags: Dict) -> int:
        """计算难度等级"""
        base_difficulty = {
            '加薪': 4, '晋升': 5, '困难求助': 2, '离职': 3, '一般沟通': 1
        }
        
        difficulty = base_difficulty.get(topic_type, 3)
        
        if tags.get('management_style') == 'Dictator':
            difficulty += 1
        elif tags.get('management_style') == 'Coach':
            difficulty -= 1
        
        return max(1, min(5, difficulty))
    
    def _generate_1on1_reactions(self, topic_type: str, boss: BossProfile) -> Dict:
        """生成1on1反应"""
        reactions = {
            'first': '',
            'subtext': '',
            'probabilities': {'accept': 30, 'conditional': 40, 'reject': 30}
        }
        
        if topic_type == '加薪':
            reactions['first'] = '「你的业绩数据我看了，确实超额完成。」（翻看数据）'
            reactions['subtext'] = '认可成绩，但想压价'
            reactions['probabilities'] = {'accept': 20, 'conditional': 50, 'reject': 30}
        elif topic_type == '晋升':
            reactions['first'] = '「你觉得现在具备晋升的条件了吗？」'
            reactions['subtext'] = '测试你的自我认知'
            reactions['probabilities'] = {'accept': 15, 'conditional': 35, 'reject': 50}
        else:
            reactions['first'] = '「说说你的想法。」'
            reactions['subtext'] = '开放态度'
            reactions['probabilities'] = {'accept': 40, 'conditional': 40, 'reject': 20}
        
        return reactions
    
    def simulate_emergency(self, boss: BossProfile, event: str, 
                          severity: str = 'high', context: str = '') -> str:
        """突发情况应对模拟"""
        # 计算怒火等级
        anger_level = self._calculate_anger_level(event, severity)
        
        # 解析风格
        stress_response = boss.tags.get('stress_response', 'Angry')
        
        output = f"""
🎩 【{boss.name}的突发情况应对】

═══ 🔥 怒火等级预测 ═══

{self._render_progress_bar(anger_level)} {anger_level}%

评估依据：
• 事件严重程度：{severity}
• 影响范围：需进一步评估
• 已采取措施：{'已处理' if '已' in event or '修复' in event else '未明确'}

═══ 💬 老板会怎么反应 ═══
"""
        
        if stress_response == 'Angry':
            if anger_level > 70:
                output += """
【质问】「我再说一遍，为什么会发生这种事？」（音量提高）
【追责】直接指出责任，要求立即解释
【要求】要求1小时内给出解决方案
"""
            else:
                output += """
【质问】「什么时候发现的？影响有多大？」（语气严肃）
【追责】追问原因，关注为什么没有提前发现
【要求】要求详细的时间线和恢复计划
"""
        elif stress_response == 'Silent':
            output += """
【质问】（沉默片刻）「...继续说」
【追责】不直接批评，但气氛压抑
【要求】要求书面报告
"""
        else:
            output += """
【质问】「会不会继续恶化？最坏会怎样？」（焦虑）
【追责】不断追问风险
【要求】要求每小时汇报
"""
        
        output += f"""
═══ 🛡️ 汇报话术 ═══

「{boss.name}，向您汇报一个紧急情况：

【当前状态】
{event[:100]}...

【影响评估】
• 影响范围：正在统计中
• 恢复时间：预计X小时内完全恢复

【已采取措施】
1. 已定位问题原因，正在修复
2. 已通知相关团队协助

【下一步计划】
30分钟内完成修复并验证，1小时内全量恢复

【预防措施】
我会牵头做详细复盘，找出根因并制定预防措施。

这是我的责任，我会全程跟进直到解决。」

═══ 📉 如何降低损失 ═══

🔴 立即停止问题扩散，控制影响范围
🟠 建立War Room，集中资源解决问题
🟡 准备用户补偿方案（如适用）
🟡 记录完整时间线，为复盘做准备

═══ ⏰ 恢复信任时间线 ═══

预计需要 {self._estimate_recovery_time(anger_level)} 周恢复信任

第1周：快速止损，控制影响范围
第2周：详细复盘，提出改进措施
第3-4周：执行改进，用结果说话
"""
        
        return output
    
    def _calculate_anger_level(self, event: str, severity: str) -> int:
        """计算怒火等级"""
        level = {'low': 20, 'medium': 40, 'high': 60, 'critical': 80}.get(severity, 50)
        
        event_lower = event.lower()
        if any(word in event_lower for word in ['p0', 'p1', 'critical', '严重']):
            level += 30
        if '修复' in event or '已' in event:
            level -= 10
        
        return max(0, min(100, level))
    
    def _estimate_recovery_time(self, anger_level: int) -> int:
        """估计恢复信任时间"""
        if anger_level > 80: return 4
        elif anger_level > 60: return 3
        elif anger_level > 40: return 2
        return 1
    
    def simulate_speech(self, boss: BossProfile, occasion: str, topic: str) -> str:
        """演讲稿生成"""
        return f"""
🎩 【{boss.name}风格的演讲稿】

═══ 演讲概览 ═══
场合：{occasion}
主题：{topic}
风格：{boss.tags.get('communication_style', 'Direct')}

═══ 演讲稿 ═══

【开场】
各位同事，简单说两句。

今天我们要讲的是{topic}。

【主体】
过去一年，我们取得了不错的成绩。
但同时也面临着不少挑战。

关于{topic}，我想强调几点：
第一，...
第二，...
第三，...

【结尾】
我相信，只要我们一起努力，一定能达成目标。
谢谢大家。

═══ 语言特色 ═══
• 简洁直接，不绕弯子
• 数据支撑，事实说话
• 鼓舞士气，但不过度承诺
"""


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='Scenario Engine - 场景模拟引擎',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 方案预审
  python scenario_engine.py review zhang "计划投入100万做用户增长"
  
  # 1on1模拟
  python scenario_engine.py 1on1 zhang "想申请加薪20%"
  
  # 突发情况应对
  python scenario_engine.py emergency zhang "线上P0级bug影响10万用户"
  
  # 演讲稿生成
  python scenario_engine.py speech zhang 年会 "Q4动员"
        """
    )
    
    subparsers = parser.add_subparsers(dest='scenario', help='场景类型')
    
    # review 场景
    review_parser = subparsers.add_parser('review', help='方案汇报预审')
    review_parser.add_argument('boss', help='老板slug')
    review_parser.add_argument('content', help='方案内容')
    
    # 1on1 场景
    oneonone_parser = subparsers.add_parser('1on1', help='1on1沟通模拟')
    oneonone_parser.add_argument('boss', help='老板slug')
    oneonone_parser.add_argument('topic', help='话题内容')
    
    # emergency 场景
    emergency_parser = subparsers.add_parser('emergency', help='突发情况应对')
    emergency_parser.add_argument('boss', help='老板slug')
    emergency_parser.add_argument('event', help='事件描述')
    emergency_parser.add_argument('--severity', default='high', 
                                  choices=['low', 'medium', 'high', 'critical'],
                                  help='严重程度')
    
    # speech 场景
    speech_parser = subparsers.add_parser('speech', help='演讲稿生成')
    speech_parser.add_argument('boss', help='老板slug')
    speech_parser.add_argument('occasion', help='场合')
    speech_parser.add_argument('topic', help='主题')
    
    args = parser.parse_args()
    
    if not args.scenario:
        parser.print_help()
        return
    
    engine = ScenarioEngine()
    boss = engine.load_boss(args.boss)
    
    if not boss:
        print(f"❌ 老板Skill '{args.boss}' 不存在，请先使用 boss_manager.py create 创建")
        return
    
    # 更新使用计数
    config_file = engine.bosses_dir / ".config.json"
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        if args.boss in config.get("bosses", {}):
            config["bosses"][args.boss]["usage_count"] = \
                config["bosses"][args.boss].get("usage_count", 0) + 1
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)
    
    # 执行模拟
    if args.scenario == 'review':
        result = engine.simulate_review(boss, args.content)
    elif args.scenario == '1on1':
        result = engine.simulate_1on1(boss, args.topic)
    elif args.scenario == 'emergency':
        result = engine.simulate_emergency(boss, args.event, args.severity)
    elif args.scenario == 'speech':
        result = engine.simulate_speech(boss, args.occasion, args.topic)
    else:
        print(f"❌ 未知场景: {args.scenario}")
        return
    
    print(result)


if __name__ == '__main__':
    main()
