#include <iostream>
#include "Persona.h"
using namespace std;
#include "Estudiante.h"
int main()
{
    //Persona p1("daniel","compadre");
    Estudiante e1("a","M",4,22);
    string nombre = e1.getNombre();
    string apellido = e1.getApellido();
    int semestre = e1.getSemestre();
    int edad = e1.getEdad();
    cout <<"el nombre del alumno es :"<< nombre << endl;
    cout <<"el apellido del alumno es :"<< apellido << endl;
    cout <<"el semestre del alumno es :"<< semestre << endl;
    cout <<"la edad del alumno es :"<< edad << endl;

    return 0;
}