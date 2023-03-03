import os
import rich
from rich.panel import Panel as Anak
from rich import print as Buat
from rich.tree import Tree
from rich import print as cetak
from rich.panel import Panel as nel
putih = '\x1b[1;97m'
def banner():
  os.system("clear")
  print(f"""{putih}
  ________  ____  ____    _______    _______   _______                 
 /"       )("  _||_ " |  |   __ "\  /"     "| /"      \                
(:   \___/ |   (  ) : |  (. |__) :)(: ______)|:        |               
 \___  \   (:  |  | . )  |:  ____/  \/    |  |_____/   )               
  __/  \\   \\ \__/ //   (|  /      // ___)_  //      /                
 /" \   :)  /\\ __ //\  /|__/ \    (:      "||:  __   \                
(_______/  (__________)(_______)    \_______)|__|  \___)               
             __   __  ___       __        _______    __      ______    
            |"  |/  \|  "|     /""\      /"      \  |" \    /    " \   
            |'  /    \:  |    /    \    |:        | ||  |  // ____  \  
            |: /'        |   /' /\  \   |_____/   ) |:  | /  /    ) :) 
             \//  /\'    |  //  __'  \   //      /  |.  |(: (____/ //  
             /   /  \\   | /   /  \\  \ |:  __   \  /\  |\\        /   
            |___/    \___|(___/    \___)|__|  \___)(__\_|_)\"_____/\n    """)
def menu():
  os.system("clear")
  banner()
  Meledak = Tree(nel.fit(f"""[bold white]Untuk Versi Sekarang Hanya Support Di Perangkat Yang aarch64 Untuk Mengecek Ketik Perintah Ini : uname -m Jika Muncul [bold green] aarch64[bold white] Selamat Engkau Bisa Menggunakan Script rembo Ini...[bold white]""",style=f"bold white"))
  Meledak.add(nel.fit(f"[bold white]Jalankan ulang python [bold green]run.py[bold white]",style="bold white"))
  cetak(Meledak)
if __name__=='__main__':
	menu()	
