Handling: Unclassified — public

# Ramping sovereign launch manufacturing: the engine is the constraint

*Open Sovereign Research · public paper v1.0 · October 2026 · OGL-Canada-2.0*

## In brief

Canada has committed to sovereign access to space. The pad and the challenge are funded. Whether that produces a launch *industry*, as opposed to a few launches, depends on something slower than either: the ability to build liquid rocket engines at a steady rate, and above all their turbopumps. This paper sets out why the engine sets the pace and where the bottleneck sits. It then poses the questions a ramp plan has to answer, framed so contributors can test them.

## 1. The commitment

- Canada's Defence Industrial Strategy (February 2026) names **space** among ten sovereign capabilities. It adopts Build–Partner–Buy as its determination logic.[1][2]
- In March 2026 the Department of National Defence announced a **$200 million, ten-year lease** for a dedicated launch pad near Canso, Nova Scotia, and **$105 million** for the *Launch the North* challenge.[3]
- *Launch the North* is a staged challenge for Canadian-designed, responsive light-lift launch. It targets an initial operational capability by as late as **2028**.[4]

A pad and a prize create the first vehicles. A cadence of launches needs a cadence of engines.

## 2. Why the engine sets the pace

Launch has become cheap because hardware is reused and produced at volume, not because single vehicles got simpler. NASA analysis put the Space Shuttle's cost to low Earth orbit at about **US$61,700/kg** and Falcon 9's at about **US$2,700/kg**, both in 2018 dollars. That is roughly a twenty-fold reduction.[5] The lesson for a new entrant is that cost follows production rate. Production rate is governed by the hardest part to make.

That part is the turbopump:

- DLR describes rocket turbopumps as **"designed at the technical limit."** Units for orbital launch run at tens of thousands of revolutions per minute. They deliver more than 100 bar in a single pump stage and, for first stages, 7,000 horsepower and more. Their service life is about **one hour**.[6]
- Industry interviews put the thrust-chamber assembly and turbopumps as **the most difficult engine parts to manufacture**. Traditional brazing-based production was cited at **40–50 engines a year** per line.[7]
- Additive manufacturing eases the problem but does not remove it. Current powder-bed machines have build areas well below what medium launch vehicles need, and print throughput is slow for volume production.[7]

**Reading.** A sovereign launch programme that funds vehicles but not engine-production capacity will be engine-limited. The bottleneck is a manufacturing and qualification capability, which is exactly what the Seam grid calls `M8 Specialized Manufacturing` and `M1 Aerospace`.

## 3. Where the bottleneck sits on the Seam

| Cell | Question for a reading |
|---|---|
| `APP-M7` Applications × Space | Is launch access bought as a service, built, or partnered? |
| `SDL-M8` Sovereign Decision Layer × Specialized Manufacturing | Is there a national record of who is qualified to make turbomachinery, so requalification is a known cost rather than a discovered one? |
| `SDL-M9` Sovereign Decision Layer × Training & Simulation | Who certifies the propulsion workforce, and whose assessment counts? |
| `CHP-M7` Chips × Space | Where does radiation-hardened silicon come from, and from how many jurisdictions? |
| `INF-M7` Infrastructure × Space | Which test stands and ranges exist, and who controls their schedule? |

Contributors are invited to read these cells in [`seam/readings/`](../../seam/readings/) and to propose eval tasks in [`evals/`](../../evals/).

## 4. The ramp questions

A credible ramp plan answers six questions. Each is an open issue for this repository.

1. **Engines per year.** What production rate does the target launch cadence imply, counting test and spare engines?
2. **Turbopump route.** Domestic design, licensed allied design, or imported units? What does each imply for time to first flight and for export-control exposure?
3. **Qualification capacity.** How many hot-fire test slots exist, and is test-stand time the real constraint?
4. **Workforce.** Which occupations have no domestic training pipeline today? Liquid-propulsion and turbomachinery engineering are the obvious first candidates.
5. **Inputs.** Which materials and parts — specialty alloys, magnets, radiation-hardened silicon — are single-sourced or come from a distant jurisdiction?
6. **Jurisdiction.** For each item above, who has legal reach over the design data and the production line? The test is jurisdiction, not physical location.

## 5. A synthetic ramp model (to be built in the open)

The roadmap includes a small, fully synthetic model. It will take launch cadence, engines per vehicle, reuse rate, test-engine allowance and per-line throughput as inputs, and output the engine lines and test slots required. All parameters will be illustrative and replaceable. Contributions are welcome under the `launch` track.

## Sources

1. Government of Canada, *Security, Sovereignty, Prosperity: Canada's Defence Industrial Strategy* (February 2026). https://www.canada.ca/content/dam/dnd-mdn/documents/reports/industrial-strategy/defence-industrial-strategy-en.pdf
2. Prime Minister of Canada, "Prime Minister Carney launches Canada's first Defence Industrial Strategy" (17 February 2026). https://www.pm.gc.ca/en/news/news-releases/2026/02/17/prime-minister-carney-launches-canadas-first-defence-industrial
3. Department of National Defence, "Minister McGuinty announces strategic investments in sovereign space launch" (March 2026). https://www.canada.ca/en/department-national-defence/news/2026/03/minister-mcguinty-announces-strategic-investments-in-sovereign-space-launch.html
4. Government of Canada, "Launch the North: Accelerating Canada's sovereign access to space."
5. Harry W. Jones, NASA Ames Research Center, "The Recent Large Reduction in Space Launch Cost," ICES-2018-81 (2018). https://ntrs.nasa.gov/api/citations/20200001093/downloads/20200001093.pdf
6. German Aerospace Center (DLR), "Rocket engines: With turbopumps at the technical limit" (12 October 2021). https://www.dlr.de/en/ra/latest/news/rocket-engines-with-turbopumps-at-the-technical-limit
7. Liz Stein, Prime Movers Lab, "Bottlenecks in Rocket Engine Production May Slow the Space Economy Flywheel" (19 January 2022). https://medium.com/prime-movers-lab/bottlenecks-in-rocket-engine-production-may-slow-the-space-economy-flywheel-a51594c510ca

*Declaration of interest: Element Ventures (Canada) Ltd. maintains this repository and works on supply-chain coordination infrastructure in this sector. Postures and questions here are analytic framings for open debate, not determinations. This paper is not investment, financial or legal advice.*
