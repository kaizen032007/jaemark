import java.util.Scanner;

public class index {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("ENTER THE OPERATOR: ");
        String operator = scanner.nextLine();

        System.out.print("ENTER THE FIRST NUMBER: ");
        int num1 = scanner.nextInt();

        System.out.print("ENTER THE SECOND NUMBER: ");
        int num2 = scanner.nextInt();

        switch(operator) {
            case "+" -> System.out.print(num1 + num2);
            case "-" -> System.out.print(num1 - num2);
            case "x" -> System.out.print(num1 * num2);
            case "/" -> System.out.print(num1 / num2);
            default -> System.out.print("INVALID OPERATOR");
        }
        scanner.close();
    }
}