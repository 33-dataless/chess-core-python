from src.game_state import GameState
from src.user  import ColorUser, User
from utils.clear_console import clear_console

def main() -> None:

    menu = input(
        "cless-cli\n"
        "< 1 > play chess\n"
        "< 2 > history game\n"
        "< 3 > profile\n"
    )

    match menu:
        case "1":
            color = input(
                "< 1 > play random color\n"
                "< 2 > play white color\n"
                "< 3 > play black color\n"
            )

            colors = {
                "1": ColorUser.RANDOM,
                "2": ColorUser.WHITE,
                "3": ColorUser.BLACK
            }

            user_color = colors.get(color, None)

            if not menu:
                print("wrong answer")
    # clear_console()
    game = GameState(
        color=user_color,
        mode=None
    )
    
    
 
if __name__ == "__main__":
    main()
    
