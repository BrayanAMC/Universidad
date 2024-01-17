#include "Estudiante.h"
#include <iostream>
Estudiante::Estudiante(int _semestre,int _edad){

    semestre = _semestre;
    edad = _edad;
}
int Estudiante::getSemestre(){

    return semestre;
}
void Estudiante::setSemestre(int _semestre){
    semestre = _semestre;
}
int Estudiante::getEdad(){
    return edad;
}
void Estudiante::setEdad(int _edad){
    edad = _edad;
}
