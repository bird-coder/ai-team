# ai-team 使用指南

这里只说明如何操作；配置、角色职责和流程规则见 [README.md](README.md)。

## 1. 准备并启动

准备需求原件路径和项目规则入口。项目已有 AGENTS.md 时可以直接使用；
否则按 [README 的项目规则说明](README.md#不创建项目-agentsmd按游戏指定规则入口) 准备 project-rules.md。
在规则中选择开发角色：`development_roles: [backend]`、`[client]` 或 `[backend, client]`。

终端执行：

```bash
bash /实际路径/ai-team/scripts/start /实际路径/目标项目
```

下面的指令在启动后的会话中发送，不是终端命令。
替换所有 `<占位内容>`；路径相对目标项目根目录。
没有独立规则文件时，删除 `project_rules_file` 行；任务 ID 可自定或让 agent 分配。
产物路径以 agent 实际返回的为准。

## 2. 启动需求审核

```text
workflow: requirements-review
project_rules_file: <项目规则文件路径>
task_id: <需求审核任务ID>

请按 ai-team 需求审核流程审核：
- <需求原件路径，可多份>

先完成可独立开展的分析，将问题集中输出到 review.md 供我回复。
本次只做需求审核，不进入设计或代码开发。
```

打开 agent 返回的 review.md，阅读其引用的分析文档，按问题编号填写人工回复；
也可交给策划填写，或在聊天中按编号回复。

默认人工入口：`docs/tasks/<需求审核任务ID>/requirements/round-<n>/review.md`。

### 回复后继续审核

```text
继续需求审核任务 <需求审核任务ID>。
我已在 <本轮review.md路径> 回复问题，请读取并复核，更新受影响产物。
新问题继续集中输出供我 review；本次仅回复问题，尚未批准整个需求基线。
```

### 确认需求并结束审核

问题处理完成，阅读最终产物后发送：

```text
我确认 <本轮review.md/gate.md路径> 所列的需求基线 <版本标识>，
包括原件、已确认决定、业务拆分、验收条件及列明的非阻塞风险。
请核验审核条件，满足后保存正式 gate.md 和 handoff.md，结束需求审核。
不要自动启动开发。
```

保存返回的 gate.md 和 handoff.md 路径，下一步使用。

## 3. 启动开发文档阶段

在原会话或按第 1 步启动的新会话中发送：

```text
workflow: development
project_rules_file: <项目规则文件路径>
task_id: <开发任务ID>

请按 ai-team 开发流程，依据以下已批准产物开始文档阶段：
- <需求审核gate.md路径>
- <需求审核handoff.md路径>

先核对原始需求与审核产物，再输出架构、接口、开发任务及测试方案。
集中输出 design/review.md 供我 review；批准文档包前不要写代码。
```

打开返回的 design/review.md，查看其引用的需求理解、架构、接口、开发计划和测试方案，
填写问题回复及修改意见。

默认人工入口：`docs/tasks/<开发任务ID>/design/review.md`。

### 提交修改意见

```text
继续开发任务 <开发任务ID> 的文档阶段。
请读取 <design/review.md路径> 中的人工回复，修改并复核受影响文档。
更新后再次交付 review，暂不批准代码实现。
```

### 批准文档并继续实现

阅读修改后的完整文档包后发送；不要仅以“问题已回复”代替批准：

```text
我批准 <design/review.md路径> 所列的完整开发文档包 <版本标识>，
包括需求理解、架构、接口、开发任务及测试方案。
请核验批准版本与当前文件一致且准入检查通过，然后继续实现、单元测试、
独立代码审核及 QA。新增的需人工决定事项集中提交 review，不擅自改规则。
不要自动合并或部署。
```

这是继续同一个开发流程，无需启动第三个入口。

## 4. 需求原件更新时

```text
需求原件已更新：<新原件路径>。
此前审核记录：<gate.md/handoff.md路径>。
当前任务状态：<status.md路径>。

请对照旧原件和已确认回复复核变化，保留编号及历史，集中输出 review.md。
暂停受影响的开发；本次不批准新基线，也不自动恢复受影响开发。
```

复核完成后，按第 2 步确认更新的需求，再明确要求恢复开发；
如果开发文档包随之修改，按第 3 步 review 并批准新版本。

## 5. 新会话恢复任务

按第 1 步选择同一项目启动，发送：

```text
workflow: <requirements-review 或 development，填写当前任务的入口>
project_rules_file: <原任务使用的规则文件路径>

请恢复任务 <任务ID>，先读取 <status.md路径> 及引用的 review、gate 和产物。
沿用有效成果，从记录的阶段继续。
若尚待人工 review，返回需回复或批准的文档，不假定已有批准。
```

填写文档后需主动发送“请读取回复并继续”，保存文件不会自动恢复流程。

## 6. 查看交付

根据最终回复中的链接，查看代码变更、测试证据、代码审核、QA 和剩余问题。

默认在 `docs/tasks/<开发任务ID>/` 下查看：
`review.md`（代码审核）、`unit-tests.md`、`qa.md` 和 `status.md`。
这里的 review.md 不是前面的 design/review.md。

验收标准见 [README 的单元测试验收](README.md#单元测试验收)。
