OPENQASM 3.1;
include "stdgates.inc";
qubit[8] leqo_reg;
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
/* Start node b5040828-71c1-4ee6-8875-3c1ce2f6981f */
let leqo_9820dbf19ae55a3cb0848f74ebd4ad39_literal = leqo_reg[{2}];
@leqo.output 0
let leqo_9820dbf19ae55a3cb0848f74ebd4ad39_out = leqo_9820dbf19ae55a3cb0848f74ebd4ad39_literal;
/* End node b5040828-71c1-4ee6-8875-3c1ce2f6981f */
/* Start node 5f841748-79e3-4a56-be98-b650d8229eec */
let leqo_4682c8439b3b5369ab91bfeabba34609_literal = leqo_reg[{3}];
@leqo.output 0
let leqo_4682c8439b3b5369ab91bfeabba34609_out = leqo_4682c8439b3b5369ab91bfeabba34609_literal;
/* End node 5f841748-79e3-4a56-be98-b650d8229eec */
/* Start node 15a581b7-d3bc-466d-a7c3-b48ac55bfe8b */
let leqo_8aaf1be59c055f6297af79e78c3419d9_literal = leqo_reg[{4}];
@leqo.output 0
let leqo_8aaf1be59c055f6297af79e78c3419d9_out = leqo_8aaf1be59c055f6297af79e78c3419d9_literal;
/* End node 15a581b7-d3bc-466d-a7c3-b48ac55bfe8b */
/* Start node 185ddc2f-34f7-415a-9e8c-bd0f7cd1ff62 */
@leqo.input 0
let leqo_361ab059e1005696a32d68dfa1946b38_merger_input_0 = leqo_reg[{1}];
@leqo.input 1
let leqo_361ab059e1005696a32d68dfa1946b38_merger_input_1 = leqo_reg[{0}];
@leqo.output 0
let leqo_361ab059e1005696a32d68dfa1946b38_merger_output = leqo_361ab059e1005696a32d68dfa1946b38_merger_input_0 ++ leqo_361ab059e1005696a32d68dfa1946b38_merger_input_1;
/* End node 185ddc2f-34f7-415a-9e8c-bd0f7cd1ff62 */
/* Start node 9c00c8db-e91f-409a-95ac-d6deab5366e5 */
@leqo.input 0
let leqo_d6fb540b5a5b54958c15fbeb7a0533fb_q0 = leqo_reg[{4}];
x leqo_d6fb540b5a5b54958c15fbeb7a0533fb_q0;
@leqo.output 0
let leqo_d6fb540b5a5b54958c15fbeb7a0533fb_q0_out = leqo_d6fb540b5a5b54958c15fbeb7a0533fb_q0;
/* End node 9c00c8db-e91f-409a-95ac-d6deab5366e5 */
/* Start node c90ea26a-521e-453d-8be5-2ea757ec044a */
@leqo.input 0
let leqo_3a76e46ae2835fe990b975c66e9cb4ba_q0 = leqo_reg[{1, 0}];
h leqo_3a76e46ae2835fe990b975c66e9cb4ba_q0;
@leqo.output 0
let leqo_3a76e46ae2835fe990b975c66e9cb4ba_q0_out = leqo_3a76e46ae2835fe990b975c66e9cb4ba_q0;
/* End node c90ea26a-521e-453d-8be5-2ea757ec044a */
/* Start node 17e73681-ae4e-4bc0-a85d-e7c92f127fc0 */
@leqo.input 0
let leqo_5339e910d08252a2921f1b7b77a6346e_merger_input_0 = leqo_reg[{4}];
@leqo.input 1
let leqo_5339e910d08252a2921f1b7b77a6346e_merger_input_1 = leqo_reg[{3}];
@leqo.input 2
let leqo_5339e910d08252a2921f1b7b77a6346e_merger_input_2 = leqo_reg[{2}];
@leqo.output 0
let leqo_5339e910d08252a2921f1b7b77a6346e_merger_output = leqo_5339e910d08252a2921f1b7b77a6346e_merger_input_0 ++ leqo_5339e910d08252a2921f1b7b77a6346e_merger_input_1 ++ leqo_5339e910d08252a2921f1b7b77a6346e_merger_input_2;
/* End node 17e73681-ae4e-4bc0-a85d-e7c92f127fc0 */
/* Start node 6ca13c69-36cf-4771-b8c4-0f5804cc7d6e */
@leqo.input 0
let leqo_b8f3c6982d375661bb24e30358b24281_q34 = leqo_reg[{1, 0}];
let leqo_b8f3c6982d375661bb24e30358b24281_q35 = leqo_reg[{7}];
let leqo_b8f3c6982d375661bb24e30358b24281_q31 = leqo_b8f3c6982d375661bb24e30358b24281_q34 ++ leqo_b8f3c6982d375661bb24e30358b24281_q35;
@leqo.input 1
let leqo_b8f3c6982d375661bb24e30358b24281_q32 = leqo_reg[{4, 3, 2}];
let leqo_b8f3c6982d375661bb24e30358b24281_q33 = leqo_reg[{5, 6}];
ccx leqo_b8f3c6982d375661bb24e30358b24281_q34[1], leqo_b8f3c6982d375661bb24e30358b24281_q32[1], leqo_b8f3c6982d375661bb24e30358b24281_q32[2];
cx leqo_b8f3c6982d375661bb24e30358b24281_q34[1], leqo_b8f3c6982d375661bb24e30358b24281_q32[1];
ccx leqo_b8f3c6982d375661bb24e30358b24281_q34[0], leqo_b8f3c6982d375661bb24e30358b24281_q32[0], leqo_b8f3c6982d375661bb24e30358b24281_q33[1];
cx leqo_b8f3c6982d375661bb24e30358b24281_q34[0], leqo_b8f3c6982d375661bb24e30358b24281_q32[0];
ccx leqo_b8f3c6982d375661bb24e30358b24281_q33[0], leqo_b8f3c6982d375661bb24e30358b24281_q32[0], leqo_b8f3c6982d375661bb24e30358b24281_q33[1];
ccx leqo_b8f3c6982d375661bb24e30358b24281_q33[1], leqo_b8f3c6982d375661bb24e30358b24281_q32[1], leqo_b8f3c6982d375661bb24e30358b24281_q32[2];
cx leqo_b8f3c6982d375661bb24e30358b24281_q33[1], leqo_b8f3c6982d375661bb24e30358b24281_q32[1];
ccx leqo_b8f3c6982d375661bb24e30358b24281_q33[0], leqo_b8f3c6982d375661bb24e30358b24281_q32[0], leqo_b8f3c6982d375661bb24e30358b24281_q33[1];
cx leqo_b8f3c6982d375661bb24e30358b24281_q34[0], leqo_b8f3c6982d375661bb24e30358b24281_q32[0];
ccx leqo_b8f3c6982d375661bb24e30358b24281_q34[0], leqo_b8f3c6982d375661bb24e30358b24281_q32[0], leqo_b8f3c6982d375661bb24e30358b24281_q33[1];
cx leqo_b8f3c6982d375661bb24e30358b24281_q33[0], leqo_b8f3c6982d375661bb24e30358b24281_q32[0];
cx leqo_b8f3c6982d375661bb24e30358b24281_q34[0], leqo_b8f3c6982d375661bb24e30358b24281_q32[0];
@leqo.output 0
let leqo_b8f3c6982d375661bb24e30358b24281_out = leqo_b8f3c6982d375661bb24e30358b24281_q32;
/* End node 6ca13c69-36cf-4771-b8c4-0f5804cc7d6e */
/* Start node f901f700-5945-4739-a078-88798fe3bebc */
@leqo.input 0
let leqo_9f567c19326f57288f0bd799e35e705b_q = leqo_reg[{4, 3, 2}];
bit[1] leqo_9f567c19326f57288f0bd799e35e705b_result = measure leqo_9f567c19326f57288f0bd799e35e705b_q[{2}];
@leqo.output 0
let leqo_9f567c19326f57288f0bd799e35e705b_out = leqo_9f567c19326f57288f0bd799e35e705b_result;
@leqo.output 1
let leqo_9f567c19326f57288f0bd799e35e705b_qubit_out = leqo_9f567c19326f57288f0bd799e35e705b_q;
/* End node f901f700-5945-4739-a078-88798fe3bebc */
