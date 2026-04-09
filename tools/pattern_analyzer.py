#!/usr/bin/env python3
"""
Pattern Analyzer
行为模式分析器 - 分析老板的行为模式和关注点
使用标准库，无需额外安装依赖
"""

import os
import sys
import json
import re
import argparse
from collections import Counter
from pathlib import Path
from datetime import datetime

BOSS_DIR = Path(__file__).parent.parent / "bosses"


class PatternAnalyzer:
    """行为模式分析器"""
    
    def __init__(self, boss_slug):
        self.boss_slug = boss_slug
        self.boss_path = BOSS_DIR / boss_slug
        self.config = self._load_config()
        self.data_path = self.boss_path / "data"
        self.data_path.mkdir(exist_ok=True)
    
    def _load_config(self):
        """加载配置"""
        config_file = self.boss_path / "config.json"
        if not config_file.exists():
            raise FileNotFoundError(f"找不到老板Skill配置: {self.boss_slug}")
        
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def analyze_keywords(self, text_data):
        """
        分析关键词频率
        
        Args:
            text_data: 文本数据（如聊天记录、邮件等）
        
        Returns:
            dict: 关键词分析结果
        """
        # 常见业务关键词
        business_keywords = [
            '增长', '收入', '成本', '利润', '用户', '客户',
            '产品', '技术', '运营', '市场', '销售',
            '团队', '管理', '绩效', '目标', 'KPI',
            '风险', '问题', '机会', '挑战', '竞争'
        ]
        
        word_counts = Counter()
        
        for keyword in business_keywords:
            count = text_data.lower().count(keyword)
            if count > 0:
                word_counts[keyword] = count
        
        return dict(word_counts.most_common(10))
    
    def analyze_catchphrases(self, text_data):
        """
        分析口头禅
        
        Args:
            text_data: 文本数据
        
        Returns:
            list: 常见口头禅
        """
        # 常见老板口头禅模式
        patterns = [
            r'(简单说两句.*?)(?:\n|$)',
            r'(这个事我提过很多次了)',
            r'(我不是批评你，但是)',
            r'(再想想)',
            r'(我再说一遍)',
            r'(数据呢)',
            r'(为什么这么想)',
            r'(最坏的情况是什么)',
            r'(做好了.*给你)',
            r'(等.*再说)',
            r'(你听懂了吗)',
            r'(咱们打开天窗说亮话)'
        ]
        
        catchphrases = []
        
        for pattern in patterns:
            matches = re.findall(pattern, text_data, re.IGNORECASE)
            if matches:
                catchphrases.append(matches[0])
        
        # 统计频率
        phrase_counts = Counter(catchphrases)
        return phrase_counts.most_common(5)
    
    def analyze_anger_signals(self, text_data):
        """
        分析发火信号
        
        Args:
            text_data: 文本数据
        
        Returns:
            list: 发火前兆信号
        """
        anger_indicators = [
            '我再说一遍',
            '你听懂了吗',
            '（深呼吸）',
            '（停顿）',
            '算了',
            '我不想再说',
            '就这样吧',
            '你自己看着办'
        ]
        
        signals = []
        for indicator in anger_indicators:
            if indicator in text_data:
                signals.append(indicator)
        
        return signals
    
    def analyze_decision_patterns(self, text_data):
        """
        分析决策模式
        
        Args:
            text_data: 文本数据
        
        Returns:
            dict: 决策模式分析
        """
        # 决策相关关键词
        decision_keywords = {
            'data_driven': ['数据', '指标', '分析', '统计', '报告'],
            'gut_feeling': ['感觉', '直觉', '觉得', '可能', '应该'],
            'consensus': ['讨论', '商量', '意见', '大家', '团队'],
            'fast': ['马上', '立即', '尽快', '现在', '快点'],
            'cautious': ['再看看', '考虑', '研究', '等等', '观察']
        }
        
        pattern_scores = {}
        
        for pattern, keywords in decision_keywords.items():
            score = sum(text_data.count(kw) for kw in keywords)
            pattern_scores[pattern] = score
        
        return pattern_scores
    
    def generate_priority_radar(self, text_data):
        """
        生成优先级雷达
        
        Args:
            text_data: 文本数据
        
        Returns:
            dict: 优先级分析
        """
        priorities = {
            '增长': text_data.count('增长') + text_data.count('growth'),
            '成本': text_data.count('成本') + text_data.count('cost'),
            '体验': text_data.count('体验') + text_data.count('用户体验'),
            '效率': text_data.count('效率') + text_data.count('效能'),
            '质量': text_data.count('质量') + text_data.count('品质'),
            '团队': text_data.count('团队') + text_data.count('人员')
        }
        
        # 归一化到百分比
        total = sum(priorities.values())
        if total > 0:
            priorities = {k: round(v/total*100, 1) for k, v in priorities.items()}
        
        return priorities
    
    def generate_full_report(self, text_data):
        """
        生成完整的分析报告
        
        Args:
            text_data: 文本数据
        
        Returns:
            dict: 完整分析报告
        """
        report = {
            "boss_name": self.config['name'],
            "analysis_date": datetime.now().isoformat(),
            "keyword_analysis": self.analyze_keywords(text_data),
            "catchphrases": self.analyze_catchphrases(text_data),
            "anger_signals": self.analyze_anger_signals(text_data),
            "decision_patterns": self.analyze_decision_patterns(text_data),
            "priority_radar": self.generate_priority_radar(text_data)
        }
        
        # 保存报告
        report_file = self.data_path / "pattern_report.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report


def print_report(report, use_json=False):
    """打印报告"""
    
    if use_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return
    
    print(f"\n{'='*60}")
    print(f"📊 {report['boss_name']} 的行为模式分析报告")
    print(f"{'='*60}")
    print(f"分析日期: {report['analysis_date'][:10]}")
    
    print(f"\n{'─'*60}")
    print("关键词分析 TOP10:")
    for word, count in report['keyword_analysis'].items():
        print(f"  • {word}: {count}次")
    
    print(f"\n{'─'*60}")
    print("口头禅:")
    if report['catchphrases']:
        for phrase, count in report['catchphrases']:
            print(f"  • \"{phrase}\" ({count}次)")
    else:
        print("  (未识别到常见口头禅)")
    
    print(f"\n{'─'*60}")
    print("发火信号:")
    if report['anger_signals']:
        for signal in report['anger_signals']:
            print(f"  ⚠️  {signal}")
    else:
        print("  (未识别到发火信号)")
    
    print(f"\n{'─'*60}")
    print("决策模式:")
    for pattern, score in sorted(report['decision_patterns'].items(), key=lambda x: x[1], reverse=True):
        bar = "█" * min(score, 20)
        print(f"  {pattern:<20} {bar} ({score})")
    
    print(f"\n{'─'*60}")
    print("优先级雷达:")
    for priority, percentage in sorted(report['priority_radar'].items(), key=lambda x: x[1], reverse=True):
        bar = "█" * int(percentage / 5)
        print(f"  {priority:<10} {bar} {percentage}%")
    
    print(f"{'='*60}\n")


def main():
    """命令行入口"""
    
    parser = argparse.ArgumentParser(description='Boss Skill 行为模式分析器')
    parser.add_argument('boss_slug', help='老板Skill的slug')
    parser.add_argument('--file', '-f', help='文本数据文件路径')
    parser.add_argument('--text', '-t', help='直接输入文本')
    parser.add_argument('--report', '-r', action='store_true', help='生成完整报告')
    parser.add_argument('--json', '-j', action='store_true', help='以JSON格式输出')
    
    args = parser.parse_args()
    
    try:
        analyzer = PatternAnalyzer(args.boss_slug)
        
        # 获取文本数据
        if args.file:
            with open(args.file, "r", encoding="utf-8") as f:
                text_data = f.read()
        elif args.text:
            text_data = args.text
        else:
            # 如果没有提供数据，显示现有报告
            report_file = analyzer.data_path / "pattern_report.json"
            if report_file.exists():
                with open(report_file, "r", encoding="utf-8") as f:
                    report = json.load(f)
                print_report(report, args.json)
                return
            else:
                print("提示: 请提供 --file 或 --text 参数进行分析")
                print("示例:")
                print(f"  python3 pattern_analyzer.py {args.boss_slug} --file chat_logs.txt")
                print(f"  python3 pattern_analyzer.py {args.boss_slug} --text '这里输入文本内容'")
                sys.exit(0)
        
        # 生成完整报告
        report = analyzer.generate_full_report(text_data)
        print_report(report, args.json)
        
        if not args.json:
            print(f"✓ 报告已保存到: {analyzer.data_path / 'pattern_report.json'}")
    
    except FileNotFoundError as e:
        print(f"错误: {e}")
        print(f"提示: 使用 'boss_manager create' 创建老板Skill")
        sys.exit(1)
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
