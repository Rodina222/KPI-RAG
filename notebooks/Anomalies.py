import json
from pathlib import Path

fault_types = set()

for file in Path("data/TelecomTS").rglob("*.jsonl"):
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            sample = json.loads(line)

            anomaly = sample.get("anomalies", {})

            if anomaly.get("exists"):
                fault_type = anomaly.get("type")
                if fault_type:
                    fault_types.add(fault_type)

print("Number of anomaly types:", len(fault_types))

for fault in sorted(fault_types):
    print(fault)