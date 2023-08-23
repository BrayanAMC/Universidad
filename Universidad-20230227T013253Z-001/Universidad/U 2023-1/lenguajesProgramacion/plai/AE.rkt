#lang plai


;; BNF
;;<AE> ::-<number>
;;     | {+ <AE> <AE>}
;;     | {- <AE> <AE>}
;;     | {* <AE> <AE>}
;;     | {! <number>}
;;     | {/ <AE> <AE>}
;;     | {++ <number>}


;; Arithmetic Expression data type
(define-type AE
  [num (n number?)]
  [add (l AE?)
       (r AE?)]
  [sub (l AE?)
       (r AE?)]
  [mul (l AE?)
       (r AE?)]
  [fac (l num?)]
  [div (l AE?)
       (r AE?)]
       )

;; parse : program -> AST (AE)
(define (parse program)
  (cond
    [(number? program) (num program)]
    [(list? program)
     (case (first program)
       [(+) (add (parse(second program))
                 (parse(third program)))]
       [(-) (sub (parse(second program))
                 (parse(third program)))]
       [(*) (mul (parse(second program))
                 (parse(third program)))]
       [(!) (fac (num(second program))
                 )]
       [(/) (div (parse(second program))
                 (parse(third program)))]
       [(++) (add (parse(second program)) (num 1))]
       )]
    ))

(define (factorial n)
  (if (or (not (integer? n)) (< n 0))
      (error "El factorial solo se puede calcular para números enteros no negativos.")
      (if (<= n 1)
          1
          (* n (factorial (- n 1))))))

(display (factorial 5)) ; Ejemplo de uso: calcula el factorial de 5 y muestra el resultado
(newline)

; El interprete 
; interp: AST -> number
(define (interp program)
  (type-case AE program
             [num (n) n] 
             [add (l r) (+ (interp l) (interp r))] 
             [sub (l r) (- (interp l) (interp r))]
             [mul (l r) (* (interp l) (interp r))]
             [fac (l)   (factorial (interp l) )]
             [div (l r) (if (= (interp r) 0) (error "no zero" ) (/ (interp l) (interp r)))]
    
             )) 

; Una función para simplificar el uso
(define (ejecutar program) 
  (interp (parse program)))


; TEST PARSER
(test (parse '3) (num 3))
(test (parse '{+ 1 2}) (add (num 1) (num 2)))
(test (parse '{+ {- 2 1} 3}) (add (sub (num 2) (num 1)) (num 3)))
(test (parse '{* 1 2}) (mul (num 1)  (num 2)))
(test (parse '{! 3}) (fac (num 3)))


; TEST INTERPRETE
(test (ejecutar '3) 3)
(test (ejecutar '{+ 1 2}) 3)
(test (ejecutar '{+ {- 2 1} 3}) 4)

;; TESTS PARA ^
(test (ejecutar '{* 2 3}) 6)
(test (ejecutar '{+ {* 2 3} 2}) 8)
(test (ejecutar '{+ {* {+ 1 1} 3} 2}) 8)
;; TEST PARA /
(test (ejecutar '{/ 1 1}) 1)
(test (ejecutar '{/ 4 2}) 2)

(test (ejecutar '{++ 5}) 6)