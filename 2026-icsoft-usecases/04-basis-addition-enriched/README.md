# Basis Addition Use Case (Pre-enriched Nodes)

This use case demonstrates a compile-ready model where every node is already an
`implementation` node produced by enrichment. It focuses on a deterministic
2-bit basis addition example (`1 + 3`) and measures a 3-bit sum register.

## Files

- `basis_addition_enriched_2plus3.json`: pre-enriched model with implementation nodes.
- `basis_addition_enriched.ipynb`: compile + Qiskit simulation walkthrough.

## Compile with backend

```bash
curl -sS -X POST "http://localhost:8000/debug/compile" \
  -H "Content-Type: application/json" \
  --data @scripts/paper-results/06-basis-addition-enriched/basis_addition_enriched_2plus3.json
```

## Expected behavior

- The model encodes `1` and `3` in basis states, applies a 2-bit adder, and measures 3 output bits.
- The dominant decoded output should correspond to decimal `4` (bitstring formatting may vary by bit order convention in downstream tooling).
