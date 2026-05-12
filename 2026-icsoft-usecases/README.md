# Paper Results Use Cases

This folder contains reproducible quantum low-code transformation pipeline use cases.

## Contents

- `docker-compose.paper.yaml`: starts the tool + PostgreSQL.
- `requirements.txt`: Python dependencies for running notebooks.
- `01-bell-states/`: Bell state use case.
- `02-state-preparation/`: state preparation use case.
- `03-qaoa/`: QAOA use case with a classical optimizer loop.
- `04-basis-addition-enriched/`: basis-addition use case built from pre-enriched implementation nodes.
- `05-ancilla-qasm2/`: ancilla reuse + uncompute use case with OpenQASM 2 snippets.


## Start the backend with Docker Compose

From the repository root:

```bash
docker compose -f scripts/paper-results/docker-compose.paper.yaml up -d
```

Backend endpoints:

- API root: `http://localhost:8000`
- Redoc: `http://localhost:8000/redoc`

## Run the notebooks

1. Create and activate a Python virtual environment.

```bash
python3 -m venv .venv-paper
source .venv-paper/bin/activate
pip install -r scripts/paper-results/requirements.txt
```

2. Launch Jupyter Lab.

3. Run the notebooks

Each notebook:

- loads model JSON files,
- posts the model to `POST /debug/compile`,
- captures the returned OpenQASM,
- executes circuits with Qiskit on Aer.

The notebooks execute backend-generated OpenQASM directly via Qiskit/Aer.
