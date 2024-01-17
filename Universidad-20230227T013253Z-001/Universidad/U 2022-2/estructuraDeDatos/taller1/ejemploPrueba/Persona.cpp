#include "Persona.h"
#include <iostream>
using namespace std;
Persona::Persona(string _nombre,string _apellido)
{
    nombre = _nombre;
    apellido = _apellido;
}

string Persona::getNombre(){
    return nombre;

}
void Persona::setNombre(string _nombre){

    nombre = _nombre;
}
string Persona::getApellido(){
    return apellido;
}
void Persona::setApellido(string _apellido){

    apellido = _apellido;
}
