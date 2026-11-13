from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister, transpile
from qiskit.circuit.classical import types
from qiskit_aer import AerSimulator
import qiskit.circuit.classical.expr as expr

qc = QuantumCircuit()
inputs_list = []
leqo_reg = QuantumRegister(3, "leqo_reg")
qc.add_register(leqo_reg)
"# Start node 53666072-9bb5-46b7-9d39-7e1fb96ffa87"
leqo_4e750a8805ea57b7b641d1da8b194934_literal = [leqo_reg[0]]
leqo_4e750a8805ea57b7b641d1da8b194934_out = (
    leqo_4e750a8805ea57b7b641d1da8b194934_literal
)
"# End node 53666072-9bb5-46b7-9d39-7e1fb96ffa87"
"# Start node 68d533bd-609c-4739-bd00-90bbf5d7a04f"
leqo_41008e45506555b6997aec150d19e6d2_state = [leqo_reg[1], leqo_reg[2]]
qc.h(leqo_41008e45506555b6997aec150d19e6d2_state[0])
qc.cx(
    leqo_41008e45506555b6997aec150d19e6d2_state[0],
    leqo_41008e45506555b6997aec150d19e6d2_state[1],
)
leqo_41008e45506555b6997aec150d19e6d2_state_out = (
    leqo_41008e45506555b6997aec150d19e6d2_state
)
"# End node 68d533bd-609c-4739-bd00-90bbf5d7a04f"
"# Start node 0ec6dfbb-0226-4a00-a139-1c3da31e751b"
leqo_c94de8581d895952bb91a4171110067e_q0 = [leqo_reg[0]]
qc.ry(2.0943951023931953, leqo_c94de8581d895952bb91a4171110067e_q0)
leqo_c94de8581d895952bb91a4171110067e_q0_out = leqo_c94de8581d895952bb91a4171110067e_q0
"# End node 0ec6dfbb-0226-4a00-a139-1c3da31e751b"
"# Start node c40f36d5-305d-4c31-b69f-97bb347127ac"
leqo_2e922240a26b5f00821562c0b6d94a32_splitter_input = [leqo_reg[1], leqo_reg[2]]
leqo_2e922240a26b5f00821562c0b6d94a32_splitter_output_0 = [
    leqo_2e922240a26b5f00821562c0b6d94a32_splitter_input[0]
]
leqo_2e922240a26b5f00821562c0b6d94a32_splitter_output_1 = [
    leqo_2e922240a26b5f00821562c0b6d94a32_splitter_input[1]
]
"# End node c40f36d5-305d-4c31-b69f-97bb347127ac"
"# Start node 5a3131c7-4039-4b26-8c14-2992b754ded8"
leqo_c537540385d65c7895335326160e879d_q0 = [leqo_reg[0]]
leqo_c537540385d65c7895335326160e879d_q1 = [leqo_reg[1]]
qc.cx(
    leqo_c537540385d65c7895335326160e879d_q0, leqo_c537540385d65c7895335326160e879d_q1
)
leqo_c537540385d65c7895335326160e879d_q0_out = leqo_c537540385d65c7895335326160e879d_q0
leqo_c537540385d65c7895335326160e879d_q1_out = leqo_c537540385d65c7895335326160e879d_q1
"# End node 5a3131c7-4039-4b26-8c14-2992b754ded8"
"# Start node cbbacff6-44a6-484d-bef2-8985504141d3"
leqo_4013a70985a85ee38c83a7f535b39337_q = [leqo_reg[1]]
leqo_4013a70985a85ee38c83a7f535b39337_result = ClassicalRegister(
    1, "leqo_4013a70985a85ee38c83a7f535b39337_result"
)
qc.add_register(leqo_4013a70985a85ee38c83a7f535b39337_result)
qc.measure(
    leqo_4013a70985a85ee38c83a7f535b39337_q[0],
    leqo_4013a70985a85ee38c83a7f535b39337_result,
)
leqo_4013a70985a85ee38c83a7f535b39337_out = leqo_4013a70985a85ee38c83a7f535b39337_result
leqo_4013a70985a85ee38c83a7f535b39337_qubit_out = (
    leqo_4013a70985a85ee38c83a7f535b39337_q
)
"# End node cbbacff6-44a6-484d-bef2-8985504141d3"
"# Start node 84e5fa41-3087-42c5-93d6-47c4b365df3d"
leqo_f06218d684815c308c414bfdfb9310a5_q0 = [leqo_reg[0]]
qc.h(leqo_f06218d684815c308c414bfdfb9310a5_q0)
leqo_f06218d684815c308c414bfdfb9310a5_q0_out = leqo_f06218d684815c308c414bfdfb9310a5_q0
"# End node 84e5fa41-3087-42c5-93d6-47c4b365df3d"
"# Start node ebc3e10b-bf5c-44b6-83b9-b6421304d1b1"
leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_pass_node_declaration_1 = [
    leqo_reg[2]
]
leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_pass_node_alias_1 = leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_pass_node_declaration_1
leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_pass_node_declaration_0 = (
    leqo_4013a70985a85ee38c83a7f535b39337_out
)
leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_pass_node_alias_0 = leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_pass_node_declaration_0
leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_if_reg = leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_pass_node_declaration_1
with qc.if_test(
    expr.equal(
        expr.cast(
            leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_pass_node_declaration_0,
            types.Uint(32),
        ),
        expr.cast(1, types.Uint(32)),
    )
):
    leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_b73a079d430552b195231072341ebdd9_q0 = [
        leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_if_reg[
            0
        ]
    ]
    qc.x(leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_b73a079d430552b195231072341ebdd9_q0)
    leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_b73a079d430552b195231072341ebdd9_q0_out = (
        leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_b73a079d430552b195231072341ebdd9_q0
    )
leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_f1b19fa0a092547a8a62d1a1579fdcb1_pass_node_declaration_1 = [
    leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_4732f268311359e784fb2f3dd6622ed1_if_reg[
        0
    ]
]
leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_f1b19fa0a092547a8a62d1a1579fdcb1_pass_node_alias_1 = leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_f1b19fa0a092547a8a62d1a1579fdcb1_pass_node_declaration_1
leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_f1b19fa0a092547a8a62d1a1579fdcb1_pass_node_declaration_0 = ClassicalRegister(
    1,
    "leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_f1b19fa0a092547a8a62d1a1579fdcb1_pass_node_declaration_0",
)
qc.add_register(
    leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_f1b19fa0a092547a8a62d1a1579fdcb1_pass_node_declaration_0
)
leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_f1b19fa0a092547a8a62d1a1579fdcb1_pass_node_alias_0 = leqo_789fcc26f77c5a019064200f09cc6d2d_leqo_f1b19fa0a092547a8a62d1a1579fdcb1_pass_node_declaration_0
"# End node ebc3e10b-bf5c-44b6-83b9-b6421304d1b1"
"# Start node 48425fbf-4576-47b3-a9c5-aca2276d9d22"
leqo_9d599b5830205ea29cd7c98b1274f967_q = [leqo_reg[0]]
leqo_9d599b5830205ea29cd7c98b1274f967_result = ClassicalRegister(
    1, "leqo_9d599b5830205ea29cd7c98b1274f967_result"
)
qc.add_register(leqo_9d599b5830205ea29cd7c98b1274f967_result)
qc.measure(
    leqo_9d599b5830205ea29cd7c98b1274f967_q[0],
    leqo_9d599b5830205ea29cd7c98b1274f967_result,
)
leqo_9d599b5830205ea29cd7c98b1274f967_out = leqo_9d599b5830205ea29cd7c98b1274f967_result
leqo_9d599b5830205ea29cd7c98b1274f967_qubit_out = (
    leqo_9d599b5830205ea29cd7c98b1274f967_q
)
"# End node 48425fbf-4576-47b3-a9c5-aca2276d9d22"
"# Start node 9162350e-8000-4e76-bf3d-0bdfffd397ca"
leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_pass_node_declaration_1 = [
    leqo_reg[2]
]
leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_pass_node_alias_1 = leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_pass_node_declaration_1
leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_pass_node_declaration_0 = (
    leqo_9d599b5830205ea29cd7c98b1274f967_out
)
leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_pass_node_alias_0 = leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_pass_node_declaration_0
leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_if_reg = leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_pass_node_declaration_1
with qc.if_test(
    expr.equal(
        expr.cast(
            leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_pass_node_declaration_0,
            types.Uint(32),
        ),
        expr.cast(1, types.Uint(32)),
    )
):
    leqo_0246af995a1a563289e38136d8ae68ef_leqo_02b1aa2e5e2855ecb3fcfd14b183efa0_q0 = [
        leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_if_reg[
            0
        ]
    ]
    qc.z(leqo_0246af995a1a563289e38136d8ae68ef_leqo_02b1aa2e5e2855ecb3fcfd14b183efa0_q0)
    leqo_0246af995a1a563289e38136d8ae68ef_leqo_02b1aa2e5e2855ecb3fcfd14b183efa0_q0_out = (
        leqo_0246af995a1a563289e38136d8ae68ef_leqo_02b1aa2e5e2855ecb3fcfd14b183efa0_q0
    )
leqo_0246af995a1a563289e38136d8ae68ef_leqo_24d56eae3b3d551394bcd40b1635df64_pass_node_declaration_1 = [
    leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_if_reg[
        0
    ]
]
leqo_0246af995a1a563289e38136d8ae68ef_leqo_24d56eae3b3d551394bcd40b1635df64_pass_node_alias_1 = leqo_0246af995a1a563289e38136d8ae68ef_leqo_24d56eae3b3d551394bcd40b1635df64_pass_node_declaration_1
leqo_0246af995a1a563289e38136d8ae68ef_leqo_24d56eae3b3d551394bcd40b1635df64_pass_node_declaration_0 = ClassicalRegister(
    1,
    "leqo_0246af995a1a563289e38136d8ae68ef_leqo_24d56eae3b3d551394bcd40b1635df64_pass_node_declaration_0",
)
qc.add_register(
    leqo_0246af995a1a563289e38136d8ae68ef_leqo_24d56eae3b3d551394bcd40b1635df64_pass_node_declaration_0
)
leqo_0246af995a1a563289e38136d8ae68ef_leqo_24d56eae3b3d551394bcd40b1635df64_pass_node_alias_0 = leqo_0246af995a1a563289e38136d8ae68ef_leqo_24d56eae3b3d551394bcd40b1635df64_pass_node_declaration_0
"# End node 9162350e-8000-4e76-bf3d-0bdfffd397ca"
"# Start node ab6a0b4c-b337-40d5-8993-55b8b4f6983d"
leqo_6e0809595ee3573884fb9527207aae7a_q0 = [leqo_reg[2]]
qc.ry(-2.0943951023931953, leqo_6e0809595ee3573884fb9527207aae7a_q0)
leqo_6e0809595ee3573884fb9527207aae7a_q0_out = leqo_6e0809595ee3573884fb9527207aae7a_q0
"# End node ab6a0b4c-b337-40d5-8993-55b8b4f6983d"
"# Start node 15632bc9-9dfa-45bf-afaa-e5818b7c2a97"
leqo_4d918e9145cf58e6bbf1732de2274afc_q = [leqo_reg[2]]
leqo_4d918e9145cf58e6bbf1732de2274afc_result = ClassicalRegister(
    1, "leqo_4d918e9145cf58e6bbf1732de2274afc_result"
)
qc.add_register(leqo_4d918e9145cf58e6bbf1732de2274afc_result)
qc.measure(
    leqo_4d918e9145cf58e6bbf1732de2274afc_q[0],
    leqo_4d918e9145cf58e6bbf1732de2274afc_result,
)
leqo_4d918e9145cf58e6bbf1732de2274afc_out = leqo_4d918e9145cf58e6bbf1732de2274afc_result
leqo_4d918e9145cf58e6bbf1732de2274afc_qubit_out = (
    leqo_4d918e9145cf58e6bbf1732de2274afc_q
)
"# End node 15632bc9-9dfa-45bf-afaa-e5818b7c2a97"
" --- EXECUTION ---"
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
print(compiled_circuit)
job = simulator.run(compiled_circuit, shots=500)
result_data = job.result()
counts = result_data.get_counts(qc)
print("Simulation Results (500 shots):", counts)
program_inputs = {
    0: leqo_4d918e9145cf58e6bbf1732de2274afc_q,
    1: leqo_0246af995a1a563289e38136d8ae68ef_leqo_2677ccfada9059e2a1c718dbab917c49_pass_node_declaration_1,
}
program_outputs = {
    0: leqo_4d918e9145cf58e6bbf1732de2274afc_out,
    1: leqo_4d918e9145cf58e6bbf1732de2274afc_qubit_out,
}
