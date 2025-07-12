;Q1
(define (over-or-under num1 num2) 
 ( cond ((< num2 num1) 1)
        ((= num2 num1) 0)
        ((> num2 num1) -1)
       
        ))

;Q2
(define (make-adder num) (lambda (inc )(+ num inc)))

;Q3
(define (composed f g) (lambda (x) (f (g x))))


;Q4
;(define (repeat f n)(if ( = n 0) total (define total  ((make-adder 0)(repeat f (- n 1))))))
(define (repeat f n)
(
  if (= n 0)
  (lambda (x) x )
  (composed f (repeat f (- n 1)))  ; The difficulties which need to be noted.
))  

;Q5
(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
(
  cond ((= (modulo (max a b) (min a b )) 0 ) (min a b) )
        (else(gcd(min a b)(modulo (max a b)(min a b)) ))
  )
)

