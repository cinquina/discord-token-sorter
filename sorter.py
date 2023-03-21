import os
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def main_menu():
    os.system("cls")
    console.print("""
                  
                  
[#c06ddb]     █████  ███                                          █████    █████       ███  ████  ████                    
[#b769d8]    ░░███  ░░░                                          ░░███    ░░███       ░░░  ░░███ ░░███                    
[#af65d4]  ███████  ████   █████   ██████   ██████  ████████   ███████     ░███ █████ ████  ░███  ░███   ██████  ████████ 
[#a661d1] ███░░███ ░░███  ███░░   ███░░███ ███░░███░░███░░███ ███░░███     ░███░░███ ░░███  ░███  ░███  ███░░███░░███░░███
[#9d5ece]░███ ░███  ░███ ░░█████ ░███ ░░░ ░███ ░███ ░███ ░░░ ░███ ░███     ░██████░   ░███  ░███  ░███ ░███████  ░███ ░░░ 
[#945aca]░███ ░███  ░███  ░░░░███░███  ███░███ ░███ ░███     ░███ ░███     ░███░░███  ░███  ░███  ░███ ░███░░░   ░███     
[#8b57c7]░░████████ █████ ██████ ░░██████ ░░██████  █████    ░░████████    ████ █████ █████ █████ █████░░██████  █████    
[#8253c3] ░░░░░░░░ ░░░░░ ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░      ░░░░░░░░    ░░░░ ░░░░░ ░░░░░ ░░░░░ ░░░░░  ░░░░░░  ░░░░░     
                                                                                                                                                                                                                                                                                           
                  """)
    console.print("discord.gg/yDV3JSqYVx | sorter!\n\n")
    OLD_TOKENS = []
    # load tokens
    tokensDirectory = Prompt.ask("[#9d5ece][?] [white]whats the [#9d5ece]token's text file[white] directory?")
    for token in open(tokensDirectory, 'r'):
        OLD_TOKENS.append(token.strip('\n'))
    console.print(f'[green][+][white] cached [#9d5ece]x{len(OLD_TOKENS)}[white] tokens successfully.\n\n')
    table = Table(title="format ids table")

    table.add_column("format", justify="right", style="#9d5ece", no_wrap=True)
    table.add_column("id", justify="right", style="#9d5ece")

    table.add_row("1", "token:mail:password")
    table.add_row("2", "mail:password:token")
    table.add_row("3", "token | mail: | password:..")
    table.add_row("custom", "custom formatting")
    console.print(table)
    tokensDirectory = Prompt.ask("[#9d5ece][?] [white]whats the [#9d5ece]token's text file[white] format id?", choices=["1", "2", "3", "custom"])
    fileAccess = open("sorted.txt", "a+")
    match tokensDirectory:
        case "1":
            for token in OLD_TOKENS:
                fileAccess.write(token.split(':')[0]+"\n")
        case "2":
            for token in OLD_TOKENS:
                fileAccess.write(token.split(':')[2]+"\n")
        case "3":
            for token in OLD_TOKENS:
                fileAccess.write(token.split(' | ')[0]+"\n")
        case "custom":
            separator = Prompt.ask("[#9d5ece][?] [white]whats the [#9d5ece]token's [white] separator? [#9d5ece](ex: |, :, ecc.)")
            position = Prompt.ask("[#9d5ece][?] [white]whats the [#9d5ece]token's [white] position? [#9d5ece](ex: email:token:password token's pos. would be 2)")
            for token in OLD_TOKENS:
                print(token.split(separator))
                fileAccess.write(token.split(separator)[int(position)-1]+"\n")

    console.print(f'[green][+][white] done.')
            
if __name__ == "__main__":
    main_menu()