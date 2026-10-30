import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from pagerank_graph import InternalLinkGraph

class TestGraph(unittest.TestCase):
    def test_orphan_detection(self):
        g = InternalLinkGraph()
        g.all_nodes = {"https://site.com/", "https://site.com/orphan"}
        self.assertIn("https://site.com/orphan", g.find_orphans())

if __name__ == "__main__":
    unittest.main()
