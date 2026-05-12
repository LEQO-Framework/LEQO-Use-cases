# Ancilla + Uncompute Use Case (OpenQASM2 Input)

This use case demonstrates two things:

- **Ancilla handling** (`@leqo.reusable`, `@leqo.uncompute`, and width optimization effects)
- **OpenQASM 2 ingestion** (snippets use OpenQASM 2 syntax and LEQO comment annotations)
- **3-qubit logical output path** (the pipeline output is a 3-qubit register)

## Files

- `ancilla_uncompute_qasm2_opt.json`: same topology with `metadata.optimizeWidth = 1`
- `ancilla_uncompute_qasm2_no_opt.json`: same topology without width optimization
- `ancilla_qasm2.ipynb`: compile + Qiskit execution notebook, including explicit postprocessing for `if (false)` blocks in the non-optimized variant

## Compile with backend

Optimized variant:

```bash
curl -sS -X POST "http://localhost:8000/debug/compile" \
  -H "Content-Type: application/json" \
  --data @scripts/paper-results/05-ancilla-qasm2/ancilla_uncompute_qasm2_opt.json
```

Non-optimized variant:

```bash
curl -sS -X POST "http://localhost:8000/debug/compile" \
  -H "Content-Type: application/json" \
  --data @scripts/paper-results/05-ancilla-qasm2/ancilla_uncompute_qasm2_no_opt.json
```

## Expected high-level difference

- Optimized (`optimizeWidth: 1`): uncompute can be enabled, reusable ancillae can be reused, and total required register width drops to `qubit[5]`.
- Non-optimized: uncompute stays as disabled `if (false) { ... }` logic, no width-reuse optimization is applied, and total width remains `qubit[7]`.

## Qiskit import restriction (documented in notebook)

Qiskit's OpenQASM 3 importer does not accept constant-boolean branch conditions like `if (false) { ... }`.
The notebook therefore applies a transparent postprocessing step for the non-optimized variant:

- remove the disabled uncompute branch for simulation,
- keep the removed lines as comments in the postprocessed QASM so the transformation remains visible.
