class Goose:
    def __init__(self, name: str, honk_volume: int) -> None:
        if not isinstance(name, str) or not name:
            self.name = "goose"
        else:
            self.name = name
        self.honk_volume = max(1, int(honk_volume))  # крик должен быть >=1

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, honk_volume={self.honk_volume})'



class WarGoose(Goose):
    def attack(self) -> int:
        return self.honk_volume
    

class HonkGoose(Goose):
    def __call__(self) -> int:
        # "Honk! " * self.honk_volume не делаем так, так как крик должен влиять на баланс игрока
        return self.honk_volume







# goo = Goose("Goose", 5)
# wargoo = WarGoose("Goose the War Goose", 10)

# print(goo)
# print(wargoo)