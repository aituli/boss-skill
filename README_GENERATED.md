# Boss Skill

> 把老板的管理风格、决策模式、说话艺术蒸馏成 AI Skill，让你随时获得「老板视角」的指导和反馈。

## 项目简介

Boss Skill 是一个专门模拟管理者思维方式的 AI Skill 系统。通过分析老板的管理风格、决策习惯和沟通模式，帮助下属预判老板反应、优化汇报策略、选择最佳沟通时机。

核心用户群包括：希望更好理解上级的职场人、想学习优秀管理经验的管理者、需要模拟投资人或合伙人视角的创业者。

## 核心功能

### 双轨架构
- **管理 Skill（Part A）**：战略思维框架、管理方法论、业务知识体系、沟通套路库
- **领导 Persona（Part B）**：权威表现层、决策风格层、情绪模式层、人际策略层

### 场景模拟器
| 场景 | 功能 |
|------|------|
| 方案汇报预审 | 预判老板会怎么问、关注什么 |
| 1on1 沟通模拟 | 模拟加薪、晋升、困难沟通 |
| 突发情况应对 | 出事了怎么汇报、怎么补救 |
| 演讲稿生成 | 生成老板风格的演讲稿 |

### 老板类型标签系统
8维分类体系：管理风格、沟通风格、决策风格、反馈风格、激励方式、压力表现、技术程度、工作节奏

常见组合类型：
- 细节控 + 数据控：准备超级详细的报告，每个数字都要有来源
- 教练型 + 闪电决策：抓住机会快速试错，事后认真复盘
- 独裁型 + 火山型：绝对服从，永远不要当众质疑

## 使用场景

**下属视角**：
- 准备汇报：提前知道老板会问什么
- 挨骂预警：项目出问题前模拟老板反应
- 争取资源：预判老板怎么拒绝，提前准备 ROI 论证
- 理解潜台词：老板说"再想想"到底是什么意思

**管理者视角**：
- 学习优秀老板的管理艺术
- 通过 AI 视角审视自己的管理风格
- 理解团队成员如何看待自己

**创业者视角**：
- 用投资人视角审视商业计划书
- 预判合伙人会怎么质疑

## 详细使用说明

### Claude Code 使用方式

安装：
```bash
git clone https://github.com/yourusername/boss-skill.git
cd boss-skill
pip install -r requirements.txt
```

创建老板 Skill：
```
/create-boss
```

使用场景模拟：
```
/{boss-slug}-review 方案内容    # 方案预审
/{boss-slug}-1on1 话题          # 1on1 模拟
/{boss-slug}-emergency 事件     # 突发情况
/{boss-slug}-speech 场合 主题   # 演讲稿生成
```

### OpenClaw 使用方式

安装：
```bash
git clone https://github.com/yourusername/boss-skill \
  ~/.openclaw/workspace/skills/boss-skill
```

Python 工具使用：
```bash
# 创建老板 Skill
python tools/boss_manager.py create \
  --name "张总" \
  --style micromanager \
  --decision data-driven

# 方案预审
python tools/scenario_engine.py review zhang \
  --content "投入100万预计带来50万新用户"

# 1on1 模拟
python tools/scenario_engine.py 1on1 zhang \
  --topic "想申请加薪20%"

# 突发情况
python tools/scenario_engine.py emergency zhang \
  --event "线上P0级bug影响10万用户"
```

### 使用示例

**方案汇报预审**：
```
$ python tools/scenario_engine.py review zhang \
    --content "计划投入100万做Q3用户增长"

═══ 可能的质疑 ═══
1. 「数据呢？50万新用户的测算依据是什么？」
2. 「为什么是100万？有没有其他预算方案对比？」
3. 「最坏的情况是什么？如果ROI只有100%怎么办？」

═══ 建议准备 ═══
✓ 历史投放数据作为 benchmark
✓ 至少3个预算方案对比
✓ 风险评估和 Plan B
```

**1on1 加薪谈判**：
```
$ python tools/scenario_engine.py 1on1 zhang \
    --topic "想申请加薪20%，过去一年业绩超额完成30%"

═══ 老板可能的反应 ═══
【第一反应】（翻看数据）「30%是不错，但...」
【潜台词】认可成绩，但想压价

═══ 建议话术 ═══
开场：「张总，想跟您聊聊职业发展...」
论据：业绩数据、行业薪资对比、未来目标
收尾：「希望能得到公司认可，我的期望是...」

═══ 最佳时机 ═══
✓ 刚完成大项目/季度业绩发布
✓ 周一上午（老板心情较好）
✗ 避免：月底、周五下午
```

**突发情况应对**：
```
$ python tools/scenario_engine.py emergency zhang \
    --event "线上P0级bug影响10万用户"

═══ 🔥 怒火等级预测 ═══
████████░░ 80% (很高)

═══ 💬 老板会怎么发火 ═══
「P0级bug为什么会发生？测试流程是摆设吗？」

═══ 🛡️ 补救话术 ═══
1. 承认错误：「张总，出了P0级bug，我的责任」
2. 当前状态：「已修复，2小时内全量恢复」
3. 影响评估：「影响10万用户，预计损失XXX」
4. 补救措施：「已准备用户补偿方案」
5. 预防措施：「复盘已完成，优化测试流程」
```

## 文件结构说明

```
boss-skill/
├── SKILL.md                    # OpenClaw Skill 入口
├── README.md                   # 项目说明
├── requirements.txt            # Python 依赖
├── prompts/                    # Prompt 模板
│   ├── intake.md              # 信息采集
│   ├── mgmt_analyzer.md       # 管理能力分析
│   ├── persona_analyzer.md    # 人格分析
│   ├── mgmt_builder.md        # 管理 Skill 生成
│   ├── persona_builder.md     # 人格生成
│   ├── scenario_simulator.md  # 场景模拟
│   └── upward_coach.md        # 向上管理教练
├── tools/                      # Python 工具
│   ├── boss_manager.py        # Skill 管理
│   ├── scenario_engine.py     # 场景模拟引擎
│   └── pattern_analyzer.py    # 行为模式分析
├── bosses/                     # 生成的老板 Skills
├── templates/                  # 场景模板
│   ├── review_template.md
│   ├── oneonone_template.md
│   ├── emergency_template.md
│   └── speech_template.md
└── docs/
    ├── PRD.md
    └── API.md
```

## 注意事项

**隐私与伦理**：
- 仅使用公开群聊、会议纪要等非敏感数据
- 个人私聊数据需获得明确授权
- 企业版需符合数据合规要求
- 所有数据本地存储，不上传云端

**使用原则**：
- 用于「理解」而非「操控」
- 明确告知这是模拟，不能替代真实沟通
- 禁止用于不当目的（如欺骗、打小报告）

**局限性**：
- 模拟基于已有数据，无法预测突发情绪
- 仅供参考，重大决策仍需真实沟通
- 不能替代正式的管理培训和咨询
