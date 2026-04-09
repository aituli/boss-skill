# Boss Skill 产品需求文档 (PRD)

## 1. 产品概述

### 1.1 产品定位
Boss Skill 是一个将老板的管理风格、决策模式、说话艺术蒸馏成 AI Skill 的工具，帮助用户获得「老板视角」的指导和反馈。

### 1.2 核心价值主张
- **对下属**：理解老板思维方式，提前预判需求
- **对管理者**：学习优秀老板的管理艺术
- **对创业者**：模拟投资人/合伙人视角

### 1.3 目标用户
- 职场新人：理解老板风格，减少沟通摩擦
- 资深员工：优化向上管理，争取资源
- 管理者：学习优秀案例，提升领导力

## 2. 功能需求

### 2.1 核心功能

#### 2.1.1 老板Skill创建
- 交互式信息采集
- 管理风格标签选择
- 自动生成管理Skill和Persona

#### 2.1.2 场景模拟器
- 方案汇报预审 (review)
- 1on1沟通模拟 (1on1)
- 突发情况应对 (emergency)
- 演讲稿生成 (speech)

#### 2.1.3 行为模式分析
- 口头禅提取
- 质疑模式识别
- 情绪周期分析
- 决策风格推断

### 2.2 功能优先级

| 功能 | 优先级 | 状态 |
|------|--------|------|
| Skill创建 | P0 | ✅ |
| 方案预审 | P0 | ✅ |
| 1on1模拟 | P0 | ✅ |
| 突发应对 | P0 | ✅ |
| 演讲生成 | P1 | ✅ |
| 行为分析 | P1 | ✅ |
| 情绪周期 | P2 | 🚧 |
| 数据采集 | P2 | 🚧 |

## 3. 技术架构

### 3.1 双轨架构
```
输入场景
    ↓
加载管理Skill → 提供内容框架、专业知识
    ↓
加载Persona → 决定态度、语气、情绪
    ↓
融合输出 → 以老板的口吻给出建议
```

### 3.2 数据模型

#### 管理Skill
- 战略思维框架
- 管理方法论
- 业务知识体系
- 沟通套路库

#### 人格Persona
- 权威表现层
- 决策风格层
- 情绪模式层
- 人际策略层

### 3.3 技术栈
- Python 3.8+
- 标准库（json, pathlib, argparse）
- 可选：OpenAI API（高级功能）

## 4. 用户界面

### 4.1 CLI 命令

```bash
# 创建
boss_manager.py create [--name NAME] [--title TITLE] [--no-interactive]

# 管理
boss_manager.py list
boss_manager.py get SLUG
boss_manager.py delete SLUG

# 场景模拟
scenario_engine.py {review|1on1|emergency|speech} BOSS [ARGS]

# 行为分析
pattern_analyzer.py analyze BOSS
pattern_analyzer.py extract BOSS --data FILE
```

### 4.2 交互流程

**创建流程：**
1. 输入老板姓名、职位
2. 选择管理风格标签（8个维度）
3. 输入口头禅、发火信号
4. 确认生成
5. 输出生成文件路径

**使用流程：**
1. 选择场景类型
2. 输入方案/话题/事件
3. 查看模拟结果
4. 根据建议调整策略

## 5. 非功能需求

### 5.1 性能
- 单次模拟响应时间 < 1秒
- 支持同时管理 50+ 个老板Skill

### 5.2 安全
- 所有数据本地存储
- 不上传云端
- 敏感数据加密存储（可选）

### 5.3 可扩展性
- 支持添加新的场景类型
- 支持自定义标签
- 支持导入/导出

## 6. 发布计划

### Phase 1: MVP (v1.0)
- [x] 基础Skill创建
- [x] 4个核心场景模拟
- [x] 基础行为分析

### Phase 2: 增强 (v1.1)
- [ ] 数据采集集成
- [ ] 高级行为分析
- [ ] 情绪周期预测

### Phase 3: 企业版 (v2.0)
- [ ] Web界面
- [ ] 团队协作
- [ ] API接口

## 7. 附录

### 7.1 老板类型标签

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

### 7.2 使用场景示例

**场景1：准备汇报**
用户：我要汇报Q3业绩，帮我预审
输出：老板可能问的问题清单、需要准备的数据、应该强调/回避的点

**场景2：挨骂预警**
用户：项目延期了，怎么汇报
输出：老板会怎么发火、如何降低损失、补救话术

**场景3：争取资源**
用户：想申请2个headcount
输出：老板会怎么拒绝、如何论证ROI、最佳申请时机
