; It looks like this:
;
;   1 2 3 4 5 6
;6  J . . . . .
;5  . . . . . .
;4  W W W W . .
;3  . . . G W .
;2  . W W W . .
;1  . . . . . F

(define (problem maze1)
  (:domain maze)
  (:objects x1 x2 x3 x4 x5 x6 y1 y2 y3 y4 y5 y6 - position car - agent)
  (:init
    (inc x1 x2) (inc x2 x3) (inc x3 x4) (inc x4 x5) (inc x5 x6)
    (inc y6 y5) (inc y5 y4) (inc y4 y3) (inc y3 y2) (inc y2 y1)
    (dec x6 x5) (dec x5 x4) (dec x4 x3) (dec x3 x2) (dec x2 x1) 
    (dec y5 y6) (dec y4 y5) (dec y3 y4) (dec y2 y3) (dec y1 y2) 

    (wall x1 y4) (wall x2 y4) (wall x3 y4) (wall x4 y4)
    (wall x5 y3)
    (wall x2 y2) (wall x3 y2) (wall x4 y2)
    (food-at x6 y1)
    (at car x4 y1))
  (:goal
    (and (picked-up x6 y1) (at car x4 y3))
  )
)
