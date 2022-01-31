#Libraries

from logic.bot_manager import BotManager

#Main

bot_manager = BotManager()

bot_manager.start_cycle(quit_keyword='q')