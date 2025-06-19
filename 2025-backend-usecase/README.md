# LEQO Backend 2025 Tutorial

> [!TIP]
> For detailed instructions have a look at the [documentation](https://leqo-framework.github.io/leqo-backend/)

## Prerequisites

- [Install Docker](https://docs.docker.com/install/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

## 0. Service Setup

### Docker Setup

In the [./docker](docker) directory you will find a simple docker compose file to spin up the whole project.

Create a new directory on your system and download the [docker-compose.yml](docker/docker-compose.yml) into that folder.
Then run the following command inside the folder:

```sh
docker compose up -d
```

> [!NOTE]
> The `-d` flag is **optional**.
> It runs the containers in the background (detached mode) and keeps them running even after the command execution is complete.

> [!WARNING]
> If you are using docker desktop, ensure it's running

> [!WARNING]
> On linux you will likely have to use `sudo` to communicate with the docker socket.

### Configure the Frontend

You need to configure the path to the backend in the frontend UI.

1. Open the frontend
1. Click on **Configuration**
1. Insert `http://localhost:8000` into the "Low-Code Backend Endpoint" field
1. Click on **Save**

## 1. Model a simple Quantum Algorithm

For demonstration purpose we will model a simple addition algorithm that uses qubits to add to integers.

1. Start by dragging two "int" nodes from the palette on the left of the screen.
1. Each integer should be connected to an "Encode Value" node.
1. The resulting qubits from the encoding will both be connected to an "Arithmetic Operator" node.
1. We can the measure the result of the addition with a "Measurement" node.

The final graph should look like this:

![Addition UseCase](./docs/graphics/addition.png)

## 2. Specify implementations

The backend is capable of providing implementations for simple nodes like "int" and "measure" but does not know how to generate advanced implementations like an encoding or addition.

In production these implementations will be ready from a database.
To simplify things for testing, we will simply manually provide an implementation for these three nodes:

### Encoding Nodes

```
OPENQASM 3.0;
include "stdgates.inc";

@leqo.input 0
int[32] val;

qubit[3] q;
x q[0];

@leqo.output 0
let out = q;
```

### Arithmetic Operator

```
OPENQASM 3.0;
include "stdgates.inc";

@leqo.input 0
qubit[3] q31;

@leqo.input 1
qubit[3] q32;

qubit[2] q33;ccx q31[1], q32[1], q32[2];
cx q31[1], q32[1];
ccx q31[0], q32[0], q33[1];
cx q31[0], q32[0];
ccx q33[0], q32[0], q33[1];
ccx q33[1], q32[1], q32[2];
cx q33[1], q32[1];
ccx q33[0], q32[0], q33[1];
cx q31[0], q32[0];
ccx q31[0], q32[0], q33[1];
cx q33[0], q32[0];
cx q31[0], q32[0];

@leqo.output 0
let out = q32;
```

> [!TIP]
> Detailed explanation on the `@leqo.*` annotations can be found in the [backend documentation](https://leqo-framework.github.io/leqo-backend/usage/annotations.html#annotations).

## 3. Specify parameters

Let's specify the values of the two integers we want to add and select which qubits to measure.

## 4. Generate final program

Now, all that's left to do is to generate actual `OPENQasm 3` code we can execute on some quantum computer.

To do so, simply click "Send to Backend".

> [!WARNING]
> Currently the implementation will only be visible in the DevTools of the frontend!
