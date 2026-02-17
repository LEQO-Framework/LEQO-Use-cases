# LEQO Backend - Koeln - 2025 Tutorial

> [!TIP]
> For detailed instructions have a look at the [documentation](https://leqo-framework.github.io/leqo-backend/)

## Prerequisites

- [Install Docker](https://docs.docker.com/install/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)
- [Clone this repository](https://github.com/LEQO-Framework/LEQO-Use-cases)
- (Optional) [Install Python](https://www.python.org/downloads/)
- (Optional) [Install curl](https://curl.se/download.html) and [Install jq](https://jqlang.org/download/)

## 1. Service Setup

### Docker Setup

Navigate to the [./docker/](./docker/) directory.
Then run the following command:

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

1. Open the frontend in a web browser: [http://localhost](http://localhost)
1. Click on **Configuration**
1. Insert `http://localhost:8000` into the "Low-Code Backend Endpoint" field
1. Click on **Save**

### (Optional) Insert Implementations into the Backend

If you want to load the implementation for the _Arithmetic Operator_ node later via the database, you can use the lightweight web helper or one of the terminal commands below.

#### Use the Web Helper (no terminal required)

1. Open [./resources/web/leqo-backend-client.html](./resources/web/leqo-backend-client.html) in a web browser.<br>
   Double-clicking the file usually works; if your browser blocks `file://` requests, serve the directory with `python -m http.server` and open the reported URL.
1. Ensure the **Backend host** field contains `http://localhost:8000` (or adjust it to match your deployment).
1. Keep the default payload from `addition_insert.json` or paste another JSON payload into the textarea.
1. Click **Send to /insert** and inspect the response panel for the backend status and message.

> [!NOTE]
> The helper page also offers a **Fetch /result** button that can be used after you trigger a compile request (see [Test the Backend](#3-test-the-backend-via-terminal-or-web-helper)).

#### Use Python

Navigate to the [./resources/scripts/](./resources/scripts/) directory and execute:

```sh
python3 ./request_helper.py ./addition_insert.json
```

#### Use curl on Linux

```sh
curl -H "Content-Type: application/json" --data @./addition_insert.json http://localhost:8000/insert
```

#### Use Powershell on Windows

```Powershell
irm -Method Post -Headers @{ "Content-Type" = "application/json" } -Uri http://localhost:8000/insert -InFile ./addition_insert.json
```

> [!TIP]
> Detailed explanation on the `@leqo.*` annotations used in inserted implementation can be found in the [backend documentation](https://leqo-framework.github.io/leqo-backend/usage/annotations.html#annotations).

## 2. Test the Backend via the Frontend

### Build the Model

We will now model this simple algorithm in the frontend:

![model in frontend](./resources/graphics/modeled_graph.png)

> [!TIP]
> Shortcut: You can directly load the stored [frontend model](./resources/scripts/frontend_model.json) via **Open** inside the frontend UI.

Here is a short textual description on how to build it:

1. Drag five _|0⟩_ nodes (under **Circuit-level Nodes**) into the graph
1. Drag one _H_ nodes (under **Circuit-level Nodes**) into the graph
1. Drag one _X_ nodes (under **Circuit-level Nodes**) into the graph
1. Drag two _Merger_ nodes (under **Circuit-level Nodes**) into the graph
    - Click on the _Merger_ node in the graph
    - Insert into **Number of Inputs** in the right panel:
        - 2 for the upper _Merger_
        - 3 for the lower _Merger_
1. Drag one _Arithmetic Operator_ node (under **Operators**) into the graph
    - If you have not yet inserted the implementation as described [here](#optional-insert-implementations-into-the-backend), you need to specify it now:
        - Click on the _Arithmetic Operator_ node in the graph
        - Insert the content of [addition_impl.txt](./resources/scripts/addition_impl.txt) into the **implementation Content** field in the right panel
1. Drag one _Measurement_ node (under **Boundary Nodes**) into the graph
    - Click on the _Measurement_ node in the graph
    - Insert into **Indicies** in the right panel: 2
1. Connect the nodes as can also be seen in the image:
    - Two qubits _|0⟩_ into the upper merger
    - The output of this _Merger_ into the Hadamard _H_ gate
    - The output of the Hadamard into the **Input 1** of the _Arithmetic Operator_
    - One of the lower qubits into the XGate _X_ gate
    - The XGate output and the remaining qubits into the lower _Merger_
    - The output of this _Merger_ into the **Input 2** of the _Arithmetic Operator_
    - The output of the _Arithmetic Operator_ into the _Measurement_

### See the Result

The frontend is unable to display the result yet.
However, we can see it via the DevTools of our web browser

1. Open the DevTools
1. Navigate to the **Network** tab
1. Press on **Send to Backend** in the frontend
1. You should now see a successful request in the **Network** tab:
   ![result in dev-tools](./resources/graphics/result_in_dev_tools.png)
1. Clicking on request should open the result in another tab

## 3. Test the Backend via Terminal or Web Helper

The backend can also be accessed directly using the helper webpage or the terminal.
Open [./resources/web/leqo-backend-client.html](./resources/web/leqo-backend-client.html) to call `/result/<uuid>` after triggering a compile request—the page displays the HTTP status and body returned by the backend.

The sections below keep the Python and curl variants using a stored compile_request with the same semantic as the model in the [frontend section](#2-test-the-backend-via-the-frontend).

> [!WARNING]
> All commands in this section assume that you are in the [./resources/scripts/](./resources/scripts/) directory.

### Send Compile Request with Hardcoded _Arithmetic Operator_ Implementation

This variation works without the insert described [here](#optional-insert-implementations-into-the-backend).
You can use one of the following options:

#### Use Python

```sh
python3 ./request_helper.py compile_request_with_addition.json /compile
```

#### Use curl and jq on Linux

```sh
UUID=$(curl -L -H "Content-Type: application/json" --data @./compile_request_with_addition.json http://localhost:8000/compile | jq -r '.uuid') \
&& for i in $(seq 1 10); do if [ "$(curl -s "http://localhost:8000/status/$UUID" | jq -r '.status')" = "completed" ]; then break; else sleep 0.5; fi; done \
&& curl "http://localhost:8000/result/$UUID"
```

#### Use Powershell on Windows

```Powershell
&{
    $pollLocation = (iwr -Method Post -Uri http://localhost:8000/compile -InFile ./compile_request_with_addition.json -Headers @{ "Content-Type" = "application/json" } -MaximumRedirection 0).Headers["Location"]
    $status = {}
    do {
        $status = iwr -Uri $pollLocation | ConvertFrom-Json
        sleep 0.5
    } while($status.status -eq "in progress")
    irm $status.result
}
```

### Send Compile Request with Database Retrieval

This variation uses the implementation from the database, assuming you inserted it [here](#optional-insert-implementations-into-the-backend).
You can use one of the following options:

#### Use Python

```sh
python3 ./request_helper.py compile_request_without_addition.json /compile
```

#### Use curl and jq on Linux

```sh
UUID=$(curl -L -H "Content-Type: application/json" --data @./compile_request_without_addition.json http://localhost:8000/compile | jq -r '.uuid') \
&& for i in $(seq 1 10); do if [ "$(curl -s "http://localhost:8000/status/$UUID" | jq -r '.status')" = "completed" ]; then break; else sleep 0.5; fi; done \
&& curl "http://localhost:8000/result/$UUID"
```

#### Use Powershell on Windows

```Powershell
&{
    $pollLocation = (iwr -Method Post -Uri http://localhost:8000/compile -InFile ./compile_request_without_addition.json -Headers @{ "Content-Type" = "application/json" } -MaximumRedirection 0).Headers["Location"]
    $status = {}
    do {
        $status = iwr -Uri $pollLocation | ConvertFrom-Json
        sleep 0.5
    } while($status.status -eq "in progress")
    irm $status.result
}
```

## 4. Analyse the Result

All the methods described above should give you the same result matching [./resources/scripts/compile_result.qasm](./resources/scripts/compile_result.qasm).

> [!WARNING]
> Building the model yourself will result in different node ids in the frontend and therefore in a different output!

The following backend behavior can be observed on by this example:

### All Qubit Declarations to the Top

The backend declares all qubits using one big qubit register at the top of the program.

```qasm
OPENQASM 3.1;
include "stdgates.inc";
qubit[8] leqo_reg;
```

### Renaming

All identifier where prefixed with a hash corresponding to one frontend node.

```qasm
/* Start node d703bb61-3410-43ce-be51-4750fb7b9f0f */
let leqo_b8d0652a44085419a43031521aab072e_literal = leqo_reg[{0}];
@leqo.output 0
let leqo_b8d0652a44085419a43031521aab072e_out = leqo_b8d0652a44085419a43031521aab072e_literal;
/* End node d703bb61-3410-43ce-be51-4750fb7b9f0f */
/* Start node 5b427a52-047a-4cbc-b4f4-6705a2b4b0bb */
let leqo_b7e9559cda9e59e2ae8e5e0b5a9689b0_literal = leqo_reg[{1}];
@leqo.output 0
let leqo_b7e9559cda9e59e2ae8e5e0b5a9689b0_out = leqo_b7e9559cda9e59e2ae8e5e0b5a9689b0_literal;
/* End node 5b427a52-047a-4cbc-b4f4-6705a2b4b0bb */
```

### Automated Node Generation

The _Merger_ nodes are auto generated matching their input.

```qasm
/* Start node 185ddc2f-34f7-415a-9e8c-bd0f7cd1ff62 */
@leqo.input 0
let leqo_361ab059e1005696a32d68dfa1946b38_merger_input_0 = leqo_reg[{1}];
@leqo.input 1
let leqo_361ab059e1005696a32d68dfa1946b38_merger_input_1 = leqo_reg[{0}];
@leqo.output 0
let leqo_361ab059e1005696a32d68dfa1946b38_merger_output = leqo_361ab059e1005696a32d68dfa1946b38_merger_input_0 ++ leqo_361ab059e1005696a32d68dfa1946b38_merger_input_1;
/* End node 185ddc2f-34f7-415a-9e8c-bd0f7cd1ff62 */
```

Furthermore, the _|0⟩_, _H_ and _Measurement_ nodes are also auto generated.

### Size Cast

The first input into the _Arithmetic Operator_ node is too small, the backend casts them up to make them fit.

```qasm
/* Start node 6ca13c69-36cf-4771-b8c4-0f5804cc7d6e */
@leqo.input 0
let leqo_b8f3c6982d375661bb24e30358b24281_q34 = leqo_reg[{1, 0}];
let leqo_b8f3c6982d375661bb24e30358b24281_q35 = leqo_reg[{7}];
let leqo_b8f3c6982d375661bb24e30358b24281_q31 = leqo_b8f3c6982d375661bb24e30358b24281_q34 ++ leqo_b8f3c6982d375661bb24e30358b24281_q35;
```

This is done by defining a register of ancillae below the input and map the used identifier to the concatenation of the input with the ancilla register.

### Deterministic Output

Sending the compile request multiple times yields the same result.

### Compatible with Qiskit

The resulting OpenQASM is compatible with Qiskit, giving following result:

```
                                                ┌───┐
                                    leqo_reg_0: ┤ H ├──■─────────■──────────────────────────────────────────────────
                                                ├───┤  │         │
                                    leqo_reg_1: ┤ H ├──┼────■────┼────■───────────────────────────■────■─────────■──
                                                └───┘┌─┴─┐  │    │    │       ┌───┐     ┌─┐       │    │         │
                                    leqo_reg_2: ─────┤ X ├──┼────┼────┼───────┤ X ├─────┤M├───────┼────┼─────────┼──
                                                     └─┬─┘  │  ┌─┴─┐  │       └─┬─┘┌───┐└╥┘       │    │         │
                                    leqo_reg_3: ───────■────┼──┤ X ├──┼─────────■──┤ X ├─╫────────┼────┼─────────┼──
                                                ┌───┐       │  └───┘┌─┴─┐       │  └─┬─┘ ║      ┌─┴─┐  │  ┌───┐┌─┴─┐
                                    leqo_reg_4: ┤ X ├───────■───────┤ X ├──■────┼────┼───╫───■──┤ X ├──■──┤ X ├┤ X ├
                                                └───┘       │       └───┘  │    │    │   ║   │  └───┘  │  └─┬─┘└───┘
                                    leqo_reg_5: ────────────┼──────────────■────┼────┼───╫───■─────────┼────■───────
                                                          ┌─┴─┐          ┌─┴─┐  │    │   ║ ┌─┴─┐     ┌─┴─┐
                                    leqo_reg_6: ──────────┤ X ├──────────┤ X ├──■────■───╫─┤ X ├─────┤ X ├──────────
                                                          └───┘          └───┘           ║ └───┘     └───┘
                                    leqo_reg_7: ─────────────────────────────────────────╫──────────────────────────
                                                                                         ║
leqo_9f567c19326f57288f0bd799e35e705b_result: 1/═════════════════════════════════════════╩══════════════════════════
                                                                                         0
```

> [!NOTE]
> This picture was produced with [compile_result_with_qiskit.py](./resources/scripts/compile_result_with_qiskit.py).
> But it requires a local Qiskit installation.

### More Features not visible in this Example

- Optimization via ancilla reusage
- Inlining of constants
- Convert from OpenQASM 2 to OpenQASM 3
- Nested nodes like If-Then-Else and Repeat
