Handling: Unclassified — public

# Evals — public benchmark tasks

Repeatable questions about sovereign capability, each with the public context it may use and the criteria a good answer meets. They let anyone test whether a model, a tool or an analyst reads the Seam well, and they measure progress over time.

| File | Purpose |
|---|---|
| [`TASK_TEMPLATE.yaml`](TASK_TEMPLATE.yaml) | Copy this to write a task |
| [`examples/synthetic-task.yaml`](examples/synthetic-task.yaml) | Worked example |

**Good tasks** have one clear question and criteria that two graders would apply the same way. They cite public sources only and never put a dollar figure on a cell.

Readings in `seam/readings/` and tasks here feed each other. A contested cell makes a good task, and a task most answers fail points to a cell worth reading.

`python3 tools/validate_evals.py` checks every task. CI runs it on each pull request.
