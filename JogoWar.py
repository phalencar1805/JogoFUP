#Author: Pedro Henrique Alencar Barbosa
import random
import turtle

#Informações para o jogo
velocidade = 0
velocidadeMaca = 0
velocidadeAnimacao = 0
pontos = 0
energia = 100
movimentoPersonagem = 0

#Configurações do cenario
janela = turtle.Screen()
janela.title('War')
janela.setup(width=700, height=650)
janela.tracer(0)
janela.addshape('CenarioJogo.gif')

#Adição do mesmo cenário para que dê a impressão de estar se mexendo
cenario = turtle.Turtle()
cenario.shape('CenarioJogo.gif')
cenario.penup()
cenario.goto(0, 0)

cenario2 = turtle.Turtle()
cenario2.shape('CenarioJogo.gif')
cenario2.penup()
cenario2.goto(0,647)

#Adicionando as imagens ao jogo
janela.addshape('PersonagemJogo.gif')
janela.addshape('Ogro.gif')
janela.addshape('Ogro2.gif')
janela.addshape('Comida.gif')
janela.addshape('ExplosaoJogo.gif')
janela.addshape('Vida0%.gif')
janela.addshape('Vida5%.gif')
janela.addshape('Vida20%.gif')
janela.addshape('Vida50%.gif')
janela.addshape('Vida75%.gif')
janela.addshape('Vida100%.gif')

#Personagem principal
personagem = turtle.Turtle()
personagem.shape('PersonagemJogo.gif')
personagem.penup()
personagem.goto(0, -265)

#Ogros
#Ogro Grande
ogro = turtle.Turtle()
ogro.shape('Ogro.gif')
ogro.penup()
ogro.goto(0,260)

#Ogro Pequeno1
ogro2 = turtle.Turtle()
ogro2.shape('Ogro2.gif')
ogro2.penup()
ogro2.goto(100,260)

#Ogro Pequeno2
ogro3 = turtle.Turtle()
ogro3.shape('Ogro2.gif')
ogro3.penup()
ogro3.goto(-100,260)

#Maçã que dará energia (combustível) para o personagem
comida = turtle.Turtle()
comida.shape('Comida.gif')
comida.penup()
comida.goto(200,200)

#Pontuacao
pontuacao = turtle.Turtle()
pontuacao.penup()
pontuacao.hideturtle()
pontuacao.goto(-260, 290)

#Combustivel
combustivel = turtle.Turtle()
combustivel.penup()
combustivel.hideturtle()
combustivel.goto(130,285)

#Explosao
explosao = turtle.Turtle()
explosao.shape('ExplosaoJogo.gif')
explosao.penup()
explosao.hideturtle()

#Vida = combustível
vida = turtle.Turtle()
vida.shape('Vida100%.gif')
vida.penup()
vida.goto(220, 300)

#Mensagem para iniciar o jogo
mensagem = turtle.Turtle()
mensagem.speed(0)
mensagem.hideturtle()
mensagem.write('Pressione espaço para iniciar o jogo', align='center', font=('Arial', 15, 'bold'))

#Assim que ele encostar na borda ou nos inimigos, acontece a explosão
def explosaoPersonagem():
    explosao.goto(personagem.xcor()+130,personagem.ycor()+200)
    personagem.hideturtle()
    explosao.showturtle()

#Escrita da pontuação do jogo
def escritaPontuacao():
    pontuacao.clear()
    pontuacao.write(f'Pontuação: {pontos}', font=('Arial', 15, 'italic'))

#Escrita do Combustível
def escritaCombustivel():
    combustivel.clear()
    combustivel.write(f'{energia}', font=('Arial',15,'italic'))

#Funções de direções para o personagem
def esquerda():
    x = personagem.xcor()
    x -= movimentoPersonagem
    personagem.setx(x)

def direita():
    x = personagem.xcor()
    x += movimentoPersonagem
    personagem.setx(x)

#Controle de Movimento para o personagem
turtle.onkeypress(direita, 'Right')
turtle.onkeypress(esquerda, 'Left')

#Movimento automático dos personagens
def movimentoOgro():
    ogro.sety(ogro.ycor() - velocidade)
    if ogro.ycor() < -360:
        y = random.randint(300,330)
        x = random.randint(-200,230)
        ogro.setpos(x,y)

def movimentoOgro2():
    ogro2.sety(ogro2.ycor() - velocidade)
    if ogro2.ycor() < -350:
        y = random.randint(360, 370)
        x = random.randint(-235, 0)
        ogro2.setpos(x, y)

def movimentoOgro3():
    ogro3.sety(ogro3.ycor() - velocidade)
    if ogro3.ycor() < -350:
        y = random.randint(400,410)
        x = random.randint(0, 235)
        ogro3.setpos(x, y)

def movimentoComida():
    comida.sety(comida.ycor() - velocidadeMaca)
    if comida.ycor() < -350:
        y = random.randint(980,1200)
        x = random.randint(-250, 240)
        comida.setposition(x, y)

def gotoOgros():
    ogro.goto(0, 260)
    ogro2.goto(100, 260)
    ogro3.goto(-100, 260)

#Colisao do personagem com a borda
def colisaoBorda():
    global pontos
    global energia
    x = personagem.xcor()
    if x >= 250:
        personagem.setx(0)
        personagem.hideturtle()
        explosaoPersonagem()
        mensagem.write('Você foi morto por peixes gigantes. Aperte espaço para recomeçar', align='center',
                       font=('Arial', 12, 'bold'))
        gotoOgros()
        comida.sety(random.randint(980, 1200))
        energia -= 5
        paradaJogo()
    elif x <= -220:
       personagem.setx(0)
       personagem.hideturtle()
       explosaoPersonagem()
       mensagem.write('Você foi morto por tubarões. Aperte espaço para recomeçar', align='center',
                      font=('Arial', 12, 'bold'))
       gotoOgros()
       comida.sety(random.randint(980, 1200))
       energia -= 5
       paradaJogo()
    else:
        pass

#Colisao do personagem com os ogros
def colisaoPersonagens():
   global pontos
   global energia
   #Calculo da colisão do personagem com o primeiro Ogro
   dx1 = ogro.xcor() - personagem.xcor()
   dy1 = ogro.ycor() - personagem.ycor()

   #Calculo da colisao do personagem com o segundo ogro
   dx2 = ogro2.xcor() - personagem.xcor()
   dy2 = ogro2.ycor() - personagem.ycor()

   #Calculo da colisao do personagem com o terceiro ogro
   dx3 = ogro3.xcor() - personagem.xcor()
   dy3 = ogro3.ycor() - personagem.ycor()

   if dx1 <= 80 and dx1 >= -110 and dy1 <= 127 and dy1 >= -127:
       explosaoPersonagem()
       mensagem.write('Você foi morto por um ogro gigante. Aperte espaço para recomeçar', align='center',
                      font=('Arial', 12, 'bold'))
       gotoOgros()
       comida.sety(random.randint(980,1200))
       energia -= 5
       paradaJogo()
   elif dx2 <= 47 and dx2 >= -90 and dy2 <= 60 and dy2 >= -70:
       explosaoPersonagem()
       mensagem.write('Você foi morto por um mini ogro. Aperte espaço para recomeçar', align='center',
                      font=('Arial', 12, 'bold'))
       gotoOgros()
       comida.sety(random.randint(980, 1200))
       energia -= 5
       paradaJogo()
   elif dx3 <= 47 and dx3 >= -90 and dy3 <= 60 and dy3 >= -70:
       explosaoPersonagem()
       mensagem.write('Você foi morto por um mini ogro. Aperte espaço para recomeçar', align='center',
                      font=('Arial', 12, 'bold'))
       gotoOgros()
       comida.sety(random.randint(980, 1200))
       energia -= 5
       paradaJogo()
   else:
       pass

#Colisão do personagem com a comida
def colisaoComida():
    global energia
    global pontos
    dx = comida.xcor() - personagem.xcor()
    dy = comida.ycor() - personagem.ycor()

    if dx <= 20 and dx >= -65 and dy <= 80:
       if energia == 100:
           energia += 0
           pontos += 100
           y = random.randint(950, 999)
           x = random.randint(-250, 240)
           comida.setposition(x, y)
       elif energia >= 95:
           energia += 5
           pontos += 100
           y = random.randint(950, 999)
           x = random.randint(-250, 240)
           comida.setposition(x, y)
       else:
        energia += 10
        pontos += 100
        y = random.randint(950, 999)
        x = random.randint(-250, 240)
        comida.setposition(x, y)

#Adição de duas telas para que pareça que estão mexendo
def telaMexendo():
    global pontos, energia, velocidade, reinicio
    cenario.sety(cenario.ycor() - velocidadeAnimacao)
    cenario2.sety(cenario2.ycor() - velocidadeAnimacao)
    if cenario.ycor() <= -647:
        cenario.sety(647)
    if cenario2.ycor() <= -647:
        cenario2.sety(647)
        pontos += 100
        energia -= 5
        velocidade += 0.5
        if energia == 100 or energia > 75:
            vida
            vida.goto(220, 300)
        elif energia == 75 or energia > 50:
            vida.shape('Vida75%.gif')

        elif energia == 50 or energia > 20:
            vida.shape('Vida50%.gif')

        elif energia == 20 or energia > 5:
            vida.shape('Vida20%.gif')

        elif energia == 5 or energia > 0:
            vida.shape('Vida5%.gif')

        elif energia <= 0:
            vida.shape('Vida0%.gif')
            mensagem.write(f'Sua energia acabou. Aperte R para reinicar ou S para sair\n                                   Pontuação final: {pontos}',
                           align='center', font=('Arial', 14, 'bold'))
            paradaJogo()
            janela.onkeypress(reinicarJogo, 'r')
            janela.onkeypress(sairJogo, 's')

        else:
            pass

#Parar o jogo
def paradaJogo():
    global velocidade, velocidadeAnimacao, velocidadeMaca, movimentoPersonagem
    velocidade = 0
    velocidadeMaca = 0
    velocidadeAnimacao = 0
    movimentoPersonagem = 0

#Laço principal do jogo
def lacoCentral():
    telaMexendo()
    colisaoBorda()
    colisaoPersonagens()
    colisaoComida()
    movimentoOgro()
    movimentoOgro2()
    movimentoOgro3()
    movimentoComida()
    escritaPontuacao()
    escritaCombustivel()
    janela.update()
    janela.ontimer(lacoCentral, 1000//75)

#Por aqui que o jogo começa a rodar
def iniciarJogo():
    global velocidade, velocidadeMaca, velocidadeAnimacao, movimentoPersonagem, mensagem, reinicio
    velocidade = 3
    velocidadeMaca = 2
    velocidadeAnimacao = 6
    movimentoPersonagem = 10
    explosao.hideturtle()
    personagem.showturtle()
    mensagem.clear()

janela.onkeypress(iniciarJogo, 'space')

#Por aqui que o jogo reinicia após o usuário chegar a 0 de energia
def reinicarJogo():
    iniciarJogo()
    global energia, pontos, comida
    energia = 100
    vida.shape('Vida100%.gif')
    pontos = 0
    gotoOgros()
    comida.goto(200, 200)
    mensagem.clear()

#Por aqui que o usuário tem a opção de sair do jogo
def sairJogo():
    janela.bye()

#Reconhecimento das teclas pressionadas pelo usuário
janela.listen()

#Chamo função principal
lacoCentral()

#Mantenho a janela aberta
janela.mainloop()