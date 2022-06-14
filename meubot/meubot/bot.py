from botcity.core import DesktopBot
from turma1742 import *

class Bot(DesktopBot):
    def action(self, execution=None):

        self.execute(r'C:\Users\User\AppData\Local\WhatsApp\WhatsApp.exe')

        self.wait(2000)

        for item in alunos1742:
            
            if not self.find( "pesquisa", matching=0.97, waiting_time=10000):
                self.not_found("pesquisa")
            self.doubleClickRelative(89, 70)

            self.wait(500)
            self.paste(item)
            self.wait(1000)
            self.enter()

            self.wait(1000)

            self.paste("mostrando para o homi")
            self.enter()

            self.wait(2000)

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()






















