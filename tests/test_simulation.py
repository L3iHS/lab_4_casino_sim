from src.simulation import run_simulation


def test_run_simulation_logs_and_final():
    steps = 5
    logs = run_simulation(
        steps=steps,
        seed=1,
        print_logs=False,
        print_final=False,
    )

    assert len(logs) == steps + 3  # 3 занимают финвльные логи
    assert logs[0].startswith("Step 1:")
    assert logs[steps].startswith("FINAL:")
    assert any("FINAL:" in line for line in logs)  # финальные вообще есть