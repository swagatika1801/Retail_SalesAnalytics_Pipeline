"""
============================================================
Retail Store Sales Analysis - Main Runner
Author: Kanhaiya Thakur
Run this file to execute the complete analysis pipeline.
============================================================
"""

import subprocess
import sys
import os

BASE = os.path.dirname(__file__)

scripts = [
    ("SQL Analysis",       os.path.join(BASE, "python/sql_runner.py")),
    ("Python Analysis",    os.path.join(BASE, "python/analysis.py")),
    ("Excel Report",       os.path.join(BASE, "python/excel_report.py")),
    ("Visualizations",     os.path.join(BASE, "python/visualizations.py")),
]

print("=" * 60)
print("  RETAIL SALES ANALYSIS - FULL PIPELINE")
print("=" * 60)

for name, path in scripts:
    print(f"\n🚀 Running: {name}")
    print("─" * 40)
    result = subprocess.run([sys.executable, path], capture_output=False)
    if result.returncode != 0:
        print(f"❌ {name} failed with exit code {result.returncode}")
    else:
        print(f"✅ {name} completed.")

print("\n" + "=" * 60)
print("  ALL TASKS COMPLETE!")
print("  Output files are in: visualizations/ and excel_output/")
print("=" * 60)
