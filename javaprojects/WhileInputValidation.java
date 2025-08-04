import java.util.Scanner;

public class WhileInputValidation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number;

        System.out.print("Enter a number between 1 and 10: ");
        number = scanner.nextInt();

        // Keep asking until a valid number is entered
        while (number < 1 || number > 10) {
            System.out.print("Invalid! Enter again (1-10): ");
            number = scanner.nextInt();
        }

        System.out.println("You entered: " + number);
        scanner.close();
    }
}