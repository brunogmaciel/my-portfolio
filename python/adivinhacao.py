import random;

def jogar():
    print("********************************");
    print("Bem vindo ao jogo de adivinhação");
    print("********************************");

    numero_secreto = random.randrange(1, 101);
    total_de_tentativas = 0;

    print("Qual nível de dificiculdade?", "(1) Fácil (2) Médio (3) Difícil", sep="\n");
    nivel = int(input("Digite o nível desejado:"));

    if(nivel == 1):
        total_de_tentativas = 20;
    elif(nivel == 2): 
        total_de_tentativas = 10;
    else:
        total_de_tentativas = 5;

    pontos = 1000;
    for rodada_atual in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada_atual, total_de_tentativas));
        chute = int(input("Digite um número entre 1 e 100:"));
        
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!");
            continue;
    

        acertou = chute == numero_secreto;
        maior   = chute >  numero_secreto;
        menor   = chute <  numero_secreto;

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos));
            break;
        else:
            if(maior):
                print("Você errou! Seu chute foi muito alto");
            elif(menor):
                print("Você errou! Seu chute foi muito baixo");
        pontos_perdidos = abs(numero_secreto - chute);
        pontos = pontos - pontos_perdidos;

    print("Fim de Jogo");


if(__name__ == "__main__"):
    jogar();
