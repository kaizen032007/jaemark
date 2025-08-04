public class LogicalOperatorsExample {
    public static void main(String[] args) {
        // Logical AND (&&) - both conditions must be true
        boolean hasHighIncome = true;
        boolean hasGoodCredit = true;
        boolean isEligibleForLoan = hasHighIncome && hasGoodCredit;
        System.out.println("Loan eligible: " + isEligibleForLoan); // true

        // Logical OR (||) - at least one condition must be true
        boolean hasSavings = false;
        boolean hasInvestment = true;
        boolean canRetire = hasSavings || hasInvestment;
        System.out.println("Can retire: " + canRetire); // true

        // Logical NOT (!) - inverts the boolean value
        boolean isRaining = true;
        System.out.println("Is it NOT raining? " + !isRaining); // false

        // Combining operators
        int age = 25;
        boolean isStudent = true;
        boolean getsDiscount = (age < 18 || age >= 65) || isStudent;
        System.out.println("Gets discount: " + getsDiscount); // true

        // Short-circuit evaluation example
        int x = 10;
        int y = 20;
        boolean result = (x > 5) || (y++ > 15); // y++ won't execute
        System.out.println("Result: " + result + ", y: " + y); // true, 20
    }
}