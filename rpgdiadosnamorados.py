import tkinter as tk
import turtle
from tkinter import PhotoImage

def iniciar_janela():
    root = tk.Tk()
    root.title('Dia dos Namorados à Distância')
    root.geometry('800x600')
    root.configure(background='#ffc8dd')
    criar_botao_coracao(root, exibir_coracao)
    return root

def introducao():
    limpar_janela()
    texto = "Oii! Você está prestes a embarcar em um dia especial cheio de amor e surpresas, mesmo à distância. Vamos começar!"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    botao_proximo = tk.Button(root, text='Começar', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=escolha_inicial)
    botao_proximo.pack(pady=20)

def criar_botao_coracao(master, command):
    img_coracao = PhotoImage(file="coracao.png")
    botao_coracao = tk.Button(master, image=img_coracao, command=command, bg='#ffc8dd', bd=0)
    botao_coracao.image = img_coracao
    botao_coracao.pack(pady=20)

def escolha_inicial():
    limpar_janela()
    texto = "Você acorda e vê uma mensagem do seu amor desejando um Feliz Dia dos Namorados! Você tem duas opções para começar o dia:"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    botao_1 = tk.Button(root, text='Preparar um café da manhã especial juntos em videochamada.', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=cafe_da_manha_virtual)
    botao_1.pack(pady=10)
    botao_2 = tk.Button(root, text='Enviar uma mensagem romântica.', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=mensagem_romantica)
    botao_2.pack(pady=10)

def cafe_da_manha_virtual():
    limpar_janela()
    texto = "Você decide preparar um café da manhã especial na videochamada. O que você vai preparar?"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    botao_1 = tk.Button(root, text='Algo simples para ter mais tempo para admirar meu bem', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=panquecas)
    botao_1.pack(pady=10)
    botao_2 = tk.Button(root, text='Caprichar para eu mostrar que eu aprendi muito com masterchef', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=torradas)
    botao_2.pack(pady=10)

def mensagem_romantica():
    limpar_janela()
    texto = "Você decide enviar uma mensagem romântica de bom dia antes da videochamada. O que você vai escrever?"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    botao_1 = tk.Button(root, text='Um poema de amor.', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=poema)
    botao_1.pack(pady=10)
    botao_2 = tk.Button(root, text='Uma mensagem curta e doce.', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=mensagem_curta)
    botao_2.pack(pady=10)

def panquecas():
    limpar_janela()
    texto = "Você preparou café da manhã simples, com seu amor via videochamada!"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    surpresa_na_chamada()

def torradas():
    limpar_janela()
    texto = "Você preparou um digno café da manhã, com seu amor via videochamada!"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    surpresa_na_chamada()

def poema():
    limpar_janela()
    texto = """Nosso amor é como uma flor a desabrochar,
                Crescendo forte, sem nunca parar.
                Seus olhos brilham como estrelas no céu,
                Num universo de sonhos onde só existe o mel.

                Seus sorrisos são notas de uma doce canção,
                Que embalam meu coração com pura emoção.                Nossas mãos se entrelaçam, formando um laço,
                Numa dança eterna de carinho e abraço.
   
                Juntos enfrentamos tempestades e vendavais,
                Mas nunca deixamos que abalem nossos ideais.
                Pois o nosso amor é forte e verdadeiro,
                Um elo que nos une, um laço derradeiro.

                Assim, neste Dia dos Namorados, meu bem,
                Quero dizer que você é meu maior alguém.
                Que nossa história de amor seja sempre celebrada,
                Porque ao seu lado, minha vida é uma jornada encantada."""
    
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)

    botao_proximo = tk.Button(root, text='Próximo', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=cafe_da_manha_virtual)
    botao_proximo.pack(pady=20)

def mensagem_curta():
    limpar_janela()
    texto = "Apesar dos desafios que enfrentamos, cada momento ao seu lado é um lembrete do quanto sou abençoada(o) por ter você na minha vida. Seu amor ilumina até os dias mais sombrios e transforma os momentos simples em memórias preciosas. Você é o meu porto seguro, minha fonte de alegria e inspiração. Em cada batida do meu coração, encontro a certeza de que, com você, estou exatamente onde pertenço. Feliz Dia dos Namorados, meu amor!."
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)

    botao_proximo = tk.Button(root, text='Próximo', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=cafe_da_manha_virtual)
    botao_proximo.pack(pady=20)

def surpresa_na_chamada():
    limpar_janela()
    texto = "Durante a videochamada, você decide fazer uma surpresa. O que você vai fazer?"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    botao_1 = tk.Button(root, text='Cantar uma música especial.', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=cantar_musica)
    botao_1.pack(pady=10)
    botao_2 = tk.Button(root, text='Mostrar um presente virtual que você criou.',bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=presente_virtual)
    botao_2.pack(pady=10)
    botao_3 = tk.Button(root, text='Sugerir jogar um game juntos.', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=escolher_game)
    botao_3.pack(pady=10)

def cantar_musica():
    limpar_janela()
    texto = """And that's why night after night
               I'll be fuckin' you right
               Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday (a week)
               Monday, Tuesday, Wednesday, Thursday, Friday, seven days a week
               Every hour, every minute, every second, you know night after night
               I'll be fuckin' you right seven days a week!"""
    
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)

    botao_proximo = tk.Button(root, text='Próximo', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=final_feliz)
    botao_proximo.pack(pady=20)

def presente_virtual():
    limpar_janela()
    texto =""" ◌                             ◌                                       ◌           
                                            ‧₊ *:･ﾟ彡       ◌                 ☽︎       ◌
            ◌                                 ✩彡 ･ﾟ *:                                     
                                ◌                                        ◌
◌
                                                 ♡
                                        (\_(\       /)_/)
                                       (      )    (      )
                                     ૮/ʚɞ  |ა      ૮|  ʚɞ\ა
                                      ( ◌    |      |     ◌ )"""
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    final_feliz()

def escolher_game():
    limpar_janela()
    texto = "Vocês decidem jogar um game juntos. Qual jogo vocês vão escolher?"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    botao_1 = tk.Button(root, text='Fortnite.',bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=jogo_fortnite)
    botao_1.pack(pady=10)
    botao_2 = tk.Button(root, text='Valorant', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=jogo_valorant)
    botao_2.pack(pady=10)
    botao_3 = tk.Button(root, text='Dead by Daylight', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=jogo_dead_by_daylight)
    botao_3.pack(pady=10)

def jogo_fortnite():
    limpar_janela()
    texto = "Vocês entram no Fortnite e lutam juntos até o final, mostrando um ao outro suas habilidades incríveis e dançam na cara dos inimigos."
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    botao_proximo = tk.Button(root, text='Próximo', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=final_feliz)
    botao_proximo.pack(pady=20)

def jogo_valorant():
    limpar_janela()
    texto = "Vocês jogam Valorant, coordenando estratégias e vencendo partidas juntos como uma dupla imbatível."
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    botao_proximo = tk.Button(root, text='Próximo', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=final_feliz)
    botao_proximo.pack(pady=20)

def jogo_dead_by_daylight():
    limpar_janela()
    texto = "Vocês jogam Dead by Daylight, trabalhando juntos para sobreviver e escapar dos perigos!"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    botao_proximo = tk.Button(root, text='Próximo', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=final_feliz)
    botao_proximo.pack(pady=20)

def final_feliz():
    texto = "Mesmo enfrentando alguns 'game overs', vocês percebem que o amor de vocês é como um jogo infinito, onde cada 'game over' é apenas uma oportunidade para começar de novo, juntos. Juntos, vocês descobrem que o verdadeiro desafio é sempre continuar jogando, não importa o que aconteça. Feliz Dia dos Namorados!"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'), wraplength=700)
    label.pack(pady=20)
    
    botao_voltar = tk.Button(root, text='Voltar ao Início', bg='#ffc8dd', fg='#590d22', font=('Montserrat', 12, 'bold'), command=lambda: [introducao(), exibir_forma_e_texto()])
    botao_voltar.pack(pady=20)

def exibir_forma_e_texto():
    t = turtle.Turtle()
    s = turtle.Turtle()

    t.hideturtle()
    t.penup()
    t.goto(0, -10)
    t.pendown()

    t.pensize(3)
    t.color("#ffc8dd")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(178)
    t.end_fill()

    t.penup()
    t.goto(-130, 130)
    t.pendown()
    t.color('#590d22') 
    texto = "Te amo <3"
    tamanho_fonte = 25
    largura_texto = len(texto) * tamanho_fonte / 2
    t.penup()
    t.goto(-largura_texto, 130)
    t.pendown()
    
    t.color('#590d22') 
    t.write(texto, font=("Arial", tamanho_fonte, "bold"))  

    turtle.done()
 

    turtle.done()

def limpar_janela():
    for widget in root.winfo_children():
        widget.destroy()

def exibir_coracao():
    limpar_janela()
    texto = "Feliz Dia dos Namorados!"
    label = tk.Label(root, text=texto, bg='#ffc8dd', fg='#590d22', font=('Montserrat', 16, 'bold'))
    label.pack(pady=20)
    exibir_forma_e_texto()

root = iniciar_janela()
introducao()
root.mainloop()
