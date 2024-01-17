#ifndef ESTUDIANTE_H
#define ESTUDIANTE_H
#include <iostream>
#include "Persona.h"


class Estudiante : public Persona
{
    using Persona::Persona;
    private:
        int semestre;
        int edad;
    public:
        Estudiante(int semestre,int edad);
        int getSemestre();
        void setSemestre(int _semestre);
        int getEdad();
        void setEdad(int _edad);
        //virtual ~Estudiante();
};

#endif // ESTUDIANTE_H
