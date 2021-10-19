import forca;
import adivinhacao;


def escolha_jogo():
    print("********************************");
    print("********Escolha seu jogo********");
    print("********************************");

    print("(1) Forca (2) Adivinhação");

    jogo_escolhido = int(input("Digite o Jogo Escolhido (1) ou (2):"));

    if(jogo_escolhido == 1):
        print("Jogando FORCA");
        forca.jogar();
    else:
        print("Jogando Adivinhação");
        adivinhacao.jogar();

if(__name__ == "__main__"):
    escolha_jogo();