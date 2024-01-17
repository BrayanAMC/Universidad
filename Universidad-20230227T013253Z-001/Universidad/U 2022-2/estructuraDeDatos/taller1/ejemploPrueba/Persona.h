#include <string>
#include <iostream>
#ifndef PERSONA_H
#define PERSONA_H
using namespace std;

class Persona
{
    protected:
        string nombre;
        string apellido;

    public:
        Persona(string _nombre,string _apellido);
        string getNombre();
        void setNombre(string _nombre);
        string getApellido();
        void setApellido(string _apellido);

};

#endif // PERSONA_H
