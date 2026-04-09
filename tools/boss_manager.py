#!/usr/bin/env python3
"""
Boss Skill Manager
用于创建、列出、删除老板Skill的管理工具
使用标准库，无需额外安装依赖
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

BOSS_DIR = Path(__file__).parent.parent / "bosses"


def ensure_boss_dir():
    """确保bosses目录存在"""
    BOSS_DIR.mkdir(parents=True, exist_ok=True)


def generate_slug(name):
    """生成slug"""
    return name.lower().replace(" ", "-").replace("_", "-")


def cmd_create(args):
    """创建一个新的老板Skill"""
    
    name = args.name or input("老板姓名/称呼: ")
    title = args.title or input("职位: ")
    company = args.company or input("公司/部门: ")
    style = args.style or input("管理风格 (micromanager/hands-off/coach/dictator/laissez-faire): ")
    decision = args.decision or input("决策风格 (fast/cautious/consensus/gut-feeling/analytical): ")
    
    slug = generate_slug(name)
    boss_path = BOSS_DIR / slug
    
    if boss_path.exists():
        print(f"错误: 老板Skill '{name}' 已存在")
        sys.exit(1)
    
    # 创建目录结构
    boss_path.mkdir(parents=True)
    (boss_path / "data").mkdir()
    
    # 创建基础配置
    config = {
        "name": name,
        "slug": slug,
        "title": title,
        "company": company,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "management_style": style,
        "decision_style": decision,
        "communication_style": "direct",
        "version": 1
    }
    
    with open(boss_path / "config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    # 创建mgmt_skill.md模板
    mgmt_template = f"""# Management Skill: {name}

## 1. 战略思维框架

### 1.1 业务优先级判断
- 第一优先级：TBD
- 决策权重：
  - 收入增长：40%
  - 成本控制：30%
  - 用户体验：20%
  - 团队稳定：10%

### 1.2 资源分配逻辑
- 人员招聘标准：TBD
- 预算分配原则：TBD
- 技术投入倾向：TBD

### 1.3 风险评估模型
- 高风险信号：TBD
- 风险容忍度：TBD
- 应急预案偏好：TBD

## 2. 管理方法论

### 2.1 1on1沟通模式
- 频率：TBD
- 典型议程：TBD
- 关注重点：TBD
- 常问问题：TBD

### 2.2 绩效评价标准
- 优秀员工特征：TBD
- 警告信号：TBD
- 晋升考量因素：TBD

### 2.3 激励机制
- 物质激励偏好：TBD
- 精神激励方式：TBD
- 团队建设风格：TBD

## 3. 业务知识体系
TBD

## 4. 沟通套路库
TBD
"""
    
    with open(boss_path / "mgmt_skill.md", "w", encoding="utf-8") as f:
        f.write(mgmt_template)
    
    # 创建persona.md模板
    persona_template = f"""# Persona: {name}

## Layer 1: 权威表现层

### 说话方式
- 正式场合用语特征：TBD
- 非正式场合用语特征：TBD
- 微信/即时通讯风格：TBD
- 邮件风格：TBD
- 会议发言风格：TBD

### 称呼习惯
- 对下属的称呼方式：TBD
- 希望被如何称呼：TBD

### 非语言特征
- 常用表情包类型：TBD
- 标点符号习惯：TBD
- 回复速度特征：TBD

## Layer 2: 决策风格层

### 决策类型
primary_style: {decision}
secondary_style: TBD

### 决策特征
- 信息收集习惯：TBD
- 思考时间：TBD
- 决策依据权重：TBD

## Layer 3: 情绪模式层

### 基础情绪特征
- 默认情绪状态：TBD
- 情绪恢复速度：TBD

### 压力反应
- 轻度压力表现：TBD
- 中度压力表现：TBD
- 重度压力表现：TBD

### 情绪信号
- 发火前兆：TBD
- 心情好的信号：TBD
- 疲惫/不在状态的信号：TBD

## Layer 4: 人际策略层

### 向下管理策略
- 对不同绩效员工的区别对待：TBD
- 信任建立方式：TBD
- 权威维护方式：TBD

### 向上管理风格
- 对上级汇报的风格：TBD
- 争取资源的方式：TBD

## Layer 5: 身份认同层

### 自我认知
- 管理者身份认同：TBD
- 专业身份认同：TBD

### 价值观
- 工作中最看重的品质：TBD
- 不能容忍的行为：TBD
"""
    
    with open(boss_path / "persona.md", "w", encoding="utf-8") as f:
        f.write(persona_template)
    
    print(f"\n{'='*50}")
    print(f"✓ 成功创建老板Skill")
    print(f"{'='*50}")
    print(f"名称: {name}")
    print(f"Slug: {slug}")
    print(f"职位: {title}")
    print(f"公司: {company}")
    print(f"管理风格: {style}")
    print(f"决策风格: {decision}")
    print(f"\n提示: 请编辑以下文件完善Skill内容:")
    print(f"  - {boss_path / 'mgmt_skill.md'}")
    print(f"  - {boss_path / 'persona.md'}")
    print(f"{'='*50}\n")


def cmd_list(args):
    """列出所有老板Skill"""
    
    bosses = []
    if BOSS_DIR.exists():
        for boss_dir in BOSS_DIR.iterdir():
            if boss_dir.is_dir():
                config_file = boss_dir / "config.json"
                if config_file.exists():
                    with open(config_file, "r", encoding="utf-8") as f:
                        config = json.load(f)
                        bosses.append(config)
    
    if not bosses:
        print("暂无老板Skill，使用 'boss_manager create' 创建一个")
        return
    
    print(f"\n{'='*80}")
    print(f"{'Slug':<20} {'姓名':<15} {'职位':<20} {'管理风格':<15}")
    print(f"{'='*80}")
    
    for boss in sorted(bosses, key=lambda x: x['created_at'], reverse=True):
        print(f"{boss['slug']:<20} {boss['name']:<15} {boss['title']:<20} {boss['management_style']:<15}")
    
    print(f"{'='*80}\n")


def cmd_show(args):
    """查看指定老板Skill的详情"""
    
    slug = args.slug
    boss_path = BOSS_DIR / slug
    config_file = boss_path / "config.json"
    
    if not config_file.exists():
        print(f"错误: 找不到老板Skill '{slug}'")
        sys.exit(1)
    
    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    print(f"\n{'='*50}")
    print(f"老板Skill: {config['name']}")
    print(f"{'='*50}")
    print(f"名称: {config['name']}")
    print(f"Slug: {config['slug']}")
    print(f"职位: {config['title']}")
    print(f"公司: {config['company']}")
    print(f"管理风格: {config['management_style']}")
    print(f"决策风格: {config['decision_style']}")
    print(f"版本: {config['version']}")
    print(f"创建时间: {config['created_at'][:10]}")
    print(f"{'='*50}\n")


def cmd_delete(args):
    """删除指定的老板Skill"""
    
    slug = args.slug
    boss_path = BOSS_DIR / slug
    
    if not boss_path.exists():
        print(f"错误: 找不到老板Skill '{slug}'")
        sys.exit(1)
    
    confirm = input(f"确定要删除老板Skill '{slug}' 吗? (yes/no): ")
    if confirm.lower() != 'yes':
        print("已取消删除")
        return
    
    import shutil
    shutil.rmtree(boss_path)
    
    print(f"✓ 已删除老板Skill '{slug}'")


def main():
    """主函数"""
    ensure_boss_dir()
    
    parser = argparse.ArgumentParser(description='Boss Skill Manager - 管理你的老板Skill')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # create 命令
    create_parser = subparsers.add_parser('create', help='创建一个新的老板Skill')
    create_parser.add_argument('--name', help='老板的姓名或常用称呼')
    create_parser.add_argument('--title', help='职位级别，如"技术总监"')
    create_parser.add_argument('--company', help='所在公司或部门')
    create_parser.add_argument('--style', 
                              choices=['micromanager', 'hands-off', 'coach', 'dictator', 'laissez-faire'],
                              help='管理风格类型')
    create_parser.add_argument('--decision',
                              choices=['fast', 'cautious', 'consensus', 'gut-feeling', 'analytical'],
                              help='决策风格类型')
    
    # list 命令
    list_parser = subparsers.add_parser('list', help='列出所有老板Skill')
    
    # show 命令
    show_parser = subparsers.add_parser('show', help='查看指定老板Skill的详情')
    show_parser.add_argument('slug', help='老板Skill的slug')
    
    # delete 命令
    delete_parser = subparsers.add_parser('delete', help='删除指定的老板Skill')
    delete_parser.add_argument('slug', help='老板Skill的slug')
    
    args = parser.parse_args()
    
    if args.command == 'create':
        cmd_create(args)
    elif args.command == 'list':
        cmd_list(args)
    elif args.command == 'show':
        cmd_show(args)
    elif args.command == 'delete':
        cmd_delete(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()