# Boss Skill API 文档

## 概述

Boss Skill 提供命令行工具和 Python API 两种使用方式。

## Python API

### BossManager

管理老板Skill的创建、列表、删除等操作。

#### 初始化

```python
from tools.boss_manager import BossManager

manager = BossManager(bosses_dir="/path/to/bosses")
```

#### 创建老板Skill

```python
boss_info = manager.create_boss(
    name="张总",
    title="CTO",
    style_tags={
        "management_style": "Hands-off",
        "communication_style": "Direct",
        "decision_style": "Data-driven",
        "stress_response": "Angry"
    },
    interactive=True  # 交互式创建
)
```

返回：
```python
{
    "id": "a1b2c3d4",
    "name": "张总",
    "slug": "zhang",
    "title": "CTO",
    "version": "1.0.0",
    "created_at": "2024-01-15T10:30:00",
    "tags": {...}
}
```

#### 列出所有老板Skill

```python
bosses = manager.list_bosses()
# 返回按创建时间排序的列表
```

#### 获取指定老板Skill

```python
boss = manager.get_boss("zhang")
# 返回单个老板信息或 None
```

#### 删除老板Skill

```python
success = manager.delete_boss("zhang")
# 返回布尔值
```

### ScenarioEngine

场景模拟引擎，模拟老板在不同场景下的反应。

#### 初始化

```python
from tools.scenario_engine import ScenarioEngine

engine = ScenarioEngine(bosses_dir="/path/to/bosses")
```

#### 加载老板档案

```python
boss = engine.load_boss("zhang")
# 返回 BossProfile 对象或 None
```

#### 方案汇报预审

```python
result = engine.simulate_review(
    boss=boss,
    content="计划投入100万做用户增长，预计带来50万新用户",
    context="Q3规划"
)
# 返回模拟结果文本
```

#### 1on1沟通模拟

```python
result = engine.simulate_1on1(
    boss=boss,
    topic="想申请加薪20%",
    context="过去一年业绩超额完成30%"
)
# 返回模拟结果文本
```

#### 突发情况应对

```python
result = engine.simulate_emergency(
    boss=boss,
    event="线上P0级bug影响10万用户，已修复但需要2小时恢复",
    severity="high",  # low/medium/high/critical
    context="双11期间"
)
# 返回模拟结果文本
```

#### 演讲稿生成

```python
result = engine.simulate_speech(
    boss=boss,
    occasion="年会",
    topic="Q4动员"
)
# 返回模拟结果文本
```

### PatternAnalyzer

行为模式分析器，分析老板的行为模式。

#### 初始化

```python
from tools.pattern_analyzer import PatternAnalyzer

analyzer = PatternAnalyzer(bosses_dir="/path/to/bosses")
```

#### 分析老板

```python
patterns = analyzer.analyze_boss(
    slug="zhang",
    source_data={
        "messages": [...],
        "meetings": [...]
    }
)
# 返回行为模式字典
```

#### 情绪周期分析

```python
cycle = analyzer.analyze_emotion_cycle([
    {"time": "2024-01-15T09:00:00", "content": "今天不错"},
    {"time": "2024-01-15T17:00:00", "content": "这个怎么还没完成"},
    ...
])
# 返回情绪周期分析结果
```

#### 生成洞察报告

```python
insights = analyzer.generate_insights("zhang")
# 返回洞察字典
```

## 数据结构

### BossProfile

```python
@dataclass
class BossProfile:
    slug: str           # 唯一标识
    name: str           # 姓名
    title: str          # 职位
    tags: Dict          # 风格标签
    mgmt_content: str   # 管理Skill内容
    persona_content: str # Persona内容
    patterns: Dict      # 行为模式
```

### 风格标签

```python
{
    "management_style": "Hands-off",      # 管理风格
    "communication_style": "Direct",       # 沟通风格
    "decision_style": "Data-driven",       # 决策风格
    "feedback_style": "Blunt",             # 反馈风格
    "motivation_style": "Vision",          # 激励方式
    "stress_response": "Angry",            # 压力表现
    "tech_level": "Tech-savvy",            # 技术程度
    "work_rhythm": "Morning-person"        # 工作节奏
}
```

### 行为模式

```python
{
    "catchphrases": [
        ("再想想", 15),
        ("数据呢", 12),
        ...
    ],
    "anger_signals": [
        "我再说一遍",
        "你听懂了吗"
    ],
    "question_patterns": [
        ("数据[呢\?]?", 20),
        ...
    ],
    "focus_keywords": [
        ("增长", 45),
        ("成本", 32),
        ...
    ]
}
```

## CLI 命令参考

### boss_manager.py

```bash
# 创建
python boss_manager.py create
python boss_manager.py create --name "张总" --title "CTO"
python boss_manager.py create --name "张总" --no-interactive

# 列出
python boss_manager.py list

# 获取详情
python boss_manager.py get zhang

# 删除
python boss_manager.py delete zhang
```

### scenario_engine.py

```bash
# 方案预审
python scenario_engine.py review zhang "方案内容"

# 1on1模拟
python scenario_engine.py 1on1 zhang "话题内容"

# 突发应对
python scenario_engine.py emergency zhang "事件描述"
python scenario_engine.py emergency zhang "事件" --severity critical

# 演讲生成
python scenario_engine.py speech zhang 年会 "Q4动员"
```

### pattern_analyzer.py

```bash
# 分析
python pattern_analyzer.py analyze zhang

# 从数据提取
python pattern_analyzer.py extract zhang --data messages.json
```

## 文件格式

### 管理Skill文件 ({slug}_mgmt.md)

```yaml
---
type: mgmt_skill
boss_name: "张总"
version: "1.0.0"
created_at: "2024-01-15"
tags:
  management_style: Hands-off
  decision_style: Data-driven
---

# 张总的管理Skill

## 战略思维框架
...

## 管理方法论
...

## 沟通套路库
...
```

### Persona文件 ({slug}_persona.md)

```yaml
---
type: persona
boss_name: "张总"
version: "1.0.0"
created_at: "2024-01-15"
tags:
  communication_style: Direct
  stress_response: Angry
---

# 张总的人格Persona

## 权威表现层
...

## 情绪模式层
...
```

### 行为模式文件 ({slug}_patterns.json)

```json
{
  "catchphrases": [
    ["再想想", 15],
    ["数据呢", 12]
  ],
  "anger_signals": [
    "我再说一遍",
    "你听懂了吗"
  ],
  "question_patterns": [
    ["数据[呢\\?]?", 20]
  ]
}
```

## 错误处理

所有 API 方法都遵循以下错误处理模式：

```python
try:
    boss = engine.load_boss("zhang")
    if boss is None:
        print("Boss not found")
except Exception as e:
    print(f"Error: {e}")
```

## 示例代码

### 完整使用示例

```python
from tools.boss_manager import BossManager
from tools.scenario_engine import ScenarioEngine

# 创建管理器
manager = BossManager()

# 创建老板Skill
boss_info = manager.create_boss(
    name="张总",
    title="CTO",
    interactive=False
)

# 创建引擎
engine = ScenarioEngine()

# 加载老板
boss = engine.load_boss("zhang")

# 方案预审
result = engine.simulate_review(
    boss,
    "计划投入100万做用户增长"
)
print(result)

# 1on1模拟
result = engine.simulate_1on1(
    boss,
    "想申请加薪20%"
)
print(result)
```
