# boss-skill

把老板的管理风格、决策模式、说话艺术蒸馏成AI Skill，让你随时获得「老板视角」的指导和反馈。

---

## 快速开始

```bash
# 创建一个新的老板Skill
/create-boss

# 列出所有已创建的老板Skill
/list-bosses

# 使用特定老板Skill进行方案预审
/{boss-slug}-review 方案文件

# 1on1沟通模拟
/{boss-slug}-1on1 话题

# 突发情况应对模拟
/{boss-slug}-emergency 事件描述

# 生成演讲稿
/{boss-slug}-speech 场合 主题
```

---

## 核心功能

### 1. 双轨架构

**Part A: 管理Skill** - 老板的管理智慧
- 战略思维框架（业务优先级、资源分配、风险评估）
- 管理方法论（1on1模式、绩效评价、激励机制）
- 业务知识体系（行业认知、竞争格局、商业模式）
- 沟通套路库（经典话术、拒绝技巧、画饼公式）

**Part B: 领导Persona** - 老板的人格特征
- 权威表现层（说话方式、称呼习惯）
- 决策风格层（民主型/专制型、数据驱动/直觉驱动）
- 情绪模式层（压力反应、好消息/坏消息表达方式）
- 人际策略层（对不同下属的区别对待、向上管理风格）

### 2. 场景模拟器

| 场景 | 命令 | 说明 |
|------|------|------|
| 方案汇报预审 | `/{slug}-review` | 预判老板会怎么问、关注什么 |
| 1on1沟通模拟 | `/{slug}-1on1` | 模拟加薪、晋升、困难沟通 |
| 突发情况应对 | `/{slug}-emergency` | 出事了怎么汇报、怎么补救 |
| 演讲稿生成 | `/{slug}-speech` | 生成老板风格的演讲稿 |

### 3. 老板思维分析器

- **优先级雷达**：分析老板最近反复提到的关键词
- **决策模式分析**：判断老板的决策风格
- **情绪周期图**：分析老板情绪波动规律
- **关注点热力图**：老板在各类事务上的关注程度
- **经典话术库**：收集老板的口头禅和潜台词

---

## 使用场景

### 下属视角
- **准备汇报**：提前知道老板会问什么，准备充分
- **挨骂预警**：项目出问题，先模拟老板反应，想好对策
- **争取资源**：申请预算/人力，预判老板怎么拒绝，提前准备ROI论证
- **理解潜台词**：老板说"再想想"到底是什么意思

### 管理者视角
- **学习优秀老板**：把优秀管理者的艺术提炼出来学习
- **自我反思**：通过AI视角审视自己的管理风格
- **团队沟通**：理解团队成员如何理解你

### 创业者视角
- **模拟投资人**：用投资人视角审视自己的BP
- **模拟合伙人**：预判合伙人会怎么质疑

---

## 命令详解

### /create-boss

创建一个新的老板Skill。系统会引导你完成信息采集：

1. **基础信息**：姓名、职位、管理风格标签
2. **数据采集**：飞书/钉钉消息、会议纪要、邮件等
3. **人格分析**：回答一些关于老板行为模式的问题
4. **生成Skill**：自动生成管理Skill + Persona

### /{boss-slug}-review <方案文件/内容>

方案汇报预审。输入你的方案，获得：
- 老板可能提出的10个问题
- 需要准备的核心数据
- 应该强调的关键点
- 可能遇到的质疑及应对建议

**示例**：
```
/{boss-slug}-review 我要汇报Q3增长方案，计划投入100万做用户增长，预计带来50万新用户
```

### /{boss-slug}-1on1 <话题>

1on1沟通模拟。输入你想谈的话题，获得：
- 老板可能的反应（接受/拒绝/拖延）
- 建议的沟通话术
- 最佳沟通时机
- 需要准备的论据

**示例**：
```
/{boss-slug}-1on1 想申请加薪20%，理由是过去一年业绩超额完成30%
```

### /{boss-slug}-emergency <事件描述>

突发情况应对。输入出的事情，获得：
- 老板会怎么发火（预测怒火等级）
- 如何降低损失
- 补救话术（怎么道歉、怎么补救）
- 预防下次发生的建议

**示例**：
```
/{boss-slug}-emergency 线上出了P0级bug，影响10万用户，已经修复但需要2小时才能全量恢复
```

### /{boss-slug}-speech <场合> <主题>

生成老板风格的演讲稿。

**示例**：
```
/{boss-slug}-speech 年会 Q4动员
```

### /list-bosses

列出所有已创建的老板Skill，显示版本、创建时间、使用次数。

### /{boss-slug}-analyze

分析老板思维模式，输出：
- 管理风格画像
- 决策模式分析
- 情绪周期规律
- 经典话术Top10

---

## 老板类型标签

创建时可以标记老板的类型：

| 维度 | 选项 |
|------|------|
| 管理风格 | Micromanager / Hands-off / Coach / Dictator / Laissez-faire |
| 沟通风格 | Direct / Indirect / Storyteller / Data-driven / Emotional |
| 决策风格 | Fast / Cautious / Consensus / Gut-feeling / Analytical |
| 反馈风格 | Blunt / Sandwich / Passive / Public / Private |
| 激励方式 | Vision / Money / Recognition / Growth / Fear |
| 压力表现 | Angry / Silent / Worried / Supportive / Absent |
| 技术程度 | Tech-savvy / Tech-curious / Tech-agnostic / Tech-averse |
| 工作节奏 | Morning-person / Night-owl / Always-on / Boundary |

---

## 隐私与伦理

**隐私保护**：
- 仅使用公开群聊、会议纪要等非敏感数据
- 个人私聊数据需获得明确授权
- 企业版需符合数据合规要求

**使用原则**：
- 用于「理解」而非「操控」
- 明确告知这是模拟，不能替代真实沟通
- 禁止用于不当目的（如欺骗、打小报告）

---

## 技术架构

```
boss-skill/
├── SKILL.md              # Skill入口
├── prompts/              # Prompt模板
│   ├── intake.md         # 信息采集对话
│   ├── mgmt_builder.md   # 管理Skill生成
│   ├── persona_builder.md # 人格Persona生成
│   └── scenario_simulator.md # 场景模拟
├── tools/                # Python工具
│   ├── boss_manager.py   # Skill管理
│   ├── scenario_engine.py # 场景模拟引擎
│   └── pattern_analyzer.py # 行为模式分析
├── bosses/               # 生成的老板Skills（gitignored）
└── templates/            # 场景模板
```

---

## 与 colleague-skill 的关系

| 维度 | colleague-skill | boss-skill |
|------|-----------------|------------|
| 核心目标 | 继承工作能力 | 学习管理思维 |
| 交互方式 | 被动响应任务 | 主动提出问题 |
| 语言风格 | 技术规范 | 权威感、启发式 |
| 关注点 | 执行细节 | 战略方向、资源、风险 |
| 使用场景 | 替代离职同事 | 模拟汇报、预判反应 |

---

## 开发路线图

- [x] MVP：基础场景模拟（review, 1on1, emergency）
- [ ] Phase 2：数据采集、行为模式分析
- [ ] Phase 3：情绪周期预测、决策风格分析
- [ ] Phase 4：Web界面、企业版、API

---

*Version: 1.0.0*
*License: MIT*
