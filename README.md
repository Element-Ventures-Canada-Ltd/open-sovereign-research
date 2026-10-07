Handling: Unclassified — public

# Open Sovereign Research (working name)

Open research on where a middle power can hold supply-chain and decision capability, and where it should partner or buy. Read the grid, argue a cell, and cite your sources.

## Start here: one cell, read

```yaml
- cell: SDL-M7          # Sovereign Decision Layer × Space
  posture: BUILD
  intensity: core
  rationale: "The registry of who supplies the launch chain is the node a nation must hold by construction."
  evidence_grade: inferred
  sources: ["https://…"]
```

That is a **reading**: one posture, at one intersection of the **Sovereign Seam**, argued and cited.

## The Sovereign Seam

Six layers of the stack — Applications, Sovereign Decision Layer, Models, Infrastructure, Chips, Energy — crossed with the ten sovereign capabilities named in Canada's Defence Industrial Strategy. Sixty cells, each read as **Build**, **Partner** or **Buy**. No cell ever carries a dollar figure.

| Path | What it is |
|---|---|
| [`seam/sovereign-seam.yaml`](seam/sovereign-seam.yaml) | The rubric: layers, capabilities, postures, cell ids |
| [`seam/readings/`](seam/readings/) | Readings, one file per contributor and lens ([template](seam/readings/TEMPLATE.yaml), [worked example](seam/readings/examples/synthetic-reading.yaml)) |
| [`tools/validate_readings.py`](tools/validate_readings.py) | Validator, run in CI on every pull request |
| [`evals/`](evals/) | Public benchmark tasks: a question, its public context, and grading criteria |
| [`docs/method.md`](docs/method.md) | How to read a cell and what counts as evidence |
| [`docs/papers/`](docs/papers/) | Public papers: sovereign launch manufacturing; the space economy value chain |
| [`docs/roadmap.md`](docs/roadmap.md) | Research tracks opening next |

```bash
pip install pyyaml
python3 tools/validate_readings.py
python3 tools/validate_evals.py
```

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). You sign the contributor licence agreement once, through a bot comment on your first pull request.

Sister project: **OpenChokepoint** (working name), an open grammar for recording supply-chain dependencies.

## Licence

Code: Apache-2.0. Documents, rubric and data: Open Government Licence – Canada 2.0. See [LICENSING.md](LICENSING.md).

© 2026 T. Leroy Smith. Exclusively licensed to Element Ventures (Canada) Ltd.
