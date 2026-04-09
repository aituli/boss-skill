# 🎩 Boss Skill

> 把老板的管理风格、决策模式、说话艺术蒸馏成AI Skill，让你随时获得「老板视角」的指导和反馈。

---

## ✨ 核心价值

### 对下属
- **预判老板反应**：提前知道老板会怎么问、怎么骂
- **优化汇报策略**：老板会喜欢/讨厌什么，如何改进
- **选对沟通时机**：了解老板的情绪周期

### 对管理者
- **学习优秀老板**：把优秀管理者的艺术提炼出来
- **自我反思**：通过AI视角审视自己的管理风格

### 对创业者
- **模拟投资人**：用投资人视角审视自己的BP
- **模拟合伙人**：预判合伙人会怎么质疑

---

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/yourusername/boss-skill.git
cd boss-skill
pip install -r requirements.txt
```

### 创建你的第一个老板Skill

```bash
# 启动创建向导
python tools/boss_manager.py create

# 或者直接指定参数
python tools/boss_manager.py create \
  --name "张总" \
  --style micromanager \
  --decision data-driven
```

### 使用场景模拟器

```bash
# 方案预审
python tools/scenario_engine.py review zhang \
  --content "我要汇报Q3增长方案，投入100万预计带来50万新用户"

# 1on1模拟
python tools/scenario_engine.py 1on1 zhang \
  --topic "想申请加薪20%"

# 突发情况应对
python tools/scenario_engine.py emergency zhang \
  --event "线上P0级bug影响10万用户"
```

---

## 📋 功能列表

### 场景模拟器 ✅

| 场景 | 命令 | 状态 |
|------|------|------|
| 方案汇报预审 | `review` | ✅ |
| 1on1沟通模拟 | `1on1` | ✅ |
| 突发情况应对 | `emergency` | ✅ |
| 演讲稿生成 | `speech` | ✅ |

### 老板思维分析器 🚧

- [ ] 优先级雷达
- [ ] 决策模式分析
- [ ] 情绪周期图
- [ ] 关注点热力图
- [ ] 经典话术库

### 数据采集 📊

- [ ] 飞书消息采集
- [ ] 钉钉消息采集
- [ ] 会议纪要解析
- [ ] 邮件解析

---

## 🏗️ 项目结构

```
boss-skill/
├── SKILL.md                    # OpenClaw Skill入口
├── README.md                   # 项目说明（本文件）
├── requirements.txt            # Python依赖
├── prompts/                    # Prompt模板
│   ├── intake.md              # 信息采集对话
│   ├── mgmt_analyzer.md       # 管理能力分析
│   ├── persona_analyzer.md    # 人格分析
│   ├── mgmt_builder.md        # 管理Skill生成
│   ├── persona_builder.md     # 人格Persona生成
│   ├── scenario_simulator.md  # 场景模拟器
│   └── upward_coach.md        # 向上管理教练
├── tools/                      # Python工具
│   ├── boss_manager.py        # Skill创建与管理
│   ├── scenario_engine.py     # 场景模拟引擎
│   ├── pattern_analyzer.py    # 行为模式分析
│   └── __init__.py
├── bosses/                     # 生成的老板Skills
│   └── .gitkeep
├── templates/                  # 场景模板
│   ├── review_template.md
│   ├── oneonone_template.md
│   ├── emergency_template.md
│   └── speech_template.md
├── scripts/                    # 辅助脚本
│   └── setup.sh
└── docs/                       # 文档
    ├── PRD.md
    └── API.md
```

---

## 🎭 双轨架构

Boss Skill 采用双轨架构，分离「管理智慧」和「人格特征」：

```
┌─────────────────────────────────────────────────────────────┐
│                    融合输出层                               │
│     接收场景 → Persona决定态度 → 管理Skill提供内容 →        │
│     以老板的口吻输出建议                                      │
└─────────────────────────────────────────────────────────────┘
                              ↑
        ┌─────────────────────┴─────────────────────┐
        ↓                                           ↓
┌───────────────────┐                   ┌───────────────────┐
│   Part A: 管理Skill │                   │  Part B: 领导Persona│
├───────────────────┤                   ├───────────────────┤
│ • 战略思维框架     │                   │ • 权威表现层       │
│ • 管理方法论       │                   │ • 决策风格层       │
│ • 业务知识体系     │                   │ • 情绪模式层       │
│ • 沟通套路库       │                   │ • 人际策略层       │
└───────────────────┘                   └───────────────────┘
```

---

## 🏷️ 老板类型标签

创建老板Skill时可以标记以下维度：

| 维度 | 选项 |
|------|------|
| **管理风格** | Micromanager / Hands-off / Coach / Dictator / Laissez-faire |
| **沟通风格** | Direct / Indirect / Storyteller / Data-driven / Emotional |
| **决策风格** | Fast / Cautious / Consensus / Gut-feeling / Analytical |
| **反馈风格** | Blunt / Sandwich / Passive / Public / Private |
| **激励方式** | Vision / Money / Recognition / Growth / Fear |
| **压力表现** | Angry / Silent / Worried / Supportive / Absent |
| **技术程度** | Tech-savvy / Tech-curious / Tech-agnostic / Tech-averse |
| **工作节奏** | Morning-person / Night-owl / Always-on / Boundary |

---

## 💡 使用示例

### 示例1：方案汇报预审

```bash
$ python tools/scenario_engine.py review zhang \
    --content "计划投入100万做Q3用户增长，预计带来50万新用户，ROI 150%"

🎩 【张总视角的方案预审】

═══ 可能的质疑 ═══
1. 「数据呢？这50万新用户的测算依据是什么？」
2. 「为什么是100万？有没有做过50万和150万的方案对比？」
3. 「最坏的情况是什么？如果ROI只有100%怎么办？」
4. 「这100万具体怎么分配？每个渠道的预期回报是多少？」

═══ 需要准备 ═══
✓ 历史投放数据作为benchmark
✓ 至少3个预算方案对比
✓ 风险评估和Plan B
✓ 分渠道ROI测算

═══ 建议强调 ═══
• 强调数据驱动，每个数字都有依据
• 主动提及风险，展示风控意识
• 准备详细的执行时间表

═══ 可能踩雷 ═══
✗ 不要说"大概"、"可能"、"估计"
✗ 不要只谈好的情况
✗ 不要没有对比方案
```

### 示例2：1on1加薪谈判

```bash
$ python tools/scenario_engine.py 1on1 zhang \
    --topic "想申请加薪20%，过去一年业绩超额完成30%"

🎩 【张总的1on1模拟】

═══ 老板可能的反应 ═══
【第一反应】（翻看业绩数据）「30%是不错，但...」
【潜台词】认可成绩，但想压价

═══ 建议话术 ═══
开场：「张总，想跟您聊聊我的职业发展。过去一年...」
论据：
  • 业绩数据（超额30%的具体数字）
  • 对比：行业同等岗位的薪资水平
  • 未来：接下来半年的目标和承诺
收尾：「希望能得到公司的认可，我的期望是...」

═══ 最佳时机 ═══
✓ 刚完成一个大项目/季度业绩发布
✓ 周一上午（老板心情较好）
✗ 避免：月底、周五下午、老板刚开完会

═══ 老板可能的拒绝话术 ═══
• 「等年底调薪再说」→ 这是拖延，要求明确时间
• 「公司现在有预算压力」→ 问是否可以用其他形式补偿
• 「20%太高了」→ 准备好15%和10%的底线
```

### 示例3：突发情况应对

```bash
$ python tools/scenario_engine.py emergency zhang \
    --event "线上P0级bug影响10万用户，已修复但需要2小时全量恢复"

🎩 【张总的突发情况应对】

═══ 🔥 怒火等级预测 ═══
████████░░ 80% (很高)

原因：
• P0级bug是红线
• 10万用户受影响
• 恢复时间2小时太长

═══ 💬 老板会怎么发火 ═══
「我再说一遍，P0级bug为什么会发生？
测试流程是摆设吗？
这2个小时你知道公司损失多少吗？」

═══ 🛡️ 补救话术 ═══
汇报框架：
1. 承认错误：「张总，出了P0级bug，我的责任」
2. 当前状态：「已修复，2小时内全量恢复」
3. 影响评估：「影响10万用户，预计损失XXX」
4. 补救措施：「已准备用户补偿方案...」
5. 预防措施：「复盘已完成，优化测试流程...」

═══ 📉 如何降低损失 ═══
• 主动准备用户补偿方案
• 准备详细的复盘报告
• 提出具体的改进措施
• 承担责任，不推诿
```

---

## ⚙️ 配置说明

### 环境变量

```bash
# OpenAI API（用于生成内容）
export OPENAI_API_KEY="your-api-key"

# 可选：使用其他模型
export BOSS_SKILL_MODEL="gpt-4"
```

### 配置文件

`~/.boss-skill/config.json`:

```json
{
  "default_model": "gpt-4",
  "data_collection": {
    "enable_feishu": false,
    "enable_dingtalk": false
  },
  "privacy": {
    "only_public_channels": true,
    "retention_days": 90
  }
}
```

---

## 🔒 隐私与伦理

### 隐私保护
- ✅ 仅使用公开群聊、会议纪要等非敏感数据
- ✅ 个人私聊数据需获得明确授权
- ✅ 企业版需符合数据合规要求
- ✅ 所有数据本地存储，不上传云端

### 使用原则
- ✅ 用于「理解」而非「操控」
- ✅ 明确告知这是模拟，不能替代真实沟通
- ❌ 禁止用于不当目的（如欺骗、打小报告）

---

## 🤝 与 colleague-skill 的关系

本项目受 [colleague-skill](https://github.com/titanwings/colleague-skill) 启发，但专注于不同的场景：

| 维度 | colleague-skill | boss-skill |
|------|-----------------|------------|
| 核心目标 | 继承工作能力 | 学习管理思维 |
| 交互方式 | 被动响应任务 | 主动提出问题 |
| 语言风格 | 技术规范、平等 | 权威感、启发式 |
| 关注点 | 执行细节 | 战略方向、资源、风险 |
| 使用对象 | 接替者/团队 | 下属/学习者 |

---

## 📅 路线图

### ✅ MVP (已完成)
- [x] 基础场景模拟（review, 1on1, emergency, speech）
- [x] 命令行工具
- [x] Prompt模板系统

### 🚧 Phase 2 (进行中)
- [ ] 数据采集（飞书/钉钉）
- [ ] 行为模式分析
- [ ] 老板思维分析器

### 📋 Phase 3 (规划中)
- [ ] 情绪周期预测
- [ ] 决策风格分析
- [ ] 时机选择建议

---

## 🎭 老板类型学 (Boss Typology)

我们基于 **8维标签系统**，定义了25+种常见老板类型，帮助你快速识别和应对。

### 8维分类体系

| 维度 | 类型数量 | 说明 |
|------|----------|------|
| **管理风格** | 5种 | Micromanager细节控、Hands-off放手型、Coach教练型、Dictator独裁型、Laissez-faire放任型 |
| **决策风格** | 5种 | Data-driven数据控、Gut-feeling直觉型、Fast闪电型、Cautious谨慎型、Consensus民主型 |
| **沟通风格** | 4种 | Direct直球型、Indirect含蓄型、Storyteller故事型、Emotional感性型 |
| **反馈风格** | 4种 | Blunt炸弹型、Sandwich三明治型、Passive暗示型、Public公开处刑型 |
| **压力表现** | 4种 | Angry火山型、Silent冷暴力型、Worried焦虑传染型、Supportive战士型 |
| **技术程度** | 4种 | Savvy技术大拿、Curious学习型、Agnostic无所谓型、Averse抗拒型 |

### 常见混合类型

| 组合 | 名称 | 难度 | 应对策略 |
|------|------|------|----------|
| 🔍+📊 | 细节控+数据控 | ⭐⭐⭐⭐⭐ | 准备超级详细的报告，每个数字都要有来源 |
| 🏃+⚡ | 教练型+闪电决策 | ⭐⭐ | 抓住机会快速试错，事后认真复盘 |
| 👑+😤 | 独裁型+火山型 | ⭐⭐⭐⭐⭐ | 绝对服从，永远不要当众质疑 |
| 🙌+🐢 | 放手型+谨慎型 | ⭐⭐⭐ | 提前很久铺垫，用时间换空间 |

### 使用老板类型学工具

```bash
# 查看所有类型定义
python3 tools/boss_typology.py --list

# 查看示例老板画像和分类报告
python3 tools/boss_typology.py --example

# 对特定老板进行分类（需要提供JSON文件）
python3 tools/boss_typology.py --classify bosses/my-boss.json
```

### 快速识别测试

**5分钟快速测试你的老板类型：**

1. **他开周会，第一句话通常是？**
   - "数据怎么样？" → 📊 数据控
   - "我简单说两句..." → 📚 故事型  
   - "上周那件事谁负责？" → 🔍 细节控
   - "大家有什么想法？" → 👥 民主型

2. **你发消息问"这个方案可以吗？"**
   - 秒回"可以" → ⚡ 闪电型
   - 2小时后才回"再想想" → 🐢 谨慎型
   - 不回 → 😶 暗示型
   - 回5条语音分析问题 → 🔍 细节控

3. **项目出问题了，他的第一反应是？**
   - "谁的责任？" → 😤 火山型
   - "怎么解决？" → 🦸 战士型
   - 不说话看着你 → 🧊 冷暴力型
   - 开始焦虑问怎么办 → 😰 焦虑传染型

---

### 🔮 Phase 4 (未来)
- [ ] Web界面
- [ ] 企业版功能
- [ ] API开放平台

---

## 🤝 贡献

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

### 开发环境

```bash
# 安装开发依赖
pip install -r requirements-dev.txt

# 运行测试
pytest tests/

# 代码格式化
black tools/
isort tools/
```

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- 受 [colleague-skill](https://github.com/titanwings/colleague-skill) 启发
- 感谢所有早期测试用户的反馈

---

*Made with ❤️ for every confused employee*