package POO;
import javax.swing.*;

public class Form1 {

    public static void main(String[] args) {

        //Configuration the window
        JFrame ventana = new JFrame();
        ventana.setTitle("Formulario");
        ventana.setBounds(0, 0, 650, 550);
        ventana.setResizable(false);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setLayout(null);

        //Creacion y configuración de Label para información estatica
        JLabel name = new JLabel("Nombre:");
        name.setBounds(10, 50, 100, 30);

        //Creación de InputBox para recopliación de datos
        JTextField entryName = new JTextField();
        entryName.setBounds(70, 55, 150, 20);

        JLabel title = new JLabel("Formulario de Registro");
        title.setBounds(10, 10, 200, 30);

        
        JLabel lastName = new JLabel("Apellido:");
        lastName.setBounds(10, 80, 100, 30);

        JTextField entryLastName = new JTextField();
        entryLastName.setBounds(70, 85, 150, 20);

        JLabel age = new JLabel("Edad:");
        age.setBounds(10, 110, 100, 30);

        JTextField entryAge = new JTextField();
        entryAge.setBounds(70, 115, 150, 20);

        JLabel genre = new JLabel("Genero:");
        genre.setBounds(10, 140, 100, 30);

        JTextField entryGenre = new JTextField();
        entryGenre.setBounds(70, 145, 150, 20);

        //Creamos un boton para enviar los datos
        JButton button = new JButton("Aceptar");
        button.setBounds(10, 450, 100, 30);

        JButton exitButton = new JButton("Salir");
        exitButton.setBounds(120, 450, 100, 30);


        //Agregamos los objetos creadoa a la ventana
        ventana.add(title);
        ventana.add(name);
        ventana.add(lastName);
        ventana.add(age);
        ventana.add(genre);

        ventana.add(entryName);
        ventana.add(entryLastName);
        ventana.add(entryAge);
        ventana.add(entryGenre);

        ventana.add(button);
        ventana.add(exitButton);

        //Mostramos la ventana
        ventana.setVisible(true);
    }


}
