(define (square n) (* n n))

(define (even? n)
  (if (= 0 (modulo n 2)) #t #f ))
  ;(if (= 0 (modulo n 2)) (#t) (#f) ))  SchemeError: bool is not callable: #f

(define (pow base exp)
  (cond 
    ((zero? exp) 1)
    ;(else  ((square  (pow base (- exp 1))))
    ;(else (lambda (exp)((square base)(- exp 1))(base exp) ))
    ((even? exp) (square (pow base (/ exp 2))))
    (else (* base (pow base (- exp 1))))
    )
)


(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (repeatedly-cube (- n 1) (* x x x))))


(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car(cdr s)))

(define (caddr s) (car(cdr(cdr s))))
