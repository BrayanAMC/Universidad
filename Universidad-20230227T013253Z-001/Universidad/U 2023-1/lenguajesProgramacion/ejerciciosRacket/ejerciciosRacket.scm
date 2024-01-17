#lang racket
(define (generate n)
        (generate-for n 1)
  )

(define (generate-for n i)
    (if (=< i n) 
        (cons i (generate-for n (+ i 1)));#t
        (list);#f
        
        )
  )

;defina la funcion(vector-suma-pares v) que sume los numeros pares de un vector
(define (vector-suma-pares-aux v)
        (cond
          [(null? 0)]
          [(even? (car l)) (+ (car v) (vector-suma-pares-aux (cdr v)))]
          [else (vector-suma-pares-aux (cdr v))]
        )
)

(define(mymap n l)
  (map (λ (x) (* x n)) l )
)

(define (filterMenores x)
  (λ(y) (< y x))
   
)
(define (filterMayores x)
  (λ(y) (> y x))
   
)
(filter (filterX 10) '(1 20 3))

(define (qs l)
  (qs (filter (filterMenores (car l)) (l)))
  (qs (filter (filterMayores (car l)) (l)))
)