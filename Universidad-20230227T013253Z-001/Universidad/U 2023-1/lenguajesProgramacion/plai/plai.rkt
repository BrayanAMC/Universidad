#lang plai

;; BNF
;;<AE> ::-<number>
;;     | {+ <AE> <AE>}
;;     | {- <AE> <AE>}
;;     | {* <AE> <AE>} 


;; Arithmetic Expression data type
(define-type AE
  [num (n number?)]
  [add (l AE?)
       (r AE?)]
  [sub (l AE?)
       (r AE?)]
  [mul (l AE?)
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
       )]
    ))


; El interprete 
; interp: AST -> number
(define (interp program)
  (type-case AE program
             [num (n) n] 
             [add (l r) (+ (interp l) (interp r))] 
             [sub (l r) (- (interp l) (interp r))]
             [mul (l r) (* (interp l) (interp r))]
             )) 

; Una función para simplificar el uso
(define (ejecutar program) 
  (interp (parse program)))


; TEST PARSER
(test (parse '3) (num 3))
(test (parse '{+ 1 2}) (add (num 1) (num 2)))
(test (parse '{+ {- 2 1} 3}) (add (sub (num 2) (num 1)) (num 3)))


; TEST INTERPRETE
(test (ejecutar '3) 3)
(test (ejecutar '{+ 1 2}) 3)
(test (ejecutar '{+ {- 2 1} 3}) 4)

;; TESTS PARA ^
(test (ejecutar '{* 2 3}) 6)
(test (ejecutar '{+ {* 2 3} 2}) 8)
(test (ejecutar '{+ {* {+ 1 1} 3} 2}) 8)