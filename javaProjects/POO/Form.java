package POO;
import javax.swing.*;

public class Form extends JFrame{
    public Form(){
        setTitle("Formulario");
        setBounds(0, 0, 400, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(null);
        JLabel label = new JLabel("Nombre:");
        label.setBounds(10, 10, 100, 30);
        add(label);
        JTextField textField = new JTextField();
        textField.setBounds(120, 10, 150, 30);
        add(textField);
        JLabel label2 = new JLabel("Apellido:");
        label2.setBounds(10, 50, 100, 30);
        add(label2);
        JTextField textField2 = new JTextField();
        textField2.setBounds(120, 50, 150, 30);
        add(textField2);
        JButton button = new JButton("Aceptar");
        button.setBounds(10, 100, 100, 30);
        add(button);
    }
    public static void main(String[] args) {
        Form form = new Form();
        form.setVisible(true);
    }
}
