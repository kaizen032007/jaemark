import java.util.Scanner;

public class calculator {
    public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);
    
    System.out.println("=".repeat(35));
    System.out.println("Hello Welcome to Simple Calculator!");
    System.out.println("=".repeat(35));

    System.out.print("Please Enter the first Number: ");
    int number1 = scanner.nextInt();
    scanner.nextLine();

    System.out.print("Please Enter the Second Number: ");
    int number2 = scanner.nextInt();
    scanner.nextLine();
    
    System.out.print("Please Enter the Operations you want to use: ");
    String operation = scanner.nextLine();
    
    calculate(number1, number2, operation);

    }

   public static void calculate(int number1, int number2, String operation) {
        if (operation.equals("+")) {
            System.out.println("The result is " + (number1 + number2));
        } else if (operation.equals("x")) {
            System.out.println("The result is " + (number1 * number2));
        } else if (operation.equals("/")) {
            System.out.println("The result is " + (number1 / number2));
        } else if (operation.equals("-")) {
            System.out.println("The result is " + (number1 - number2));
        } else {
            System.out.println("System Error");
        }
   } 
}
