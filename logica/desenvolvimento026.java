import java.io.Serializable;
import java.io.IOException;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

class Pessoa implements Serializable
{
    public String nome;
    public int idade;

    public Pessoa(String nome, int idade)
    {
        this.nome = nome;
        this.idade = idade;
    }
}

public class Main {
    public static void main(String[] args)
    {
        Pessoa p = new Pessoa("Walter",31);

        try
        {
            FileOutputStream dados = new FileOutputStream("dados.ser");
            ObjectOutputStream out = new ObjectOutputStream(dados);

            out.writeObject(p);
            out.close();
            dados.close();

            System.out.println("O objeto foi serializado");
        }

        catch(IOException erro)
        {
            System.out.println("Erro");
        }

        Pessoa p1;

        try
        {
            FileInputStream dados = new FileInputStream("dados.ser");
            ObjectInputStream in = new ObjectInputStream(dados);

            p1 = (Pessoa)in.readObject();
            in.close();
            dados.close();

            System.out.println("O objeto foi desserializado");
            System.out.println(p1.nome);
            System.out.println(p1.idade);

        }

        catch(IOException erro)
        {
            System.out.println("Erro 1");
        }
        
        catch (ClassNotFoundException erro) 
        {
            System.out.println("Erro 2");
        }
        
    }
}
