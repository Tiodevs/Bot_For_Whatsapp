from botcity.core import DesktopBot
import random
from turma1742 import *
from turma1743 import *
from turma1735 import *
from turma1733 import *

mensagemteste = "testando"
teste = ['opa', 'opa']

class Bot(DesktopBot):
    def action(self, execution=None):
        self.execute(r'C:\Users\Aluno\AppData\Local\WhatsApp\WhatsApp.exe')
        self.wait(1000)  # Espera 3 segundos

        for contato in teste:
            # Cria um valor aleatorio para o click
            cordenada = random.randrange(66, 82)
            
            # clica no campo de pesquisa
            if not self.find( "pesquisar", matching=0.97, waiting_time=10000):
                self.not_found("pesquisar")
            self.click_relative(92, cordenada)

            # gera um numero aleatorio para esperar entre 500 ms e 1500 ms
            a = random.randrange(500, 1500)
            self.wait(a)

            # cola o numero do aluno
            self.paste(contato)

            # gera um numero aleatorio para esperar entre 1500 ms e 2000 ms
            b = random.randrange(1500, 2000)
            self.wait(b)

            # aperta enter para entrar na conversa
            self.enter()
            self.wait(1000)

            # escreve a mensagem armazenada na variavel
            self.paste(mensagemteste)

            # aperta enter para enviar a mensagem
            self.enter()

            # gera um numero aleatorio para esperantes de mandar para outro contato entre 1500 ms e 3500 ms
            x = random.randrange(1500, 3500)
            self.wait(x)

            print(contato)

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
