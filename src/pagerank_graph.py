#!/usr/bin/env python3
import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

class InternalLinkGraph:
    def __init__(self, damping=0.85, max_iter=50, tol=1e-6):
        self.damping = damping
        self.max_iter = max_iter
        self.tol = tol
        self.adj = defaultdict(set)
        self.all_nodes = set()
        self.in_degree = defaultdict(int)

    def load_crawl_csv(self, csv_path):
        with open(csv_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                src = row.get("source_url") or row.get("Source")
                dest = row.get("destination_url") or row.get("Destination")
                if src and dest:
                    s, d = src.strip(), dest.strip()
                    self.all_nodes.add(s)
                    self.all_nodes.add(d)
                    self.adj[s].add(d)
                    self.in_degree[d] += 1
                elif src:
                    self.all_nodes.add(src.strip())

    def compute_pagerank(self):
        nodes = list(self.all_nodes)
        N = len(nodes)
        if N == 0:
            return {}
        pr = {n: 1.0 / N for n in nodes}

        for _ in range(self.max_iter):
            new_pr = {}
            sink_sum = sum(pr[n] for n in nodes if len(self.adj[n]) == 0)
            for d in nodes:
                in_sum = sum(pr[s] / len(self.adj[s]) for s in nodes if d in self.adj[s])
                new_pr[d] = ((1.0 - self.damping) / N) + self.damping * (in_sum + sink_sum / N)
            diff = sum(abs(new_pr[n] - pr[n]) for n in nodes)
            pr = new_pr
            if diff < self.tol:
                break

        max_v = max(pr.values()) if pr else 1.0
        return {n: round((v / max_v) * 100, 2) for n, v in pr.items()}

    def find_orphans(self):
        return [n for n in self.all_nodes if self.in_degree[n] == 0]

    def export_html(self, out_path, pr):
        orphans = self.find_orphans()
        rows = "".join([f"<tr><td><code>{u}</code></td><td>{s}</td><td>{self.in_degree[u]}</td><td>{'<b style="color:red">ORPHAN</b>' if u in orphans else '<b style="color:green">OK</b>'}</td></tr>" for u, s in sorted(pr.items(), key=lambda x: x[1], reverse=True)])
        html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>PageRank Report</title><style>body{{font-family:sans-serif;padding:20px;background:#0f172a;color:#f8fafc}}table{{width:100%;border-collapse:collapse}}th,td{{padding:8px;border:1px solid #334155}}th{{background:#0284c7}}code{{color:#38bdf8}}</style></head><body><h1>Internal Link Equity & Orphan Radar</h1><p>Pages: {len(self.all_nodes)} | Orphans: {len(orphans)}</p><table><tr><th>URL</th><th>Equity Score</th><th>Inlinks</th><th>Status</th></tr>{rows}</table></body></html>"
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        Path(out_path).write_text(html, encoding="utf-8")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True)
    p.add_argument("--report", default="reports/sample_report.html")
    args = p.parse_args()

    g = InternalLinkGraph()
    g.load_crawl_csv(args.csv)
    pr = g.compute_pagerank()
    g.export_html(args.report, pr)
    print(f"Computed PageRank for {len(g.all_nodes)} URLs -> {args.report}")

if __name__ == "__main__":
    main()
