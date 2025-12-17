from casino import Casino
from models.player import Player
from models.goose import WarGoose, HonkGoose



def run_simulation(steps: int=20, seed: int=1, print_logs: bool=True, print_final: bool=True) -> list[str]:
    casino = Casino(seed=seed)
    
    casino.register_player(Player(name="Толян", balance=100))
    casino.register_player(Player(name="Сергей", balance=150))
    casino.register_player(Player(name="Игнат", balance=200))
    
    casino.register_goose(WarGoose(name="Бомбомбини Гусини", honk_volume=30))
    casino.register_goose(HonkGoose(name="Гусоид", honk_volume=10))
    
    logs: list[str] = []
    
    events = [
        casino.event_bet,
        casino.event_win,
        casino.event_lose,
        casino.event_wargoose_attack,
        casino.event_honkgoose_scream
    ]
    
    for step in range(steps):
        event = casino.rng.choice(events)
        try:
            log = event()
        except ValueError as e:
            log = f"EVENT ERROR: {e}"
        logs.append(f"Step {step + 1}: {log}")

    for player in casino.players:
        logs.append(f"FINAL: {player.name}: {player.balance}")
    
    step_logs = logs[:steps]
    final_logs = logs[steps:]

    if print_logs:
        for log in step_logs:
            print(log)

    if print_final:
        for log in final_logs:
            print(log)
    
    return logs