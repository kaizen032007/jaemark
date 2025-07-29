import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CalculatorGUI {
    private JFrame frame;
    private JTextField display;
    private double firstNumber = 0;
    private String operation = "";
    private boolean startNewInput = true;

    public CalculatorGUI() {
        frame = new JFrame("Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 400);
        frame.setLayout(new BorderLayout());

        // Display
        display = new JTextField();
        display.setFont(new Font("Arial", Font.BOLD, 24));
        display.setHorizontalAlignment(JTextField.RIGHT);
        display.setEditable(false);
        frame.add(display, BorderLayout.NORTH);

        // Buttons Panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(5, 4, 5, 5));

        String[] buttons = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C", "⌫", "", ""
        };

        for (String text : buttons) {
            JButton button = createButton(text);
            buttonPanel.add(button);
        }

        frame.add(buttonPanel, BorderLayout.CENTER);
        frame.setVisible(true);
    }

    private JButton createButton(String text) {
        JButton button = new JButton(text);
        button.setFont(new Font("Arial", Font.BOLD, 18));
        button.setFocusPainted(false);
        
        // Color coding
        if (text.matches("[0-9.]")) {
            button.setBackground(new Color(240, 240, 240));
        } else if (text.equals("=")) {
            button.setBackground(new Color(76, 175, 80));
            button.setForeground(Color.WHITE);
        } else if (text.equals("C") || text.equals("⌫")) {
            button.setBackground(new Color(244, 67, 54));
            button.setForeground(Color.WHITE);
        } else {
            button.setBackground(new Color(33, 150, 243));
            button.setForeground(Color.WHITE);
        }

        button.addActionListener(new ButtonClickListener());
        return button;
    }

    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            String command = e.getActionCommand();
            
            if (command.matches("[0-9]")) {
                if (startNewInput) {
                    display.setText("");
                    startNewInput = false;
                }
                display.setText(display.getText() + command);
            }
            else if (command.equals(".")) {
                if (!display.getText().contains(".")) {
                    display.setText(display.getText() + ".");
                }
            }
            else if (command.equals("C")) {
                display.setText("0");
                firstNumber = 0;
                operation = "";
                startNewInput = true;
            }
            else if (command.equals("⌫")) {
                String current = display.getText();
                if (!current.isEmpty()) {
                    display.setText(current.substring(0, current.length() - 1));
                    if (display.getText().isEmpty()) {
                        display.setText("0");
                        startNewInput = true;
                    }
                }
            }
            else if (command.matches("[+\\-*/]")) {
                if (!operation.isEmpty()) calculate();
                firstNumber = Double.parseDouble(display.getText());
                operation = command;
                startNewInput = true;
            }
            else if (command.equals("=")) {
                if (!operation.isEmpty()) {
                    calculate();
                    operation = "";
                }
                startNewInput = true;
            }
        }

        private void calculate() {
            double secondNumber = Double.parseDouble(display.getText());
            switch (operation) {
                case "+":
                    firstNumber += secondNumber;
                    break;
                case "-":
                    firstNumber -= secondNumber;
                    break;
                case "*":
                    firstNumber *= secondNumber;
                    break;
                case "/":
                    if (secondNumber != 0) {
                        firstNumber /= secondNumber;
                    } else {
                        display.setText("Error");
                        return;
                    }
                    break;
            }
            display.setText(String.valueOf(firstNumber));
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new CalculatorGUI());
    }
}