# importing another python code (calc_adv_return.py) as module and using it "as" 'calc_adv_new'

import calc_adv_return as calc_adv_new 


new_addtn= calc_adv_new.addtn(300,232)  #calling the addtn() from calc_adv_return.py
print("New addition result: ", new_addtn)

new_subtn= calc_adv_new.subtn(300,230)
print("New substraction result: ", new_subtn)

new_divtn= calc_adv_new.divtn(300,24)
print("New division result: ", new_divtn)

new_multn= calc_adv_new.multn(300,10)
print("New multiplication result: ", new_multn)


