import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class JavaGUI {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Card Validator");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(500, 300);

            JPanel mainPanel = new JPanel();
            mainPanel.setLayout(new BorderLayout(10, 10));
            mainPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

            JPanel inputPanel = new JPanel();
            inputPanel.setLayout(new GridLayout(0, 1));

            JLabel inputLabel = new JLabel("Enter Card Number:");
            inputLabel.setFont(new Font("Arial", Font.BOLD, 14));
            JTextField inputField = new JTextField(20);
            inputField.setFont(new Font("Arial", Font.PLAIN, 14));
            inputPanel.add(inputLabel);
            inputPanel.add(inputField);

            JTextArea resultArea = new JTextArea();
            resultArea.setEditable(false);
            resultArea.setFont(new Font("Arial", Font.BOLD, 18));
            resultArea.setLineWrap(true);
            resultArea.setWrapStyleWord(true);

            JScrollPane resultScrollPane = new JScrollPane(resultArea);
            resultScrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);

            JButton checkButton = new JButton("Check");
            checkButton.setFont(new Font("Arial", Font.BOLD, 14));
            checkButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    long n;
                    try {
                        n = Long.parseLong(inputField.getText().trim());
                    } catch (NumberFormatException ex) {
                        resultArea.setText("INVALID");
                        resultArea.setForeground(Color.RED);
                        return;
                    }

                    String type = getType(n);
                    if (type.equals("INVALID")) {
                        resultArea.setText("INVALID");
                        resultArea.setForeground(Color.RED);
                    } else {
                        if (isValid(n, type)) {
                            resultArea.setText(type);
                            resultArea.setForeground(Color.GREEN);
                        } else {
                            resultArea.setText("INVALID");
                            resultArea.setForeground(Color.RED);
                        }
                    }
                }
            });

            JButton resetButton = new JButton("Reset");
            resetButton.setFont(new Font("Arial", Font.BOLD, 14));
            resetButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    inputField.setText("");
                    resultArea.setText("");
                    resultArea.setForeground(Color.BLACK);
                }
            });

            JPanel buttonPanel = new JPanel();
            buttonPanel.setLayout(new GridLayout(1, 2, 10, 10));
            buttonPanel.add(checkButton);
            buttonPanel.add(resetButton);

            mainPanel.add(inputPanel, BorderLayout.NORTH);
            mainPanel.add(resultScrollPane, BorderLayout.CENTER);
            mainPanel.add(buttonPanel, BorderLayout.SOUTH);

            frame.add(mainPanel);
            frame.setVisible(true);
        });
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

    // Luhn's algorithm
    public static boolean checksum(long n) {
        // multiply every other digit by 2, starting with the number's second-to-last
        // digit,
        // and then add those products' digits together.
        int sum = 0;
        for (int i = Long.toString(n).length() - 2; i >= 0; i -= 2) {
            int digit = Integer.parseInt(Character.toString(Long.toString(n).charAt(i)));
            int product = digit * 2;
            sum += product % 10;
            sum += product / 10;
        }
        // add the sum to the sum of the digits that weren't multiplied by 2.
        for (int i = Long.toString(n).length() - 1; i >= 0; i -= 2) {
            sum += Integer.parseInt(Character.toString(Long.toString(n).charAt(i)));
        }
        // if the total's last digit is 0 (or, put more formally, if the total modulo 10
        // is congruent to 0),
        // the number is valid!
        if (sum % 10 == 0) {
            return true;
        } else {
            return false;
        }
    }
}