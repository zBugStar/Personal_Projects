import java.util.Random;

public class dados {

    public static void main(String[] args){
        Random rnd = new Random();
        boolean cont = true;
         System.out.println("Vamos a simular el lanzamiento de unos dados");



        do{
            System.out.println("-----------------------------");

         int dadoUno = rnd.nextInt(1,6);
         int dadoDos = rnd.nextInt(1,6);

        System.out.println("En el primer dado salio el numero "+ dadoUno);
        System.out.println("En el segundo dado salio el numero "+ dadoDos);
        int total=dadoDos+dadoUno;
        System.out.println("La suma de ambos dados es de "+ total);

        if(total == 7 || total == 11){
            cont = false;
        }
        elseif(total)
            System.out.println("-----------------------------");


        }while(cont);

    }
}
