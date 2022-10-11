import random
import turtle

#Informações para o jogo
velocidade = 3
velocidadeMaca = 2
velocidadeAnimacao = 6
pontos = 0
energia = 0
movimento = True

#Cenario do jogo
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
#janela.addshape('Vida0%.gif')
#janela.addshape('Vida5%.gif')
#janela.addshape('Vida20%.gif')
#janela.addshape('Vida50%.gif')
#janela.addshape('Vida75%.gif')
janela.addshape('Vida100%.gif')
janela.addshape('ExplosaoJogo.gif')

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
ogro.goto(0,300)

#Ogro Pequeno1
ogro2 = turtle.Turtle()
ogro2.shape('Ogro2.gif')
ogro2.penup()
ogro2.goto(100,300)

#Ogro Pequeno2
ogro3 = turtle.Turtle()
ogro3.shape('Ogro2.gif')
ogro3.penup()
ogro3.goto(-100,300)

#Combustível
comida = turtle.Turtle()
comida.shape('Comida.gif')
comida.penup()
comida.goto(200,200)

#Pontuacao
pontuacao = turtle.Turtle()
pontuacao.penup()
pontuacao.hideturtle()
pontuacao.goto(-260, 290)

# Configurações básicas do jogo
def iniciacaoJogo():
    global velocidade
    global velocidadeMaca
    global velocidadeAnimacao
    global pontos
    global energia
    velocidade = 3
    velocidadeMaca = 2
    velocidadeAnimacao = 6
    pontos = 0
    energia = 0

#Assim que ele encostar na borda ou nos inimigos, acontece a explosão
def explosaoPersonagem():
    explosao = turtle.Turtle()
    explosao.shape('ExplosaoJogo.gif')
    explosao.penup()
    explosao.goto(personagem.xcor()+130,personagem.ycor()+200)
    personagem.hideturtle()

#Aumento na pontuação do jogo
def aumentoPontuacao():
    global pontos
    pontos +=1
    pontuacao.clear()
    pontuacao.write(f'Pontuação: {pontos}', font=('Arial', 15, 'italic'))

#Funções de direções para o personagem
def esquerda():
    x = personagem.xcor()
    x -= 10
    personagem.setx(x)

def direita():
    x = personagem.xcor()
    x += 10
    personagem.setx(x)

#Controle de Movimento para o personagem
if movimento == True:
    turtle.onkeypress(direita, 'Right')
    turtle.onkeypress(esquerda, 'Left')
    turtle.listen()

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
        y = random.randint(350, 370)
        x = random.randint(-250, 0)
        ogro2.setpos(x, y)

def movimentoOgro3():
    ogro3.sety(ogro3.ycor() - velocidade)
    if ogro3.ycor() < -350:
        y = random.randint(400,410)
        x = random.randint(0, 250)
        ogro3.setpos(x, y)

def movimentoComida():
    comida.sety(comida.ycor() - velocidadeMaca)
    if comida.ycor() < -350:
        y = random.randint(950, 999)
        x = random.randint(-250, 240)
        comida.setposition(x, y)

#Colisao do personagem com a borda
def colisaoBorda():
    x = personagem.xcor()
    if x >= 250:
        personagem.setx(0)
        personagem.hideturtle()
        explosaoPersonagem()
        paradaJogo()
        movimento == False
    elif x <=-240:
       personagem.setx(0)
       personagem.hideturtle()
       explosaoPersonagem()
       paradaJogo()
       movimento == False
    else:
        pass

#Colisao do personagem com os ogros e sua energia
def colisaoPersonagens():
   #Calculo da colisão do personagem com o primeiro Ogro
   dx1 = ogro.xcor() - personagem.xcor()
   dy1 = ogro.ycor() - personagem.ycor()

   #Calculo da colisao do personagem com o segundo ogro
   dx2 = ogro2.xcor() - personagem.xcor()
   dy2 = ogro.ycor() - personagem.ycor()

   #Calculo da colisao do personagem com o terceiro ogro
   dx3 = ogro3.xcor() - personagem.xcor()
   dy3 = ogro3.ycor() - personagem.ycor()

   if dx1 <= 80 and dx1 >= -110 and dy1 <= 127 and dy1 >= -127:
       explosaoPersonagem()
       paradaJogo()
       movimento == False
   elif dx2 <= 47 and dx2 >= -90 and dy2 <= 60 and dy2 >= -60:
       explosaoPersonagem()
       paradaJogo()
       movimento == False
   elif dx3 <= 47 and dx3 >= -90 and dy3 <= 60 and dy3 >= -60:
       explosaoPersonagem()
       paradaJogo()
       movimento == False
   else:
       pass

#Adição de duas telas para que pareça que estão mexendo
def telaMexendo():
        cenario.sety(cenario.ycor() - velocidadeAnimacao)
        cenario2.sety(cenario2.ycor() - velocidadeAnimacao)
        if cenario.ycor() <= -647:
            cenario.sety(647)
        if cenario2.ycor() <= -647:
            cenario2.sety(647)

#Parar o jogo
def paradaJogo():
    global velocidade
    global velocidadeAnimacao
    global velocidadeMaca
    velocidade = 0
    velocidadeMaca = 0
    velocidadeAnimacao = 0

#Adição das vidas
def vidaCem():
    energia = turtle.Turtle()
    energia.shape('Vida100%.gif')
    energia.penup()
    energia.goto(220, 300)

def vidaSetentaCinco():
    energia = turtle.Turtle()
    energia.shape('Vida75%.gif')
    energia.penup()
    energia.goto(220, 300)

def vidaCinquenta():
    energia = turtle.Turtle()
    energia.shape('Vida50%.gif')
    energia.penup()
    energia.goto(220, 300)

def vidaVinte():
    energia = turtle.Turtle()
    energia.shape('Vida20%.gif')
    energia.penup()
    energia.goto(220, 300)

def vidaCinco():
    energia = turtle.Turtle()
    energia.shape('Vida5%.gif')
    energia.penup()
    energia.goto(220, 300)

def vida0():
    energia = turtle.Turtle()
    energia.shape('Vida0%.gif')
    energia.penup()
    energia.goto(220, 300)


def lacoCentral():
    colisaoBorda()
    movimentoOgro()
    movimentoOgro2()
    movimentoOgro3()
    movimentoComida()
    telaMexendo()
    colisaoPersonagens()
    aumentoPontuacao()
    #vidaCem()
    janela.update()
    janela.ontimer(lacoCentral, 1000//140)


lacoCentral()
janela.mainloop()




