import sys

if len(sys.argv) < 2:
  print("Usage: axe_trace_filter.py <trace_file>", file=sys.stderr)
  sys.exit(1)

with open(sys.argv[1]) as trace_file:
  for line in trace_file:
    if line.startswith("### AXE"):
      print(line.replace("### AXE", "").strip())
