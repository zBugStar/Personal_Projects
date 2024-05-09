package POO;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Form1 {


    public static void main(String[] args) {

        //Configuration the window
        JFrame window = new JFrame();
        window.setTitle("Registration Form");
        window.setBounds(0, 0, 350, 350);
        window.setResizable(false);
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setLayout(null);

        JLabel title = new JLabel("Registration Form");
        title.setBounds(10, 10, 200, 30);

        //Creacion y configuración de Label para información estatica
        JLabel name = new JLabel("Name:");
        name.setBounds(10, 50, 100, 30);

        //Creación de InputBox para recopliación de datos
        JTextField entryName = new JTextField();
        entryName.setBounds(70, 55, 150, 20);

        
        JLabel lastName = new JLabel("LastName:");
        lastName.setBounds(10, 80, 100, 30);

        JTextField entryLastName = new JTextField();
        entryLastName.setBounds(70, 85, 150, 20);

        JLabel age = new JLabel("Age:");
        age.setBounds(10, 110, 100, 30);

        JTextField entryAge = new JTextField();
        entryAge.setBounds(70, 115, 150, 20);

        JLabel genre = new JLabel("Genre:");
        genre.setBounds(10, 140, 100, 30);

        JTextField entryGenre = new JTextField();
        entryGenre.setBounds(70, 145, 150, 20);

        //Creamos un boton para enviar los datos
        JButton button = new JButton("Confirm");
        button.setBounds(10, 270, 100, 30);
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = entryName.getText();
                String lastName = entryLastName.getText();
                String age = entryAge.getText();
                String genre = entryGenre.getText();

                JOptionPane.showMessageDialog(null, "Name: " + name + "\nLastname: "
                        + lastName + "\nAge: " + age + "\nGenre: " + genre);
            }
        });

        JButton exitButton = new JButton("Exit");
        exitButton.setBounds(120, 270, 100, 30);
        exitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });


        //Agregamos los objetos creadoa a la window
        window.add(title);
        window.add(name);
        window.add(lastName);
        window.add(age);
        window.add(genre);

        window.add(entryName);
        window.add(entryLastName);
        window.add(entryAge);
        window.add(entryGenre);

        window.add(button);
        window.add(exitButton);

        //Mostramos la window
        window.setVisible(true);
    }


}
