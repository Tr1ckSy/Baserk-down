import json
import yt_dlp 
import os

NEGRITO = "\033[1m"
RESET = "\033[0m"
VERDE = "\033[90m"
RED = "\033[93m" 


def audio():
        URLS = input (f"{RED}   AUDIO LINK: {RESET}")
        ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
        }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
             error_code = ydl.download(URLS)

def video():



    URLS = input (f"{RED}   VIDEO LINK: {RESET}")

    class MyLogger:
        def debug(self, msg):
            # For compatibility with youtube-dl, both debug and info are passed into debug
            # You can distinguish them by the prefix '[debug] '
            if msg.startswith('[debug] '):
                pass
            else:
                self.info(msg)

        def info(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)


    # ℹ️ See "progress_hooks" in help(yt_dlp.YoutubeDL)
    def my_hook(d):
        if d['status'] == 'finished':
            print(f"""{VERDE} Done downloading, now post-processing ...{RESET}""")


    ydl_opts = {
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)



def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

def figlet():
        print(f'''{VERDE}{NEGRITO} 


                 ▄▄▄▄   ▓█████   ██████ ▓█████  ██▀███   ██ ▄█▀
                ▓█████▄ ▓█   ▀ ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒ ██▄█▒ 
                ▒██▒ ▄██▒███   ░ ▓██▄   ▒███   ▓██ ░▄█ ▒▓███▄░ 
                ▒██░█▀  ▒▓█  ▄   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▓██ █▄ 
                ░▓█  ▀█▓░▒████▒▒██████▒▒░▒████▒░██▓ ▒██▒▒██▒ █▄
                ░▒▓███▀▒░░ ▒░ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒
                ▒░▒   ░  ░ ░  ░░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░░ ░▒ ▒░
                 ░    ░    ░   ░  ░  ░     ░     ░░   ░ ░ ░░ ░ 
                 ░         ░  ░      ░     ░  ░   ░     ░  ░   
                      ░                                        
                      ▓█████▄  ▒█████   █     █░███▄    █ 
                      ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ 
                      ░██   █▌▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒
                      ░▓█▄   ▌▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒
                      ░▒████▓ ░ ████▓▒░░░██▒██▓▒██░   ▓██░
                       ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ 
                       ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░
                       ░ ░  ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░ 
                         ░        ░ ░      ░            ░ 
                       ░                                  



{RESET}''')

while True:	
    limpar_tela()
    figlet()
    print(f'{VERDE}{NEGRITO}   [1] DOWNLOAD VIDEO WEBM {RESET}')
    print(f'{VERDE}{NEGRITO}   [2] DOWNLOAD AUDIO M4A {RESET}')
    opcao1 = input("   |-ESCOLHA UMA OPÇÂO: ")
    if opcao1 == '1':
       limpar_tela()
       figlet()
       video()

    elif opcao1 == '2':
       limpar_tela()
       figlet()
       audio()