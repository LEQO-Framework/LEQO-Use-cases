from pathlib import Path

from qiskit.qasm3 import loads

with (Path(__file__).parent / "compile_result.qasm").open() as f:
    print(loads(f.read()))
