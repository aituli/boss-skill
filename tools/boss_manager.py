#!/usr/bin/env python3
"""
Boss Skill Manager
管理老板Skill的创建、列表、删除等操作
"""

import os
import json
import re
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import argparse


class BossManager:
    """老板Skill管理器"""
    
    def __init__(self, base_dir: str = None):
        """初始化管理器"""
        if base_dir is None:
            self.base_dir = Path(__file__).parent.parent / "bosses"
        else:
            self.base_dir = Path(base_dir)
        
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        # 配置文件路径
        self.config_file = self.base_dir / ".config.json"
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        """加载配置"""
        if self.config_file.exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"bosses": {}}
    
    def _save_config(self):
        """保存配置"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
    
    def _generate_slug(self, name: str) -> str:
        """生成slug"""
        slug = re.sub(r'[^\w\s-]', '', name.lower())
        slug = re.sub(r'[-\s]+', '-', slug)
        return slug.strip('-')
    
    def _generate_id(self, name: str) -> str:
        """生成唯一ID"""
        timestamp = datetime.now().isoformat()
        return hashlib.md5(f"{name}{timestamp}".encode()).hexdigest()[:8]
    
    def create_boss(self, name: str, title: str = "", style_tags: Dict = None, 
                    interactive: bool = True) -> Dict:
        """
        创建新的老板Skill
        """
        slug = self._generate_slug(name)
        boss_id = self._generate_id(name)
        
        # 检查是否已存在
        if slug in self.config["bosses"]:
            print(f"老板Skill '{name}' 已存在 (slug: {slug})")
            return self.config["bosses"][slug]
        
        # 创建老板目录
        boss_dir = self.base_dir / slug
        boss_dir.mkdir(exist_ok=True)
        
        # 基础信息
        boss_info = {
            "id": boss_id,
            "name": name,
            "slug": slug,
            "title": title,
            "version": "1.0.0",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "usage_count": 0,
            "tags": style_tags or {},
            "files": {
                "mgmt": f"{slug}_mgmt.md",
                "persona": f"{slug}_persona.md",
                "patterns": f"{slug}_patterns.json"
            }
        }
        
        if interactive:
            boss_info = self._interactive_intake(boss_info)
        else:
            self._create_default_files(boss_dir, boss_info)
        
        # 保存配置
        self.config["bosses"][slug] = boss_info
        self._save_config()
        
        print(f"成功创建老板Skill: {name} (slug: {slug})")
        return boss_info
    
    def _interactive_intake(self, boss_info: Dict) -> Dict:
        """交互式信息采集"""
        print("\n" + "="*50)
        print("Boss Skill 创建向导")
        print("="*50 + "\n")
        
        name = input(f"老板姓名 [{boss_info['name']}]: ").strip() or boss_info['name']
        boss_info['name'] = name
        
        title = input(f"职位 [{boss_info.get('title', '')}]: ").strip()
        boss_info['title'] = title
        
        # 管理风格标签
        print("\n管理风格标签")
        
        tags = {}
        
        print("\n1. 管理风格:")
        print("   A. Micromanager  B. Hands-off  C. Coach  D. Dictator  E. Laissez-faire")
        choice = input("   选择: ").strip().upper()
        style_map = {'A': 'Micromanager', 'B': 'Hands-off', 'C': 'Coach',
                     'D': 'Dictator', 'E': 'Laissez-faire'}
        tags['management_style'] = style_map.get(choice, 'Hands-off')
        
        print("\n2. 沟通风格:")
        print("   A. Direct  B. Indirect  C. Storyteller  D. Data-driven  E. Emotional")
        choice = input("   选择: ").strip().upper()
        comm_map = {'A': 'Direct', 'B': 'Indirect', 'C': 'Storyteller',
                    'D': 'Data-driven', 'E': 'Emotional'}
        tags['communication_style'] = comm_map.get(choice, 'Direct')
        
        print("\n3. 决策风格:")
        print("   A. Fast  B. Cautious  C. Consensus  D. Gut-feeling  E. Analytical")
        choice = input("   选择: ").strip().upper()
        dec_map = {'A': 'Fast', 'B': 'Cautious', 'C': 'Consensus',
                   'D': 'Gut-feeling', 'E': 'Analytical'}
        tags['decision_style'] = dec_map.get(choice, 'Analytical')
        
        print("\n4. 压力表现:")
        print("   A. Angry  B. Silent  C. Worried  D. Supportive  E. Absent")
        choice = input("   选择: ").strip().upper()
        stress_map = {'A': 'Angry', 'B': 'Silent', 'C': 'Worried',
                      'D': 'Supportive', 'E': 'Absent'}
        tags['stress_response'] = stress_map.get(choice, 'Angry')
        
        boss_info['tags'] = tags
        
        # 经典行为模式
        print("\n经典行为模式")
        
        catchphrases = input("老板的口头禅（用逗号分隔）: ").strip()
        boss_info['catchphrases'] = [p.strip() for p in catchphrases.split(',') if p.strip()]
        
        anger_signals = input("老板发火前的信号（用逗号分隔）: ").strip()
        boss_info['anger_signals'] = [s.strip() for s in anger_signals.split(',') if s.strip()]
        
        # 生成文件
        boss_dir = self.base_dir / boss_info['slug']
        self._create_mgmt_file(boss_dir, boss_info)
        self._create_persona_file(boss_dir, boss_info)
        self._create_patterns_file(boss_dir, boss_info)
        
        return boss_info
    
    def _create_mgmt_file(self, boss_dir: Path, boss_info: Dict):
        """创建管理Skill文件"""
        tags = boss_info.get('tags', {})
        
        content = f"""---
type: mgmt_skill
boss_name: "{boss_info['name']}"
version: "{boss_info['version']}"
created_at: "{boss_info['created_at']}"
tags:
  management_style: {tags.get('management_style', 'Hands-off')}
  decision_style: {tags.get('decision_style', 'Analytical')}
---

# {boss_info['name']}的管理Skill

## 战略思维框架

### 业务优先级判断
- 关注重点：结果导向，数据驱动
- 决策依据：事实和数据优先
- 优先级调整：根据市场变化灵活调整

### 资源分配逻辑
- 投资原则：ROI优先，快速验证
- 预算态度：谨慎但支持有价值的投入
- 风险控制：要求明确的止损点

### 风险评估模型
必问问题：
- 最坏的情况是什么？
- Plan B是什么？
- 如何控制 downside？

## 管理方法论

### 1on1沟通模式
- 频率：根据项目阶段调整
- 风格：{tags.get('management_style', 'Hands-off')}
- 关注点：结果和进展

### 绩效评价标准
- 优秀：超额完成目标 + 主动解决问题
- 合格：完成既定目标
- 不合格：未达目标且无合理原因

### 激励机制
- 主要方式：认可和成长机会
- 反馈风格：直接但有建设性

## 沟通套路库

### 经典话术
"""
        
        for phrase in boss_info.get('catchphrases', [])[:5]:
            content += f'- "{phrase}"\n'
        
        content += """
### 质疑方式
- 「为什么这么想？」
- 「还有别的方案吗？」
- 「数据支撑是什么？」

### 决策信号
- 快速通过：「可以」、「就这么办」
- 需要再考虑：「再看看」、「再想想」
- 即将拒绝：「有难度」、「我再考虑」
"""
        
        mgmt_file = boss_dir / boss_info['files']['mgmt']
        with open(mgmt_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _create_persona_file(self, boss_dir: Path, boss_info: Dict):
        """创建人格Persona文件"""
        tags = boss_info.get('tags', {})
        
        content = f"""---
type: persona
boss_name: "{boss_info['name']}"
version: "{boss_info['version']}"
created_at: "{boss_info['created_at']}"
tags:
  communication_style: {tags.get('communication_style', 'Direct')}
  stress_response: {tags.get('stress_response', 'Angry')}
---

# {boss_info['name']}的人格Persona

## 权威表现层

### 说话方式
- 风格：{tags.get('communication_style', 'Direct')}
- 句式：简洁明了，直击要点
- 回复：及时但简洁

### 称呼习惯
- 对下属：使用姓名或昵称
- 对同级：正式称呼
- 对上级：尊重且专业

## 决策风格层
- 类型：{tags.get('decision_style', 'Analytical')}
- 特点：理性分析，重视数据
- 习惯：需要充分信息才做决定

## 情绪模式层

### 压力表现
- 类型：{tags.get('stress_response', 'Angry')}
- 触发点：目标未达成、重复错误
- 恢复：较快，对事不对人

### 发火前信号
"""
        
        for signal in boss_info.get('anger_signals', []):
            content += f'- {signal}\n'
        
        content += f"""
### 好消息反应
- 表面：认可但保持冷静
- 内在：记录成绩，适时表扬
- 后续：可能增加期望

### 坏消息反应
- 第一反应：询问原因
- 第二反应：要求解决方案
- 最终：根据态度决定是否追责

## 语言风格指南

### 语气特征
- 权威感：中到高
- 直接度：高
- 情感表达：克制

### 常用句式
- 质疑：「为什么...」、「数据呢？」
- 肯定：「可以」、「不错」
- 否定：「再想想」、「还有优化空间」
"""
        
        persona_file = boss_dir / boss_info['files']['persona']
        with open(persona_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _create_patterns_file(self, boss_dir: Path, boss_info: Dict):
        """创建行为模式文件"""
        patterns = {
            "catchphrases": boss_info.get('catchphrases', []),
            "anger_signals": boss_info.get('anger_signals', []),
            "question_patterns": [
                "数据呢？",
                "为什么这么想？",
                "还有别的方案吗？",
                "最坏的情况是什么？"
            ],
            "delay_phrases": [
                "再想想",
                "再看看",
                "过两天再说"
            ]
        }
        
        patterns_file = boss_dir / boss_info['files']['patterns']
        with open(patterns_file, 'w', encoding='utf-8') as f:
            json.dump(patterns, f, ensure_ascii=False, indent=2)
    
    def _create_default_files(self, boss_dir: Path, boss_info: Dict):
        """创建默认文件（非交互模式）"""
        self._create_mgmt_file(boss_dir, boss_info)
        self._create_persona_file(boss_dir, boss_info)
        self._create_patterns_file(boss_dir, boss_info)
    
    def list_bosses(self) -> List[Dict]:
        """列出所有老板Skill"""
        bosses = []
        for slug, info in self.config.get("bosses", {}).items():
            bosses.append(info)
        
        bosses.sort(key=lambda x: x.get('created_at', ''), reverse=True)
        return bosses
    
    def get_boss(self, slug: str) -> Optional[Dict]:
        """获取指定老板Skill"""
        return self.config.get("bosses", {}).get(slug)
    
    def delete_boss(self, slug: str) -> bool:
        """删除老板Skill"""
        if slug not in self.config.get("bosses", {}):
            print(f"老板Skill '{slug}' 不存在")
            return False
        
        boss_dir = self.base_dir / slug
        if boss_dir.exists():
            import shutil
            shutil.rmtree(boss_dir)
        
        del self.config["bosses"][slug]
        self._save_config()
        
        print(f"已删除老板Skill: {slug}")
        return True
    
    def update_usage(self, slug: str):
        """更新使用次数"""
        if slug in self.config.get("bosses", {}):
            self.config["bosses"][slug]["usage_count"] = \
                self.config["bosses"][slug].get("usage_count", 0) + 1
            self.config["bosses"][slug]["updated_at"] = datetime.now().isoformat()
            self._save_config()


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='Boss Skill Manager',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python boss_manager.py create
  python boss_manager.py create --name "张总" --title "CTO" --no-interactive
  python boss_manager.py list
  python boss_manager.py delete zhang
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # create 命令
    create_parser = subparsers.add_parser('create', help='创建新的老板Skill')
    create_parser.add_argument('--name', help='老板姓名')
    create_parser.add_argument('--title', help='职位')
    create_parser.add_argument('--no-interactive', action='store_true', 
                               help='非交互式创建')
    
    # list 命令
    subparsers.add_parser('list', help='列出所有老板Skill')
    
    # delete 命令
    delete_parser = subparsers.add_parser('delete', help='删除老板Skill')
    delete_parser.add_argument('slug', help='老板Skill的slug')
    
    # get 命令
    get_parser = subparsers.add_parser('get', help='获取老板Skill详情')
    get_parser.add_argument('slug', help='老板Skill的slug')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    manager = BossManager()
    
    if args.command == 'create':
        if args.no_interactive:
            if not args.name:
                print("非交互模式需要提供 --name")
                return
            manager.create_boss(
                name=args.name,
                title=args.title or "",
                interactive=False
            )
        else:
            name = args.name or input("老板姓名: ").strip()
            if not name:
                print("需要提供姓名")
                return
            title = args.title or input("职位（可选）: ").strip()
            manager.create_boss(name=name, title=title, interactive=True)
    
    elif args.command == 'list':
        bosses = manager.list_bosses()
        if not bosses:
            print("暂无老板Skill")
            return
        
        print(f"\n{'Slug':<15} {'姓名':<10} {'职位':<15} {'版本':<8}")
        print("-" * 60)
        
        for boss in bosses:
            print(f"{boss['slug']:<15} {boss['name']:<10} "
                  f"{boss.get('title', '-'):<15} {boss['version']:<8}")
    
    elif args.command == 'delete':
        manager.delete_boss(args.slug)
    
    elif args.command == 'get':
        boss = manager.get_boss(args.slug)
        if boss:
            print(json.dumps(boss, ensure_ascii=False, indent=2))
        else:
            print(f"老板Skill '{args.slug}' 不存在")


if __name__ == '__main__':
    main()
