import java.util.Random;

public class dados {

    public static void main(String[] args){
        Random rnd = new Random();
        boolean continuar = true;
        int punto=0;
         System.out.println("Vamos a simular el lanzamiento de unos dados");



         System.out.println("En el primer dado salio el numero "+ lanzarDadoUno(rnd));
         System.out.println("En el segundo dado salio el numero "+ lanzarDadoDos(rnd));
         int total=sumaDados(lanzarDadoUno(rnd), lanzarDadoDos(rnd));
         System.out.println("La suma de ambos dados es de "+ total);

         if(total == 7 || total == 11){
                System.out.println("Ganaste en la primera tirada");

          }
         else if(total == 2 || total == 3 || total == 12){
             System.out.println("Perdiste ");
             System.out.println("-----------------------------");
         }
         else{
             punto = total;
             System.out.println("Sigues lanzando");
         }

         do{
             System.out.println("En el primer dado salio el numero "+ lanzarDadoUno(rnd));
             System.out.println("En el segundo dado salio el numero "+ lanzarDadoDos(rnd));
             total = sumaDados(lanzarDadoUno(rnd), lanzarDadoDos(rnd));
             System.out.println("La suma de ambos dados es de "+ total);

             if (total == punto) {
                 System.out.println( ". You win!");
                continuar = false;
            }
             else if (total == 7) {
                System.out.println( ". You lose!");
                continuar = false;
            }
             else {
                System.out.println(" Roll again.");
            }

         }while(!continuar);




    }

    public static int lanzarDadoUno(Random rnd){
        return rnd.nextInt(1,6);
    }
    public static int lanzarDadoDos(Random rnd){
        return rnd.nextInt(1,6);
    }
    public static int sumaDados(int dado1, int dado2){
        return dado1+dado2;
    }

}
