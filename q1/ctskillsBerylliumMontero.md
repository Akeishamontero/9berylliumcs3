# Computational Thinking Exercise

## Smart School Canteen Queue
**Name:** Princess Akeisha Eunice 
**Section:** 9 - Beryllium 
**Last Name:** Montero
**Date:** August 20, 2026


## Step 1: Identify the Big Problem

### Main Problem

The school canteen's ordering process suffers from an inefficient and slow ordering process. This is due to severe overcrowding during peak lunch breaks, as multiple classes are dismissed simultaneously. This bottleneck is worsened by slow student decision-making.Also because the lack of a food inventory tracking system, which significanly delays transactions and the entire ordering process.

---

## Step 2: Identify Three to Four Sub-Problems

1. Students spend too much time viewing the menu and deciding on their meals while standing in front of the counter that slows down the entire line.
2. The cashier must manually calculate the cost of the items and also the cash change, which makes the line wait longer and cause human error.
3. The amount of students entering and inside the canteen causes traffic layout issues and also the overcrowding might cause accidents.
4. If food items run out unexpectedly, students may have to change their orders, which can make the ordering process longer.

---

## Step 3: Define Computational Thinking Approaches

|     Sub-Problem     |        CT Skill         |            Proposed Solution           |

| Slow Menu Decisions | Pattern Recognition can |  Identify the food items that students  |
                      | helps identify which me-| commonly order and display their names  |
                      | als students choose more| and prices clearly so students can deci-|
                      | often, making it easier | de faster. By identifying we can create |                           
                      | to organize the menu ar-| a digital menu that highlights meals    |
                      | ound popular choices.   | shows clear prices, and let students    |
                      |                         | decide what they want before reaching   |
                      |                         | the cashier.                            |

| Checkout Processing | Algorithm Design helps  |  A proposed solution could be using a   |
  Delays              | create a clear set of   | smart checkout system that automatically|
                      | steps that can calculate| sums up prices, calculates the change   |
                      | totals and changes qui- | without creating human errors that could|                           
                      | ckly and accurately.    | slow down the process.                  |
                                             
| Canteen Overcrowding| Decomposition helps     |  We can create seperate areas for order-|
                      | break the overcrowding  | ing, waiting and collecting food, with a|
                      | problem into smaller    | simple queue system to keep students    |
                      | parts that are easier to| moving smoothly.                        |                           
                      | manage                  |                                         |
                 
| Tracking Food       | Abstraction helps the   |  By using a digital inventory tracker   |
  Inventory           | system to focus only on | that shows each food item, its price and|
                      | the important informati-| how many servings left until unavailable|
                      | on needed to know what  | also an alert to measure if it can still|                           
                      | food is available.      | be ordered or running low on stocks.    |                             
||||
||||


## Step 4: Algorithmic Solution

### Selected Sub-Problem
Checkout Processing Delays

### Pseudocode

START

Ask student to enter the number of items

Set total = 0

REPEAT for each item
    Ask for the item price
    Add item price to total
END REPEAT

Display total price

Ask student to enter payment amount

WHILE payment amount < total
    Display "Not enough money"
    Ask student to enter payment amount  <-- Overwrites the old payment amount
END WHILE

Change = payment amount - total

Display change

Display "Payment successful"

END
