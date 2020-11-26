
package com.mycompany.miniconsolavirtual;


public class Controlador extends javax.swing.JFrame {

   
    public Controlador() {
        initComponents();
    }

    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        BotonSuperior = new javax.swing.JLabel();
        BotonDerecho = new javax.swing.JLabel();
        BotonIzquierdo = new javax.swing.JLabel();
        BotonInferior = new javax.swing.JLabel();
        BotonA = new javax.swing.JLabel();
        BotonB = new javax.swing.JLabel();
        Fondo = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());
        getContentPane().add(BotonSuperior, new org.netbeans.lib.awtextra.AbsoluteConstraints(260, 250, 40, 40));
        getContentPane().add(BotonDerecho, new org.netbeans.lib.awtextra.AbsoluteConstraints(300, 290, 40, 40));
        getContentPane().add(BotonIzquierdo, new org.netbeans.lib.awtextra.AbsoluteConstraints(220, 290, 50, 40));
        getContentPane().add(BotonInferior, new org.netbeans.lib.awtextra.AbsoluteConstraints(260, 330, 40, 40));
        getContentPane().add(BotonA, new org.netbeans.lib.awtextra.AbsoluteConstraints(640, 300, 70, 70));
        getContentPane().add(BotonB, new org.netbeans.lib.awtextra.AbsoluteConstraints(560, 300, 70, 70));

        Fondo.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Imagenes/Controler.jpg"))); // NOI18N
        getContentPane().add(Fondo, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 990, -1));

        pack();
    }// </editor-fold>//GEN-END:initComponents

   

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel BotonA;
    private javax.swing.JLabel BotonB;
    private javax.swing.JLabel BotonDerecho;
    private javax.swing.JLabel BotonInferior;
    private javax.swing.JLabel BotonIzquierdo;
    private javax.swing.JLabel BotonSuperior;
    private javax.swing.JLabel Fondo;
    // End of variables declaration//GEN-END:variables
}
