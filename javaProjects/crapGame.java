import java.util.Random;

public class crapGame {
    public static void main(String[] args) {
        Random random = new Random();
        int roll = rollDice(random);
        int point = 0;
        boolean gameOn = true;

        System.out.println("Welcome to the Craps Game!");

        if (roll == 7 || roll == 11) {
            System.out.println("You rolled " + roll + ". You win!");
            gameOn = false;
        } else if (roll == 2 || roll == 3 || roll == 12) {
            System.out.println("You rolled " + roll + ". You lose!");
            gameOn = false;
        } else {
            point = roll;
            System.out.println("You rolled " + roll + ". Point is set to " + point);
        }

        while (gameOn) {
            roll = rollDice(random);
            if (roll == point) {
                System.out.println("You rolled " + roll + ". You win!");
                gameOn = false;
            } else if (roll == 7) {
                System.out.println("You rolled " + roll + ". You lose!");
                gameOn = false;
            } else {
                System.out.println("You rolled " + roll + ". Roll again.");
            }
        }
    }

    private static int rollDice(Random random) {
        int die1 = random.nextInt(6) + 1;
        int die2 = random.nextInt(6) + 1;
        return die1 + die2;
    }
}