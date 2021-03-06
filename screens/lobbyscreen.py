from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.clock import mainthread


class LobbyScreen(Screen):
    @mainthread
    def set_this_players_nickname_and_elo(self):
        # This player hosted the match
        app = App.get_running_app()
        self.ids.player_one.text = app.player.nickname
        self.ids.player_one_elo.text = str(app.player.elo)

    @mainthread
    def back_to_lobby_browser(self):
        self.ids.player_two.text = " "
        self.ids.player_two_elo.text = " "
        self.ids.toolbar.title = "Waiting for opponent"
        self.ids.player_two_image.source = 'images/blankpiece.png'

        app = App.get_running_app()
        app.change_screen('lobby_browser_screen')
        message = {"command": "leave_lobby", 'is_host': app.client.is_host}
        app.client.send_message(message)

    @mainthread
    def clear_player_two_widgets(self):
        self.ids.player_two.text = " "
        self.ids.player_two_elo.text = " "
        self.ids.toolbar.title = "Waiting for opponent"
        self.ids.player_two_image.source = 'images/blankpiece.png'

    @mainthread
    def set_nicknames_and_elos(self, nick1, elo1, nick2, elo2):
        # Both players are in the match
        self.ids.player_one.text = nick1
        self.ids.player_one_elo.text = elo1
        self.ids.player_two.text = nick2
        self.ids.player_two_elo.text = elo2
        self.ids.player_two_image.source = 'images/kingpieceblack.png'
        self.ids.toolbar.title = "Ready to play!"

    def start_match(self, time_limit):
        # Send a message to the server that the game is started
        app = App.get_running_app()
        message = {"command": "start_match", "time_limit": time_limit}
        app.client.send_message(message)
        # When the game starts, it will send a message back to both players
        # which will change the screen to the game screen