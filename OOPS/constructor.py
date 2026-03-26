class game:
    def __init__(self,launcher,game_name):
        self.launcher=launcher
        self.game_name=game_name
g1=game("steam", "dying light2")
print(g1.launcher)
print(g1.game_name)

