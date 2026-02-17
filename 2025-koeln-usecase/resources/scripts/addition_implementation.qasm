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
