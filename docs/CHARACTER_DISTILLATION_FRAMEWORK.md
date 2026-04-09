# 人物类型蒸馏框架 (Character Distillation Framework)

> 从本次 boss-skill 项目实践中抽象出的通用方法论，适用于任何人物类型的AI Skill生成。

---

## 一、框架概述

### 1.1 什么是人物类型蒸馏？

将真实人物的行为模式、思维方式、沟通风格等特征，通过结构化的数据采集和分析，转化为可运行的AI Skill的过程。

### 1.2 适用场景

| 场景 | 示例 | 价值 |
|------|------|------|
| **职场** | 同事、老板、下属 | 理解工作风格，优化协作 |
| **亲密关系** | 女友、男友、配偶 | 理解情感需求，改善沟通 |
| **家庭** | 父母、小孩 | 理解成长阶段，科学养育 |
| **社交** | 朋友、导师 | 学习优点，维系关系 |
| **宠物** | 猫、狗 | 理解行为，更好陪伴 |

### 1.3 核心原则

1. **基于事实，不做臆测** - 从真实数据中提取，而非想象
2. **结构化而非碎片化** - 建立多维度标签体系
3. **动态进化，非一成不变** - 支持持续更新迭代
4. **理解而非操控** - 目的是更好相处，不是操控对方

---

## 二、标准流程（7步法）

### Step 1: 需求定义 (Define)

**目标**: 明确要蒸馏的人物类型和使用场景

**关键问题**:
- 这个人物类型是谁？（角色定位）
- 为什么要蒸馏？（核心痛点）
- 用来做什么？（使用场景）
- 和现有方案的区别？（差异化价值）

**交付物**:
```markdown
## 项目定位
- 人物类型: [例如：老板]
- 核心目标: [例如：理解管理风格，提前预判反应]
- 使用场景: [例如：汇报前预审、争取资源、突发应对]
- 核心价值: [例如：提升向上管理能力]
```

---

### Step 2: 维度设计 (Design)

**目标**: 设计多维度标签体系，全面刻画人物特征

**方法**: 8维分析法

| 维度 | 说明 | 示例标签 |
|------|------|----------|
| **行为风格** | 日常行为模式 | 主动/被动、规律/随性 |
| **决策模式** | 如何做决定 | 理性/感性、快速/谨慎 |
| **沟通方式** | 表达和理解信息的方式 | 直接/含蓄、详细/简洁 |
| **情绪特征** | 情绪反应模式 | 稳定/波动、外放/内敛 |
| **价值观念** | 重视什么，轻视什么 | 成就/关系、创新/稳定 |
| **互动策略** | 与人交往的模式 | 亲密/疏离、主导/配合 |
| **压力反应** | 面对压力的表现 | 焦虑/冷静、战斗/逃避 |
| **成长背景** | 影响性格的关键因素 | 家庭、教育、经历 |

**交付物**:
```python
class CharacterDimensions:
    behavior_style: Enum  # 行为风格
    decision_pattern: Enum  # 决策模式
    communication_style: Enum  # 沟通方式
    emotion_traits: Enum  # 情绪特征
    value_system: Enum  # 价值观念
    interaction_strategy: Enum  # 互动策略
    stress_response: Enum  # 压力反应
    background_factors: List[str]  # 成长背景
```

---

### Step 3: 数据采集 (Collect)

**目标**: 收集人物的真实行为数据

**数据源类型**:

| 数据源 | 适用场景 | 采集方式 |
|--------|----------|----------|
| **聊天记录** | 职场/亲密关系 | 导出微信/钉钉/飞书记录 |
| **语音/视频** | 家庭/亲密关系 | 录音转文字（需授权） |
| **社交动态** | 朋友/亲密关系 | 朋友圈、微博、小红书 |
| **行为观察** | 小孩/宠物 | 日常记录、行为日志 |
| **第三方反馈** | 职场/家庭 | 问卷、访谈共同熟人 |
| **自我描述** | 所有场景 | 引导对方做性格测试 |

**采集原则**:
1. **隐私优先** - 获得明确授权，敏感数据脱敏
2. **时间跨度** - 至少3个月数据，覆盖不同情境
3. **情境多样** - 包含平时、压力、开心等不同状态
4. **数量充足** - 至少100+条有效交互记录

**交付物**:
```
data/
├── raw/
│   ├── chat_logs/          # 原始聊天记录
│   ├── voice_transcripts/  # 语音转录
│   └── observations/       # 观察笔记
└── processed/
    ├── cleaned_data.json   # 清洗后数据
    └── tagged_data.json    # 标注后数据
```

---

### Step 4: 模式分析 (Analyze)

**目标**: 从数据中提取行为模式和特征标签

**分析方法**:

#### 4.1 关键词分析
```python
def analyze_keywords(text_data):
    """提取高频关键词，了解关注点"""
    # 例如："增长"出现50次，"成本"出现30次 → 关注业务增长
```

#### 4.2 口头禅识别
```python
def analyze_catchphrases(text_data):
    """识别重复出现的表达"""
    # 例如："数据呢？"、"再想想"、"我再说一遍"
```

#### 4.3 情绪周期分析
```python
def analyze_emotion_cycle(text_data, timestamps):
    """分析情绪波动规律"""
    # 例如：周一上午脾气好，周五下午暴躁
```

#### 4.4 决策模式识别
```python
def analyze_decision_pattern(interactions):
    """分析如何做决定"""
    # 数据驱动 vs 直觉型，快速 vs 谨慎
```

#### 4.5 关系亲疏分析
```python
def analyze_relationship_dynamics(interactions):
    """分析对不同人的区别对待"""
    # 对谁更耐心，对谁更严格
```

**交付物**:
```json
{
  "analysis_report": {
    "keyword_frequency": {...},
    "catchphrases": [...],
    "emotion_patterns": {...},
    "decision_style": "...",
    "communication_patterns": {...}
  }
}
```

---

### Step 5: 模型构建 (Model)

**目标**: 构建AI Skill的核心模型

**双轨架构**（推荐）:

```
┌─────────────────────────────────────────┐
│           Character Skill                │
├───────────────────┬─────────────────────┤
│   Capability      │   Personality       │
│   (能力层)        │   (人格层)          │
├───────────────────┼─────────────────────┤
│ • 知识技能        │ • 行为风格          │
│ • 思维方式        │ • 情绪模式          │
│ • 决策逻辑        │ • 沟通偏好          │
│ • 专业经验        │ • 价值观念          │
└───────────────────┴─────────────────────┘
```

**构建步骤**:

1. **Capability层构建**
   - 提取专业知识和技能
   - 总结思维框架和方法论
   - 整理常用工具和套路

2. **Personality层构建**
   - 定义行为风格标签
   - 描述情绪反应模式
   - 总结沟通偏好

3. **融合规则定义**
   - 不同情境下的行为选择
   - 情绪对决策的影响权重
   - 个性化表达生成规则

**交付物**:
```
character_skill/
├── capability.md      # 能力层定义
├── personality.md     # 人格层定义
├── fusion_rules.json  # 融合规则
└── scenarios/         # 场景定义
    ├── scenario_1.md
    └── scenario_2.md
```

---

### Step 6: 场景实现 (Implement)

**目标**: 实现具体的使用场景

**常见场景模板**:

| 场景 | 输入 | 输出 | 示例 |
|------|------|------|------|
| **方案预审** | 你的方案/计划 | 对方可能的反应、质疑、建议 | 向老板汇报前预审 |
| **沟通模拟** | 想谈的话题 | 对话模拟、最佳话术、时机建议 | 和伴侣谈重要事情 |
| **冲突应对** | 冲突情境 | 对方的情绪预测、和解策略 | 和孩子闹矛盾后 |
| **礼物推荐** | 场合+预算 | 符合对方喜好的礼物建议 | 给女友选生日礼物 |
| **学习模仿** | 具体技能 | 对方的做事方式和技巧 | 学习老板的管理艺术 |

**实现步骤**:

1. **场景定义** - 明确输入输出格式
2. **Prompt工程** - 设计场景模拟Prompt
3. **规则引擎** - 实现基于标签的决策逻辑
4. **输出生成** - 生成符合人物风格的回复

**代码结构**:
```python
class ScenarioEngine:
    def simulate(self, scenario_type, input_data):
        # 1. 加载人物模型
        capability = load_capability()
        personality = load_personality()
        
        # 2. 确定态度和情绪
        attitude = personality.decide_attitude(scenario_type)
        emotion = personality.decide_emotion(input_data)
        
        # 3. 生成内容
        content = capability.generate_response(scenario_type, input_data)
        
        # 4. 融合输出
        return merge_with_style(content, attitude, emotion)
```

---

### Step 7: 迭代优化 (Iterate)

**目标**: 持续改进模型准确性

**迭代机制**:

#### 7.1 反馈收集
```python
def collect_feedback(skill_output, user_rating, correction):
    """收集用户对输出的反馈"""
    # 存储到反馈数据库
```

#### 7.2 模型更新
```python
def update_model(feedback_data):
    """基于反馈更新模型"""
    # 增量学习，不覆盖原有结论
```

#### 7.3 版本管理
```python
class VersionManager:
    def create_version(self, skill_data):
        """创建新版本快照"""
    
    def rollback(self, version_id):
        """回滚到历史版本"""
```

**迭代周期**:
- **每日**: 自动收集反馈
- **每周**: 小幅度调整参数
- **每月**: 基于新数据重新分析
- **每季**: 全面评估和重大更新

---

## 三、技术架构

### 3.1 项目结构

```
character-skill/
├── README.md                    # 项目说明
├── SKILL.md                     # OpenClaw Skill入口
├── requirements.txt             # 依赖
│
├── docs/                        # 文档
│   ├── FRAMEWORK.md            # 本框架文档
│   ├── PRD.md                  # 产品需求
│   └── API.md                  # API文档
│
├── prompts/                     # Prompt模板
│   ├── intake.md               # 信息采集
│   ├── analysis.md             # 模式分析
│   ├── capability_builder.md   # 能力层构建
│   ├── personality_builder.md  # 人格层构建
│   └── scenario_simulator.md   # 场景模拟
│
├── tools/                       # 核心工具
│   ├── character_manager.py    # Skill管理
│   ├── data_collector.py       # 数据采集
│   ├── pattern_analyzer.py     # 模式分析
│   ├── typology.py             # 类型学系统
│   └── scenario_engine.py      # 场景引擎
│
├── characters/                  # 生成的人物Skills
│   └── [character-slug]/
│       ├── config.json
│       ├── capability.md
│       ├── personality.md
│       └── data/
│
└── templates/                   # 场景模板
    ├── review_template.md
    ├── communication_template.md
    └── conflict_template.md
```

### 3.2 核心类图

```python
class CharacterProfile:
    """人物画像"""
    name: str
    dimensions: CharacterDimensions
    capability: CapabilityLayer
    personality: PersonalityLayer
    
class CapabilityLayer:
    """能力层"""
    knowledge: Dict          # 知识技能
    thinking_patterns: List  # 思维方式
    decision_rules: List     # 决策规则
    
class PersonalityLayer:
    """人格层"""
    behavior_style: Enum     # 行为风格
    emotion_patterns: Dict   # 情绪模式
    communication_prefs: Dict # 沟通偏好
    
class ScenarioEngine:
    """场景引擎"""
    def simulate(scenario_type, input) -> SimulationResult
    
class TypologySystem:
    """类型学系统"""
    def classify(profile) -> TypeReport
    def get_strategy(type) -> StrategyGuide
```

---

## 四、应用示例

### 4.1 女友Skill示例

```python
# 创建女友Skill
/create-girlfriend --name "小美"

# 维度标签
- 行为风格: 感性型、需要关注
- 决策模式: 直觉型、情绪化
- 沟通方式: 暗示型、需要猜测
- 情绪特征: 波动大、需要安抚
- 价值观念: 重视陪伴、仪式感

# 使用场景
/girlfriend-mood      # 分析当前情绪状态
/girlfriend-gift      # 礼物推荐
/girlfriend-conflict  # 冲突后和解策略
/girlfriend-talk      # 重要话题沟通模拟
```

### 4.2 小孩Skill示例

```python
# 创建小孩Skill
/create-child --name "小宝" --age 5

# 维度标签
- 发展阶段: 学龄前、自我意识觉醒
- 行为特征: 好奇心强、注意力短
- 沟通方式: 具体形象思维、需要游戏化
- 情绪特点: 情绪调节能力弱、需要引导
- 学习风格: 视觉型、动手型

# 使用场景
/child-education      # 教育方法建议
/child-emotion        # 情绪引导策略
/child-activity       # 适合的活动推荐
```

---

## 五、伦理与边界

### 5.1 隐私保护

- **知情同意** - 必须告知并获得授权
- **数据脱敏** - 敏感信息匿名化处理
- **访问控制** - 限制Skill的访问范围
- **删除权** - 支持随时删除个人数据

### 5.2 使用边界

- **理解而非操控** - 目的是改善关系，不是控制对方
- **尊重自主性** - 不用于预测敏感信息（如密码、隐私）
- **避免标签化** - 人是动态变化的，标签只是参考
- **保持真实互动** - Skill是辅助，不能替代真实沟通

### 5.3 免责声明

> 本框架生成的人物Skill基于历史数据模式，不代表对该人物的完整理解。人是复杂且动态变化的，Skill输出仅供参考，不能替代真实的沟通和理解。

---

## 六、从 boss-skill 迁移

如果你已经实现了 boss-skill，要迁移到其他人物类型：

### 6.1 修改清单

| 修改项 | boss-skill | girlfriend-skill | child-skill |
|--------|-----------|------------------|-------------|
| **维度设计** | 8维职场标签 | 8维亲密关系标签 | 8维发展阶段标签 |
| **数据源** | 工作消息、会议 | 聊天记录、社交动态 | 观察记录、成长日记 |
| **场景** | 汇报、争取资源 | 沟通、礼物、冲突 | 教育、陪伴、引导 |
| **Prompt** | 职场沟通风格 | 情感表达方式 | 儿童心理发展 |

### 6.2 复用组件

可以直接复用的组件：
- ✅ 数据采集工具 `data_collector.py`
- ✅ 模式分析引擎 `pattern_analyzer.py`
- ✅ 类型学框架 `typology.py`
- ✅ 版本管理系统 `version_manager.py`
- ✅ 场景引擎框架 `scenario_engine.py`

需要定制的组件：
- 📝 Prompt模板（适应新场景）
- 📝 维度标签定义
- 📝 场景具体实现

---

## 七、总结

### 7.1 核心收益

1. **深度理解** - 系统性地理解重要人物
2. **预测能力** - 提前预判反应，减少冲突
3. **沟通优化** - 选择最佳时机和方式
4. **关系改善** - 基于理解的相处，而非猜测

### 7.2 关键成功因素

1. **数据质量** - 真实、多样、充足的数据
2. **维度完整** - 8维标签全面刻画
3. **持续迭代** - 基于反馈不断优化
4. **伦理边界** - 尊重隐私，理解而非操控

### 7.3 下一步行动

1. 选择一个人物类型作为试点
2. 设计该类型的8维标签体系
3. 收集真实数据（至少100条交互）
4. 按照7步法逐步实现
5. 测试验证，迭代优化

---

**参考实现**: [boss-skill](https://github.com/aituli/boss-skill)

**框架版本**: v1.0
**最后更新**: 2026-04-09
