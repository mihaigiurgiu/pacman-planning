(define (domain delivery)
  (:requirements :strips :adl)
  (:types agent position)
  (:predicates 
    (inc ?a ?b - position)
    (dec ?a ?b - position)
    (at ?a - agent ?x ?y - position)
    (hole ?x ?y)
    (picked-up ?x ?y)
    (food-at ?x ?y - position)
    )
   
  (:action 
    north
    :parameters (?car - agent)
    :precondition ()
    :effect (forall (?x ?y ?yn - position)
                    (when 
                      (and (at ?car ?x ?y)
                           (dec ?y ?yn)
                           (not (hole ?x ?yn))
                      )
                      (and (not (at ?car ?x ?y))
                           (at ?car ?x ?yn))
                    )
            )
  )

  (:action 
    south
    :parameters (?car - agent)
    :precondition ()
    :effect (forall (?x ?y ?yn - position)
                    (when 
                      (and (at ?car ?x ?y)
                           (inc ?y ?yn)
                           (not (hole ?x ?yn))
                      )
                      (and (not (at ?car ?x ?y))
                                (at ?car ?x ?yn)
                      )
                    )
            )
  )

  (:action 
    east
    :parameters (?car - agent)
    :precondition ()
    :effect (forall (?x ?y ?xn - position)
                    (when 
                      (and (at ?car ?x ?y)
                           (inc ?x ?xn)
                           (not (hole ?xn ?y)
                      )
                    )
                      (and (not (at ?car ?x ?y))
                                (at ?car ?xn ?y))
                      )
              )
  )

  (:action 
    west
    :parameters (?car - agent)
    :precondition ()
    :effect (forall (?x ?y ?xn - position)
                    (when 
                      (and (at ?car ?x ?y)
                           (dec ?x ?xn)
                           (not (hole ?xn ?y)
                      )
                    )
                      (and (not (at ?car ?x ?y))
                                (at ?car ?xn ?y)
                      )
                    )
            )
  )

  (:action 
    pick-up
    :parameters (?car - agent)
    :precondition ()
    :effect (forall (?x ?y - position)
                    (when 
                      (and (at ?car ?x ?y)
                           (food-at ?x ?y)
                      )
                      (picked-up ?x ?y)
                    )
            )
  )

)
