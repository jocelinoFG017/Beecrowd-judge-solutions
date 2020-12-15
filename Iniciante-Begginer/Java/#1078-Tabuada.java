import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner ler = new Scanner(System.in);
    int i,N;
    N = ler.nextInt();
    for (i=1; i<=10;i++){

        System.out.println(i + " x " + N + " = \n" + (i*N));
    }
   }
}
