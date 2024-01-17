#lang racket

(define (generate n)
        (generate-for n 1)
  )

(define (generate-for n i)
    (if (<= i n) 
        (cons i (generate-for n (+ i 1)));#t
        (list);#f
        
        )
  )
(print (generate 4))

;1) Haga una función que vaya restando de izquierda a derecha todos los números de una lista. 
;Ejemplo ‘(1 2 3) = -1 -2 -3 = -6

(define (restLeftRight l)
        (if (null? l)
            0;t
            (+ (* (car l) -1) (restLeftRight (cdr l)))                ;f
            )
        
  )

(print (restLeftRight '(1 2 3)))

;2. Haga una función que devuelva el número negativo de cada número de una lista.

(define (negativeWay l)
     (cond
       [(null? l) l]
       
       [(negative? (car l)) (cons (car l) (negativeWay (cdr l))) ]
       [else (cons (* (car l) -1) (negativeWay (cdr l)))]

     )


)
(print (negativeWay '(1 2 3)))

;3. Haga una función que reciba (x y) numéricos. Esta debe entregar el cuadrante en que se 
;encuentran esas coordenadas.

(define(cuadrante x y )
  (if (negative? x)
      (if (negative? y);t x es negativo
          (print "3° cuadrante");t y es negativa
          (print "2° cuadrante");f y no es negativa
      )
      (if(negative? y);f x no es negativo
         (print "4° cuadrante");t y es negativa
         (print "1° cuadrante");f y no es negativa
      )   
  )
    
    
  
)
(cuadrante 5 -5)

;combinaciones
;+x+y-> 1° cuadrante
;+x-y-> 4° cuadrante
;-x+y-> 2° cuadrante
;-x-y-> 3° cuadrante

;4. Haga una función que cuente la longitud de un String.
(define (stringLength str)
  (cond
    [(string? str) (display (format "el largo del string es: ~a" (string-length str)))]
    [(print "la variable no es un string")]
  )
)
(stringLength "holamundo")

;5. Haga una función que cuente la cantidad de elementos de una lista sin usar (length )



;. Haga una función que filtre los números que son resultados de un factorial de 1 a 10 (1 (1!), 2 
;  (2!), 6 (3!), 24 (4!), etc) de una lista. Ejemplo: ‘(1 2 3 4 5 6) -> ‘(3 4 5)
(define (filtrar-factoriales lista)
  (define (factoriales-hasta n)
    (if (= n 0)
        '(1)
        (cons (* n (car (factoriales-hasta (- n 1))))
              (factoriales-hasta (- n 1)))))
  (define factoriales (foldl append '() (map factoriales-hasta (range 1 11))))
  (filter (lambda (x) (member x factoriales)) lista))


(filtrar-factoriales '(1 2 3 4 5 6))














