import java.util.Scanner;

public class Java {
    public static void main(String[] args) {
        // ask for the number
        Scanner input = new Scanner(System.in);
        System.out.print("Number: ");
        long n = input.nextLong();

        // close the scanner
        input.close();

        String type = getType(n);
        if (type.equals("INVALID")) {
            System.out.println("INVALID");
        } else {
            if (isValid(n, type)) {
                System.out.println(type);
            } else {
                System.out.println("INVALID");
            }
        }
    }

    // check the validity
    public static boolean isValid(long n, String type) {
        if (type.equals("VISA") && (Long.toString(n).length() == 13 || Long.toString(n).length() == 16)) {
            return true;
        } else if (type.equals("AMEX") && Long.toString(n).length() == 15) {
            return true;
        } else if (type.equals("MASTERCARD") && Long.toString(n).length() == 16) {
            return true;
        } else {
            return false;
        }
    }

    // get what type of card
    public static String getType(long n) {
        // visa
        if (Long.toString(n).charAt(0) == '4' && checksum(n)) {
            return "VISA";
        }
        // amex
        else if ((Long.toString(n).substring(0, 2).equals("34") || Long.toString(n).substring(0, 2).equals("37"))
                && checksum(n)) {
            return "AMEX";
        }
        // mastercard
        else if (Long.parseLong(Long.toString(n).substring(0, 2)) >= 51
                && Long.parseLong(Long.toString(n).substring(0, 2)) <= 55 && checksum(n)) {
            return "MASTERCARD";
        } else {
            return "INVALID";
        }
    }

    // luhn's algorithm
    public static boolean checksum(long n) {
        // multiply every other digit by 2, starting with the number’s second-to-last
        // digit,
        // and then add those products’ digits together.
        int sum = 0;
        for (int i = Long.toString(n).length() - 2; i >= 0; i -= 2) {
            int digit = Integer.parseInt(Character.toString(Long.toString(n).charAt(i)));
            int product = digit * 2;
            sum += product % 10;
            sum += product / 10;
        }
        // add the sum to the sum of the digits that weren’t multiplied by 2.
        for (int i = Long.toString(n).length() - 1; i >= 0; i -= 2) {
            sum += Integer.parseInt(Character.toString(Long.toString(n).charAt(i)));
        }
        // if the total’s last digit is 0(or, put more formally, if the total modulo 10
        // is congruent to 0),
        // the number is valid!
        if (sum % 10 == 0) {
            return true;
        } else {
            return false;
        }
    }
}