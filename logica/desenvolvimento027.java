import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);
        try
        {
            System.out.println("Em que ano você nasceu?");
            int nasc = ler.nextInt();
            System.out.println("Qual o ano atual?");
            int atual = ler.nextInt();

            if (nasc > atual){
            System.out.println("ERRO - O ano atual tem que ser maior que a idade de nascimento!");
        }
            else {
            System.out.println("Esse ano você tem ou fará " + (atual-nasc) + " anos.");
            }
        }
        
        catch (Exception erro)
        {
            System.out.println("ERRO - Valor digitado não é um número inteiro!");
        }
    }
}
