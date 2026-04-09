#!/usr/bin/env python3
"""
Pattern Analyzer
行为模式分析器 - 分析老板的行为模式、情绪周期、决策习惯
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Counter
from collections import defaultdict
from datetime import datetime
import argparse


class PatternAnalyzer:
    """行为模式分析器"""
    
    # 常见口头禅
    COMMON_CATCHPHRASES = [
        '再想想', '我再说一遍', '简单说两句', '数据呢',
        '为什么', '还有别的方案吗', '最坏的情况',
        '做好了给你', '等公司', '我相信你', '你听懂了吗',
        '明白吗', '懂了吗', '不错', '可以', '就这么办'
    ]
    
    # 发火信号词
    ANGER_SIGNALS = [
        '我再说一遍', '你听懂了吗', '深呼吸', '停顿',
        '（沉默）', '语气变冷', '音量提高', '拍桌子'
    ]
    
    # 质疑模式
    QUESTION_PATTERNS = [
        r'数据[呢\?]?',
        r'为什么',
        r'还有别的',
        r'最坏的情况',
        r'plan\s*b',
        r'怎么[解决办]',
        r'责任[在谁]',
    ]
    
    def __init__(self, bosses_dir: str = None):
        """初始化分析器"""
        if bosses_dir is None:
            self.bosses_dir = Path(__file__).parent.parent / "bosses"
        else:
            self.bosses_dir = Path(bosses_dir)
    
    def analyze_boss(self, slug: str, source_data: Dict = None) -> Dict:
        """
        分析老板行为模式
        
        Args:
            slug: 老板slug
            source_data: 可选的原始数据
        
        Returns:
            分析结果
        """
        boss_dir = self.bosses_dir / slug
        patterns_file = boss_dir / f"{slug}_patterns.json"
        
        # 加载已有模式
        existing_patterns = {}
        if patterns_file.exists():
            with open(patterns_file, 'r', encoding='utf-8') as f:
                existing_patterns = json.load(f)
        
        # 如果有新数据，进行分析
        if source_data:
            new_patterns = self._extract_patterns_from_data(source_data)
            existing_patterns.update(new_patterns)
            
            # 保存更新
            with open(patterns_file, 'w', encoding='utf-8') as f:
                json.dump(existing_patterns, f, ensure_ascii=False, indent=2)
        
        return existing_patterns
    
    def _extract_patterns_from_data(self, data: Dict) -> Dict:
        """从数据中提取行为模式"""
        patterns = {
            'catchphrases': [],
            'anger_signals': [],
            'question_patterns': [],
            'focus_keywords': [],
            'decision_indicators': {},
            'emotion_patterns': {},
        }
        
        # 分析消息内容
        messages = data.get('messages', [])
        if messages:
            patterns['catchphrases'] = self._extract_catchphrases(messages)
            patterns['anger_signals'] = self._detect_anger_signals(messages)
            patterns['question_patterns'] = self._extract_question_patterns(messages)
            patterns['focus_keywords'] = self._extract_focus_keywords(messages)
        
        # 分析会议纪要
        meetings = data.get('meetings', [])
        if meetings:
            patterns['decision_indicators'] = self._analyze_decision_patterns(meetings)
        
        return patterns
    
    def _extract_catchphrases(self, messages: List[str]) -> List[Tuple[str, int]]:
        """提取口头禅及频率"""
        phrase_counts = Counter()
        
        for msg in messages:
            for phrase in self.COMMON_CATCHPHRASES:
                if phrase in msg:
                    phrase_counts[phrase] += 1
        
        # 返回频率最高的10个
        return phrase_counts.most_common(10)
    
    def _detect_anger_signals(self, messages: List[str]) -> List[str]:
        """检测发火信号"""
        signals = []
        
        for msg in messages:
            for signal in self.ANGER_SIGNALS:
                if signal in msg:
                    signals.append(signal)
        
        return list(set(signals))  # 去重
    
    def _extract_question_patterns(self, messages: List[str]) -> List[Tuple[str, int]]:
        """提取质疑模式"""
        pattern_counts = Counter()
        
        for msg in messages:
            for pattern in self.QUESTION_PATTERNS:
                if re.search(pattern, msg, re.IGNORECASE):
                    pattern_counts[pattern] += 1
        
        return pattern_counts.most_common(5)
    
    def _extract_focus_keywords(self, messages: List[str], top_n: int = 10) -> List[Tuple[str, int]]:
        """提取关注关键词"""
        # 业务关键词列表
        business_keywords = [
            '增长', '成本', '收入', '利润', '用户', '留存', '转化',
            '体验', '效率', '质量', '风险', '竞争', '市场',
            '产品', '技术', '运营', '销售', '客户'
        ]
        
        keyword_counts = Counter()
        
        for msg in messages:
            for keyword in business_keywords:
                if keyword in msg:
                    keyword_counts[keyword] += 1
        
        return keyword_counts.most_common(top_n)
    
    def _analyze_decision_patterns(self, meetings: List[Dict]) -> Dict:
        """分析决策模式"""
        indicators = {
            'avg_decision_time': 0,  # 平均决策时间（天）
            'data_driven_ratio': 0,  # 数据驱动决策比例
            'consensus_ratio': 0,    # 协商决策比例
            'reversal_rate': 0,      # 决策反转率
        }
        
        # TODO: 实现具体的决策模式分析逻辑
        
        return indicators
    
    def analyze_emotion_cycle(self, messages: List[Dict]) -> Dict:
        """
        分析情绪周期
        
        Args:
            messages: 带时间戳的消息列表，每项包含 'time' 和 'content'
        
        Returns:
            情绪周期分析结果
        """
        # 按小时和星期几分组的情绪统计
        hourly_emotion = defaultdict(list)
        daily_emotion = defaultdict(list)
        
        for msg in messages:
            time_str = msg.get('time', '')
            content = msg.get('content', '')
            
            try:
                dt = datetime.fromisoformat(time_str)
                hour = dt.hour
                weekday = dt.weekday()  # 0=Monday, 6=Sunday
                
                # 简单情绪分析（基于关键词）
                emotion = self._detect_emotion(content)
                
                hourly_emotion[hour].append(emotion)
                daily_emotion[weekday].append(emotion)
            except:
                continue
        
        # 计算各时段平均情绪
        hourly_avg = {}
        for hour, emotions in hourly_emotion.items():
            hourly_avg[hour] = sum(emotions) / len(emotions) if emotions else 0
        
        daily_avg = {}
        for day, emotions in daily_emotion.items():
            daily_avg[day] = sum(emotions) / len(emotions) if emotions else 0
        
        return {
            'hourly_pattern': hourly_avg,
            'daily_pattern': daily_avg,
            'best_communication_time': self._find_best_time(hourly_avg, daily_avg),
            'avoid_time': self._find_avoid_time(hourly_avg, daily_avg),
        }
    
    def _detect_emotion(self, content: str) -> float:
        """
        检测情绪值 (-1 到 1)
        -1: 非常负面 (发火)
        0: 中性
        1: 非常正面 (高兴)
        """
        emotion = 0.0
        
        # 负面信号
        negative_signals = [
            '不行', '错了', '问题', '怎么回事', '为什么', '糟糕',
            '严重', '必须', '立即', '马上', '怎么会'
        ]
        
        # 正面信号
        positive_signals = [
            '不错', '很好', '优秀', '赞', '棒', '可以', '满意',
            '谢谢', '感谢', '做得好'
        ]
        
        for signal in negative_signals:
            if signal in content:
                emotion -= 0.2
        
        for signal in positive_signals:
            if signal in content:
                emotion += 0.2
        
        # 限制在 -1 到 1 之间
        return max(-1, min(1, emotion))
    
    def _find_best_time(self, hourly: Dict, daily: Dict) -> str:
        """找出最佳沟通时间"""
        # 找平均情绪最高的时段
        if hourly:
            best_hour = max(hourly.items(), key=lambda x: x[1])[0]
        else:
            best_hour = 10  # 默认上午10点
        
        if daily:
            best_day = max(daily.items(), key=lambda x: x[1])[0]
        else:
            best_day = 0  # 默认周一
        
        day_names = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        
        return f"{day_names[best_day]}上午{best_hour}:00左右"
    
    def _find_avoid_time(self, hourly: Dict, daily: Dict) -> str:
        """找出避免沟通的时间"""
        # 找平均情绪最低的时段
        if hourly:
            worst_hour = min(hourly.items(), key=lambda x: x[1])[0]
        else:
            worst_hour = 17  # 默认下午5点
        
        if daily:
            worst_day = min(daily.items(), key=lambda x: x[1])[0]
        else:
            worst_day = 4  # 默认周五
        
        day_names = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        
        return f"{day_names[worst_day]}下午{worst_hour}:00左右"
    
    def generate_insights(self, slug: str) -> Dict:
        """生成洞察报告"""
        patterns = self.analyze_boss(slug)
        
        insights = {
            'communication_style': self._infer_communication_style(patterns),
            'decision_style': self._infer_decision_style(patterns),
            'pressure_points': self._identify_pressure_points(patterns),
            'motivation_triggers': self._identify_motivation_triggers(patterns),
            'warning_signals': self._identify_warning_signals(patterns),
        }
        
        return insights
    
    def _infer_communication_style(self, patterns: Dict) -> str:
        """推断沟通风格"""
        catchphrases = patterns.get('catchphrases', [])
        
        # 基于口头禅推断
        direct_indicators = ['不行', '错了', '就这么办', '立即']
        indirect_indicators = ['再想想', '再看看', '考虑一下']
        
        direct_score = sum(1 for phrase, _ in catchphrases if any(ind in phrase for ind in direct_indicators))
        indirect_score = sum(1 for phrase, _ in catchphrases if any(ind in phrase for ind in indirect_indicators))
        
        if direct_score > indirect_score:
            return "Direct（直接型）"
        elif indirect_score > direct_score:
            return "Indirect（含蓄型）"
        else:
            return "Balanced（平衡型）"
    
    def _infer_decision_style(self, patterns: Dict) -> str:
        """推断决策风格"""
        questions = patterns.get('question_patterns', [])
        
        data_indicators = ['数据', '指标', '数字']
        gut_indicators = ['觉得', '感觉', '直觉']
        
        data_score = sum(1 for q, _ in questions if any(ind in q for ind in data_indicators))
        gut_score = sum(1 for q, _ in questions if any(ind in q for ind in gut_indicators))
        
        if data_score > gut_score:
            return "Data-driven（数据驱动型）"
        elif gut_score > data_score:
            return "Gut-feeling（直觉型）"
        else:
            return "Analytical（分析型）"
    
    def _identify_pressure_points(self, patterns: Dict) -> List[str]:
        """识别压力触发点"""
        anger_signals = patterns.get('anger_signals', [])
        
        # 基于发火信号推断压力点
        pressure_points = []
        
        if any('数据' in str(signal) for signal in anger_signals):
            pressure_points.append("数据不准确/缺失")
        if any('重复' in str(signal) for signal in anger_signals):
            pressure_points.append("重复犯错")
        if any('延期' in str(signal) or 'delay' in str(signal) for signal in anger_signals):
            pressure_points.append("项目延期")
        
        if not pressure_points:
            pressure_points = ["目标未达成", "质量问题", "沟通不畅"]
        
        return pressure_points
    
    def _identify_motivation_triggers(self, patterns: Dict) -> List[str]:
        """识别激励触发点"""
        catchphrases = patterns.get('catchphrases', [])
        
        triggers = []
        
        vision_indicators = ['做好了', '未来', '相信', '一定']
        recognition_indicators = ['不错', '很好', '优秀']
        
        vision_score = sum(count for phrase, count in catchphrases if any(ind in phrase for ind in vision_indicators))
        recognition_score = sum(count for phrase, count in catchphrases if any(ind in phrase for ind in recognition_indicators))
        
        if vision_score > 0:
            triggers.append("愿景激励（画饼）")
        if recognition_score > 0:
            triggers.append("认可表扬")
        
        if not triggers:
            triggers = ["结果导向的认可", "成长机会"]
        
        return triggers
    
    def _identify_warning_signals(self, patterns: Dict) -> List[str]:
        """识别警告信号"""
        signals = patterns.get('anger_signals', [])
        
        if not signals:
            return [
                "语气变冷",
                "回复变慢",
                "使用'再想想'",
                "追问细节"
            ]
        
        return signals[:5]
    
    def print_analysis_report(self, slug: str):
        """打印分析报告"""
        patterns = self.analyze_boss(slug)
        insights = self.generate_insights(slug)
        
        print(f"\n{'='*60}")
        print(f"📊 老板行为模式分析报告: {slug}")
        print(f"{'='*60}\n")
        
        print("【口头禅Top5】")
        for phrase, count in patterns.get('catchphrases', [])[:5]:
            print(f"  • \"{phrase}\" - 出现 {count} 次")
        
        print("\n【质疑模式】")
        for pattern, count in patterns.get('question_patterns', [])[:5]:
            print(f"  • {pattern} - {count} 次")
        
        print("\n【关注关键词】")
        for keyword, count in patterns.get('focus_keywords', [])[:5]:
            print(f"  • {keyword} - {count} 次")
        
        print("\n【洞察】")
        print(f"  沟通风格: {insights['communication_style']}")
        print(f"  决策风格: {insights['decision_style']}")
        
        print("\n  压力触发点:")
        for point in insights['pressure_points']:
            print(f"    • {point}")
        
        print("\n  激励触发点:")
        for trigger in insights['motivation_triggers']:
            print(f"    • {trigger}")
        
        print("\n  警告信号:")
        for signal in insights['warning_signals']:
            print(f"    • {signal}")
        
        print(f"\n{'='*60}\n")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='Pattern Analyzer - 行为模式分析器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 分析现有老板Skill
  python pattern_analyzer.py analyze zhang
  
  # 从数据中提取新模式
  python pattern_analyzer.py extract zhang --data messages.json
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # analyze 命令
    analyze_parser = subparsers.add_parser('analyze', help='分析老板行为模式')
    analyze_parser.add_argument('boss', help='老板slug')
    
    # extract 命令
    extract_parser = subparsers.add_parser('extract', help='从数据提取模式')
    extract_parser.add_argument('boss', help='老板slug')
    extract_parser.add_argument('--data', required=True, help='数据文件路径(JSON)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    analyzer = PatternAnalyzer()
    
    if args.command == 'analyze':
        analyzer.print_analysis_report(args.boss)
    
    elif args.command == 'extract':
        # 加载数据
        with open(args.data, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        patterns = analyzer.analyze_boss(args.boss, data)
        print(f"✅ 已从数据中提取模式并保存")
        print(json.dumps(patterns, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
