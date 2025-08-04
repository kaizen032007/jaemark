import java.util.Scanner;
public class simplecalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("ENTER THE OPERATOR (* / + -): ");
        String operator  =  scanner.nextLine();

        System.out.print("ENTER THE FIRST NUMBER: ");
        int num1 = scanner.nextInt();

        System.out.print("ENTER THE SECOND NUMBER: ");
        int num2 = scanner.nextInt();

        if (operator.equals("+")) {
             System.out.print(num1 + num2);
        }
        else if (operator.equals("/")) {
            System.out.print(num1 / num2);
        }
        else if (operator.equals("*")) {
            System.out.print(num1 * num2);
        }
        else if (operator.equals("-")) {
            System.out.print(num1 - num2);
        }
        else {
            System.out.print("INVALID INPUT PLS TYPE THE CORRECT INPUT");
        }


    }
}
