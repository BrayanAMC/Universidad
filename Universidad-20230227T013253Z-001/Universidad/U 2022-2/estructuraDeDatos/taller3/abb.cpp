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
    int peso;
    Node* hizq;
    Node* hder;
    Node(string nombre){
        this->nombre = nombre;
        this->hizq = nullptr;
        this->hder = nullptr;
        this->peso = letterWeight(nombre);
        //calcular el peso del nodo
        //llamar a un metodo??
    }

};
class ABB{
    private:
        Node *root;
    public:
        ABB(){
            root = nullptr;
        };
        void insertar(Node &raiz,Node*node){

        };

};

int main(){
    cout<<"hola mundo"<<endl;

    return 0;
}
