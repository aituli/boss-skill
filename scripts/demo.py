#!/usr/bin/env python3
"""
Boss Skill Demo
演示脚本 - 展示如何使用 Boss Skill
"""

import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.boss_manager import BossManager
from tools.scenario_engine import ScenarioEngine
from tools.pattern_analyzer import PatternAnalyzer


def demo_create_boss():
    """演示创建老板Skill"""
    print("=" * 60)
    print("演示1: 创建老板Skill")
    print("=" * 60)
    
    manager = BossManager()
    
    # 非交互式创建示例老板
    boss_info = manager.create_boss(
        name="张总",
        title="CTO",
        style_tags={
            "management_style": "Hands-off",
            "communication_style": "Direct",
            "decision_style": "Data-driven",
            "stress_response": "Angry"
        },
        interactive=False
    )
    
    print(f"\n✅ 已创建老板Skill:")
    print(f"   姓名: {boss_info['name']}")
    print(f"   职位: {boss_info['title']}")
    print(f"   Slug: {boss_info['slug']}")
    print(f"   版本: {boss_info['version']}")
    
    return boss_info['slug']


def demo_review(slug: str):
    """演示方案预审"""
    print("\n" + "=" * 60)
    print("演示2: 方案汇报预审 (review)")
    print("=" * 60)
    
    engine = ScenarioEngine()
    boss = engine.load_boss(slug)
    
    if not boss:
        print(f"❌ 老板Skill '{slug}' 不存在")
        return
    
    content = "计划投入100万做Q3用户增长，预计带来50万新用户，ROI 150%"
    
    print(f"\n方案内容: {content}\n")
    print("-" * 60)
    
    result = engine.simulate_review(boss, content)
    print(result)


def demo_1on1(slug: str):
    """演示1on1模拟"""
    print("\n" + "=" * 60)
    print("演示3: 1on1沟通模拟 (1on1)")
    print("=" * 60)
    
    engine = ScenarioEngine()
    boss = engine.load_boss(slug)
    
    if not boss:
        print(f"❌ 老板Skill '{slug}' 不存在")
        return
    
    topic = "想申请加薪20%，过去一年业绩超额完成30%"
    
    print(f"\n话题: {topic}\n")
    print("-" * 60)
    
    result = engine.simulate_1on1(boss, topic)
    print(result)


def demo_emergency(slug: str):
    """演示突发情况应对"""
    print("\n" + "=" * 60)
    print("演示4: 突发情况应对 (emergency)")
    print("=" * 60)
    
    engine = ScenarioEngine()
    boss = engine.load_boss(slug)
    
    if not boss:
        print(f"❌ 老板Skill '{slug}' 不存在")
        return
    
    event = "线上P0级bug影响10万用户，已经修复但需要2小时才能全量恢复"
    
    print(f"\n事件: {event}\n")
    print("-" * 60)
    
    result = engine.simulate_emergency(boss, event, severity="high")
    print(result)


def demo_speech(slug: str):
    """演示演讲稿生成"""
    print("\n" + "=" * 60)
    print("演示5: 演讲稿生成 (speech)")
    print("=" * 60)
    
    engine = ScenarioEngine()
    boss = engine.load_boss(slug)
    
    if not boss:
        print(f"❌ 老板Skill '{slug}' 不存在")
        return
    
    occasion = "年会"
    topic = "Q4动员"
    
    print(f"\n场合: {occasion}")
    print(f"主题: {topic}\n")
    print("-" * 60)
    
    result = engine.simulate_speech(boss, occasion, topic)
    print(result)


def demo_list_bosses():
    """演示列出所有老板Skill"""
    print("\n" + "=" * 60)
    print("演示6: 列出所有老板Skill")
    print("=" * 60)
    
    manager = BossManager()
    bosses = manager.list_bosses()
    
    if not bosses:
        print("\n暂无老板Skill")
        return
    
    print(f"\n共 {len(bosses)} 个老板Skill:\n")
    print(f"{'Slug':<15} {'姓名':<10} {'职位':<15} {'版本':<8}")
    print("-" * 60)
    
    for boss in bosses:
        print(f"{boss['slug']:<15} {boss['name']:<10} "
              f"{boss.get('title', '-'):<15} {boss['version']:<8}")


def demo_analyze_patterns(slug: str):
    """演示行为模式分析"""
    print("\n" + "=" * 60)
    print("演示7: 行为模式分析")
    print("=" * 60)
    
    analyzer = PatternAnalyzer()
    
    # 模拟一些数据
    test_data = {
        "messages": [
            "这个数据不错，再想想怎么放大",
            "数据呢？我要看到具体的数字",
            "简单说两句，这个项目我很看好",
            "再想想，还有优化的空间",
            "最坏的情况是什么？想过吗？",
            "做好了给你升职加薪",
            "我再说一遍，数据是第一位的",
            "你听懂了吗？",
        ]
    }
    
    # 更新模式
    patterns = analyzer.analyze_boss(slug, test_data)
    
    # 打印分析结果
    analyzer.print_analysis_report(slug)


def main():
    """主函数"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    🎩 Boss Skill Demo                        ║
║                                                              ║
║  本演示展示 Boss Skill 的核心功能：                          ║
║  1. 创建老板Skill                                            ║
║  2. 方案汇报预审 (review)                                    ║
║  3. 1on1沟通模拟 (1on1)                                      ║
║  4. 突发情况应对 (emergency)                                 ║
║  5. 演讲稿生成 (speech)                                      ║
║  6. 列出所有老板Skill                                        ║
║  7. 行为模式分析                                             ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    # 创建老板Skill
    slug = demo_create_boss()
    
    # 演示各种场景
    demo_review(slug)
    demo_1on1(slug)
    demo_emergency(slug)
    demo_speech(slug)
    
    # 列出演示
    demo_list_bosses()
    
    # 分析演示
    demo_analyze_patterns(slug)
    
    print("\n" + "=" * 60)
    print("演示完成！")
    print("=" * 60)
    print(f"""
你可以继续使用以下命令：

  # 交互式创建新的老板Skill
  python tools/boss_manager.py create

  # 使用已有老板Skill进行场景模拟
  python tools/scenario_engine.py review {slug} "你的方案内容"
  python tools/scenario_engine.py 1on1 {slug} "你想聊的话题"
  python tools/scenario_engine.py emergency {slug} "突发事件"

更多信息请查看：
  - SKILL.md - Skill 说明文档
  - README.md - 项目介绍
  - docs/API.md - API 文档
""")


if __name__ == '__main__':
    main()
