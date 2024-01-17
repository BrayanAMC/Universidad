#include <iostream>
#include <string>
using namespace std;
int letterWeight(string word){
    char abc[]= {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    int totalSum=0;
    for(int i=0;i<word.length();i++){
        for(int j=0;j<=26;j++){
            if(word[i]==abc[j]){
                totalSum+=(j+1);
            }
        }
    }
    return totalSum;
}
struct Node{
    string nombre;
    int FE;//factor equilibrio
    int peso;
    Node* padre;
    Node* hizq;
    Node* hder;
    friend class AVL;
    Node(string nombre){//constructor
        this->nombre = nombre;
        this->padre = nullptr;
        this->hizq = nullptr;
        this->hder = nullptr;
        this->peso = letterWeight(nombre);
        this->FE = 0;
        //calcular el peso del nodo
        //llamar a un metodo??
    }

};
/**
// Clase Nodo de Arbol AVL:
class Nodo {
  public:
   // Constructor:
   Nodo(const int dat, Nodo *pad=NULL, Nodo *izq=NULL, Nodo *der=NULL) :
     dato(dat), padre(pad), izquierdo(izq), derecho(der), FE(0) {}
   // Miembros:
   int dato;
   int FE;
   Nodo *izquierdo;
   Nodo *derecho;
   Nodo *padre;
   friend class AVL;
};

class AVL {
  private:
   enum {IZQUIERDO, DERECHO};
   // Punteros de la lista, para cabeza y nodo actual:
   Nodo *raiz;
   Nodo *actual;
   int contador;
   int altura;

  public:
   // Constructor y destructor básicos:
   AVL() : raiz(NULL), actual(NULL) {}
   ~AVL() { Podar(raiz); }
   // Insertar en árbol ordenado:
   void Insertar(const int dat);
   // Borrar un elemento del árbol:
   void Borrar(const int dat);
   // Función de búsqueda:
   bool Buscar(const int dat);
   // Comprobar si el árbol está vacío:
   bool Vacio(Nodo *r) { return r==NULL; }
   // Comprobar si es un nodo hoja:
   bool EsHoja(Nodo *r) { return !r->derecho && !r->izquierdo; }
   // Contar número de nodos:
   const int NumeroNodos();
   const int AlturaArbol();
   // Calcular altura de un dato:
   int Altura(const int dat);
   // Devolver referencia al dato del nodo actual:
   int &ValorActual() { return actual->dato; }
   // Moverse al nodo raiz:
   void Raiz() { actual = raiz; }
   // Aplicar una función a cada elemento del árbol:
   void InOrden(void (*func)(int&, int) , Nodo *nodo=NULL, bool r=true);
   void PreOrden(void (*func)(int&, int) , Nodo *nodo=NULL, bool r=true);
   void PostOrden(void (*func)(int&, int) , Nodo *nodo=NULL, bool r=true);
  private:
   // Funciones de equilibrado:
   void Equilibrar(Nodo *nodo, int, bool);
   void RSI(Nodo* nodo);
   void RSD(Nodo* nodo);
   void RDI(Nodo* nodo);
   void RDD(Nodo* nodo);
   // Funciones auxiliares
   void Podar(Nodo* &);
   void auxContador(Nodo*);
   void auxAltura(Nodo*, int);
};
**/
class AVL{
    private:

        enum {IZQUIERDO, DERECHO};
        // Punteros de la lista, para cabeza y nodo actual:
        Node *raiz;
        Node *actual;
        int contador;
        int altura;
    public:

        AVL(){
            raiz = nullptr;
            actual = nullptr;
        };
        ~AVL(){
            //Podar(raiz);
        }
        void insertar(const string  nombre){
            Node*padre = NULL;
            int peso = letterWeight(nombre);
            cout<<"se insertara el mes :" <<nombre<<endl;
            cout<<"el peso de el mes :" <<nombre<<" es : "<<peso<<endl;
            actual = raiz;
            while(!Vacio(actual)&&peso!=actual->peso){
                padre = actual;
                //actual->hizq->padre = padre;
                if(peso>actual->peso){
                    actual = actual->hder;
                }else if(peso<actual->peso){
                    actual = actual->hizq;

                ;}
            }
            if(!Vacio(actual)){//el nodo ya existe

                peso--;
                cout<<"se rectifica peso del mes "<<nombre<<endl;
                cout<<"el nuevo peso del mes "<<nombre<<" es: "<<peso<<endl;
                insertarNum(nombre,peso);//el nodo intentara ingresar nuevamente ahora con el peso disminuido en una unidad
                return;


            }//si el elemento ya esta no se inserta
            //caso base el padre es null
            if(Vacio(padre)){
                cout<<"entra if"<<endl;
                raiz = new Node(nombre);
            }else if(peso < padre->peso){
                padre->hizq = new Node(nombre);
                padre->hizq->padre = padre;//el nuevo nodo sabe cual es su padre
                cout<<"entra else if menor"<<endl;
                equilibrar(padre,IZQUIERDO,true);//109
                //cout<<"sale  de equilibrar"<<endl;
            }else if(peso>padre->peso){
                padre->hder = new Node(nombre);
                padre->hder->padre = padre;
                cout<<"entra else if mayor"<<endl;
                equilibrar(padre,DERECHO,true);
            }

        };
        void insertarNum(const string  nombre,int peso){//funcion que inserta el nodo con su peso rectificado
            Node*padre = NULL;
            //int peso = letterWeight(nombre);
            cout<<"se insertara el mes :" <<nombre<<endl;
            cout<<"el peso de el mes :" <<nombre<<" es : "<<peso<<endl;
            actual = raiz;
            while(!Vacio(actual)&&peso!=actual->peso){
                padre = actual;
                //actual->hizq->padre = padre;
                if(peso>actual->peso){
                    actual = actual->hder;
                }else if(peso<actual->peso){
                    actual = actual->hizq;

                ;}
            }
            if(!Vacio(actual)){

                peso--;
                cout<<"se rectifica peso del mes "<<nombre<<endl;
                cout<<"el nuevo peso del mes "<<nombre<<" es: "<<peso<<endl;
                insertarNum(nombre,peso);
                return;


            }//si el elemento ya esta no se inserta
            //caso base el padre es null
            if(Vacio(padre)){
                cout<<"entra if"<<endl;
                raiz = new Node(nombre);
                raiz->peso = peso;
            }else if(peso < padre->peso){
                padre->hizq = new Node(nombre);
                padre->hizq->peso = peso;
                padre->hizq->padre = padre;//el nuevo nodo sabe cual es su padre
                cout<<"entra else if menor"<<endl;
                equilibrar(padre,IZQUIERDO,true);//109
                //cout<<"sale  de equilibrar"<<endl;
            }else if(peso>padre->peso){
                padre->hder = new Node(nombre);
                padre->hder->peso = peso;
                padre->hder->padre = padre;
                cout<<"entra else if mayor"<<endl;
                equilibrar(padre,DERECHO,true);
            }

        };

        bool Vacio(Node *r) { return r==NULL; }

        void equilibrar(Node *nodo,int rama,bool nuevo){
            bool salir = false;
            //recorremos camino inverso actualizado valores FE
            while(nodo && !salir){
                if(nuevo){
                    if(rama == IZQUIERDO){
                        nodo->FE--;
                    }else{
                        nodo->FE++;
                    }
                }else{
                    if(rama == IZQUIERDO){
                        nodo->FE++;
                    }else{
                        nodo->FE--;
                    }
                }
                if(nodo->FE ==0){
                    salir = true;//no esta desbalanceado
                }
                else if(nodo->FE == -2){//rotar a la derecha
                    if(nodo->hizq->FE ==1){
                        RDD(nodo);//rotacion doble derecha
                    }else{
                        RSD(nodo);//rotacion simple derecha
                    }
                    salir = true;
                }
                else if(nodo->FE ==2){//rotar a la izquierda
                    if(nodo->hder->FE ==-1){
                        RDI(nodo);//rotacion doble izquierda
                    }else{
                        RSI(nodo);//rotacion simple izquierda
                    }
                    salir = true;
                }
                if(nodo->padre){
                    if(nodo->padre->hder == nodo){
                        rama = DERECHO;
                    }else{
                        rama = IZQUIERDO;
                    }
                }
                nodo = nodo->padre;//se calcula fe con el siguiente nodo
            }
        }
        //funciones para equilibrar

        void RDD(Node*nodo){//rotacion doble derecha
            cout<<"entrando a RDD"<<endl;
            Node *Padre = nodo->padre;
            Node *P = nodo;
            Node *Q = P->hizq;
            Node *R = Q->hder;
            Node *B = R->hizq;
            Node *C = R->hder;

            if(Padre){
                if(Padre->hder ==nodo){
                    Padre->hder = R;
                }else{
                    Padre->hizq = R;
                }
            }else{
                raiz = R;
            }
            //se reconstruye el arbol
            Q->hder = B;
            P->hizq = C;
            R->hizq = Q;
            R->hder = P;
            //reasignacion de padres
            R->padre = Padre;
            P->padre = Q->padre = R;
            if(B){B->padre = Q;}
            if(C){C->padre = P;}

            //ajustamos valores de FE
            switch(R->FE){
                case -1:
                    Q->FE=0;
                    P->FE=1;
                    break;
                case 0:
                    Q->FE=0;
                    P->FE=0;
                    break;
                case 1:
                    Q->FE = -1;
                    P->FE = 0;
                    break;
            }
            R->FE = 0;
        }

        void RDI(Node *nodo){//rotacion doble izquierda
            cout<<"entrando a RDI"<<endl;
            Node *Padre = nodo->padre;
            Node *P = nodo;
            Node *Q = P->hder;
            Node *R = Q->hizq;
            Node *B = R->hizq;
            Node *C = R->hder;

            if(Padre){
                if(Padre->hder == nodo){
                    Padre->hder = R;
                }else{
                    Padre->hizq = R;
                }
            }else{
                raiz = R;
            }

            //reconstruimos el arbol
            P->hder = B;
            Q->hizq = C;
            R->hizq = P;
            R->hder = Q;
            //reasignamos padres
            R->padre = Padre;
            P->padre = Q->padre = R;
            if(B){B->padre = P;}
            if(C){C->padre = Q;}
            //ajustamos valores de FE
            switch(R->FE){
                case -1:
                    P->FE=0;
                    Q->FE=1;
                    break;
                case 0:
                    P->FE=0;
                    Q->FE=0;
                    break;
                case 1:
                    P->FE = -1;
                    Q->FE = 0;
                    break;
            }
            R->FE = 0;
        }

        void RSD(Node *nodo){//rotacion simple derecha
            cout<<"entrando a RSD"<<endl;
            Node *Padre = nodo->padre;
            Node *P = nodo;
            Node *Q = P->hizq;
            Node *B = Q->hder;

            if(Padre){
                if(Padre->hder == P){
                    Padre->hder = Q;
                }else{
                    Padre->hizq = Q;
                }
            }else{
                raiz = Q;
            }

            //reconstruimos el arbol
            P->hizq = B;
            Q->hder = P;

            //reasignamos los padres
            P->padre = Q;
            if(B){B->padre = P;}
            Q->padre = Padre;

            //ajustamos valores de FE
            P->FE = 0;
            Q->FE = 0;

        }

        void RSI(Node *nodo){//rotacion simple izquierda
            cout<<"entrando a RSI"<<endl;
            Node *Padre = nodo->padre;
            Node *P = nodo;
            Node *Q = P->hder;
            Node *B = Q->hizq;

            if(Padre){
                if(Padre->hder == P){
                    Padre->hder = Q;
                }else{
                    Padre->hizq = Q;
                }
            }else{
                raiz = Q;
            }

            //reconstruimos el arbol
            P->hder = B;
            Q->hizq = P;

            //reasignamos padres
            P->padre = Q;
            if(B){B->padre = P;}
            Q->padre = Padre;

            //ajustamos valores de FE
            P->FE = 0;
            Q->FE = 0;
        }

        void inOrden(Node *p){
            if(p){
                inOrden(p->hizq);
                cout<<"nombre nodo: "<<p->nombre<<endl;
                cout<<"peso nodo: "<<p->peso<<endl;
                inOrden(p->hder);
            }
        }
        void preOrden(Node *p){
            if(p){
                cout<<"nombre nodo: "<<p->nombre<<endl;
                cout<<"peso nodo: "<<p->peso<<endl;
                preOrden(p->hizq);
                preOrden(p->hder);

            }
        }
        void postOrden(Node *p){
            if(p){
                postOrden(p->hizq);
                postOrden(p->hder);
                cout<<"nombre nodo: "<<p->nombre<<endl;
                cout<<"peso nodo: "<<p->peso<<endl;

            }
        }
        Node* getRaiz(){
            return raiz;
        }



};

int main(){
    cout<<"hola mundo"<<endl;
    AVL avl = AVL();
    avl.insertar("enero");
    avl.insertar("febrero");
    avl.insertar("marzo");
    avl.insertar("abril");
    avl.insertar("mayo");
    avl.insertar("junio");
    avl.insertar("julio");
    avl.insertar("agosto");
    avl.insertar("septiembre");
    avl.insertar("octubre");
    avl.insertar("noviembre");
    avl.insertar("diciembre");


    cout << "-----------InOrden-----------"<<endl;
    //avl.inOrden(mostrar);
    avl.inOrden(avl.getRaiz());
    cout << "-----------PreOrden-----------"<<endl;
    avl.preOrden(avl.getRaiz());
    cout << "-----------PostOrden-----------"<<endl;
    avl.postOrden(avl.getRaiz());
    return 0;
}