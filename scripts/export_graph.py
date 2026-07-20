#!/usr/bin/env python3
"""
Export the Foam vault's wikilink graph to portable formats.

Outputs (into ./graph/):
  - graph.json  : node-link data (nodes typed by frontmatter, edges from [[wikilinks]])
  - graph.dot   : Graphviz DOT (open in Gephi/Graphviz/Cytoscape, or `dot -Tsvg`)
  - graph.html  : self-contained interactive graph (vis-network from CDN) — GitHub-Pages ready

Pure standard library. No pip install required.
Run from the repo root:  python3 scripts/export_graph.py
"""

import os, re, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "graph")
os.makedirs(OUT, exist_ok=True)

SRC_GLOBS = ["notes/*.md", "mocs/*.md", "tags.md"]
WIKILINK = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
REFDEF = re.compile(r"^\[[^\]]+\]:\s")          # skip Foam's link-reference-definition footer
FM_TYPE = re.compile(r"^type:\s*(\w+)", re.M)
FM_STATUS = re.compile(r"^status:\s*(\w+)", re.M)

COLOR = {  # by type / status
    "moc":        "#b3541e",   # hubs — warm
    "developed":  "#1f6f54",
    "seed":       "#2f80a8",
    "stub":       "#8aa0ad",
    "reference":  "#777777",
    "default":    "#2f80a8",
}

def classify(text, ntype):
    if ntype == "moc":
        return "moc"
    if ntype == "reference":
        return "reference"
    m = FM_STATUS.search(text)
    return m.group(1) if m else "default"

nodes, edges = {}, []
for pat in SRC_GLOBS:
    for path in glob.glob(os.path.join(ROOT, pat)):
        base = os.path.splitext(os.path.basename(path))[0]
        text = open(path, encoding="utf-8").read()
        ntype = (FM_TYPE.search(text) or [None, "permanent"])[1] if FM_TYPE.search(text) else "permanent"
        nodes[base] = {"id": base, "type": ntype, "group": classify(text, ntype)}

for pat in SRC_GLOBS:
    for path in glob.glob(os.path.join(ROOT, pat)):
        base = os.path.splitext(os.path.basename(path))[0]
        for line in open(path, encoding="utf-8"):
            if REFDEF.match(line):
                continue
            for m in WIKILINK.finditer(line):
                tgt = m.group(1).strip()
                # case-insensitive resolve to an existing node
                if tgt not in nodes:
                    hit = next((k for k in nodes if k.lower() == tgt.lower()), None)
                    if hit:
                        tgt = hit
                if tgt in nodes and tgt != base:
                    edges.append((base, tgt))

# degree for sizing
deg = {n: 0 for n in nodes}
for a, b in edges:
    deg[a] += 1; deg[b] += 1

data = {
    "nodes": [{**v, "label": k, "value": deg[k] + 1, "color": COLOR.get(v["group"], COLOR["default"])}
              for k, v in nodes.items()],
    "edges": [{"from": a, "to": b} for a, b in sorted(set(edges))],
}

# ---- graph.json
json.dump(data, open(os.path.join(OUT, "graph.json"), "w"), indent=2, ensure_ascii=False)

# ---- graph.dot
with open(os.path.join(OUT, "graph.dot"), "w", encoding="utf-8") as f:
    f.write("digraph vault {\n  graph [overlap=false, splines=true];\n")
    f.write('  node [style=filled, fontname="Helvetica", shape=ellipse];\n')
    for k, v in nodes.items():
        f.write(f'  "{k}" [fillcolor="{COLOR.get(v["group"], COLOR["default"])}", fontcolor=white];\n')
    for a, b in sorted(set(edges)):
        f.write(f'  "{a}" -> "{b}";\n')
    f.write("}\n")

# ---- graph.html (self-contained, interactive)
html = """<!doctype html><html><head><meta charset="utf-8">
<title>Clearing and Settling the Realm — knowledge graph</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.9/dist/vis-network.min.js"></script>
<style>
  html,body{margin:0;height:100%;background:#f7f5f1;font-family:Helvetica,Arial,sans-serif}
  #net{width:100%;height:100vh}
  #legend{position:fixed;top:12px;left:12px;background:#fffef9;border:1px solid #ddd;
          border-radius:8px;padding:10px 12px;font-size:13px;line-height:1.6;box-shadow:0 1px 4px rgba(0,0,0,.08)}
  .dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:middle}
  h1{font-size:14px;margin:0 0 6px}
</style></head><body>
<div id="legend"><h1>Knowledge graph</h1>
  <div><span class="dot" style="background:#b3541e"></span>MOC hub</div>
  <div><span class="dot" style="background:#2f80a8"></span>note (seed)</div>
  <div><span class="dot" style="background:#1f6f54"></span>note (developed)</div>
  <div><span class="dot" style="background:#8aa0ad"></span>concept stub</div>
</div>
<div id="net"></div>
<script>
const data = __DATA__;
const nodes = new vis.DataSet(data.nodes);
const edges = new vis.DataSet(data.edges.map(e => ({...e, arrows:"to"})));
new vis.Network(document.getElementById("net"), {nodes, edges}, {
  nodes:{shape:"dot", scaling:{min:6,max:34}, font:{size:14, face:"Helvetica"}},
  edges:{color:{color:"#c9c2b6", highlight:"#b3541e"}, width:0.6, smooth:{type:"continuous"}},
  physics:{barnesHut:{gravitationalConstant:-9000, springLength:130, springConstant:0.03},
           stabilization:{iterations:220}},
  interaction:{hover:true, tooltipDelay:120}
});
</script></body></html>"""
html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False))
open(os.path.join(OUT, "graph.html"), "w", encoding="utf-8").write(html)

print(f"nodes: {len(nodes)}  edges: {len(set(edges))}")
print("wrote graph/graph.json, graph/graph.dot, graph/graph.html")
top = sorted(deg.items(), key=lambda x: -x[1])[:6]
print("most-connected:", ", ".join(f"{k} ({d})" for k, d in top))
