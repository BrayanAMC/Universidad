#lang racket
(define (calcular-producto-punto l1 l2)
  (cond
    [(empty? l1) 0]
    [(and (even? (car l1)) (even? (car l2)))    (+ (* (car l1) (car l2)) (calcular-producto-punto (cdr l1) (cdr l2)))     ]
    (else (calcular-producto-punto (cdr l1) (cdr l2))) 
  )
)

  
(calcular-producto-punto '(2 2 3) '(4 2 3))
;