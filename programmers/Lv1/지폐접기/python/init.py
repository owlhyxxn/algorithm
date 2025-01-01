# PCCE
def solution(wallet, bill):
    answer = 0
    largeBill = max(bill[0], bill[1])
    smallBill = min(bill[0], bill[1])
    largeWallet = max(wallet[0], wallet[1])
    smallWallet = min(wallet[0], wallet[1])
    
    while (largeBill > largeWallet or smallBill > smallWallet):
        largeBillBefore = int(largeBill / 2)
        smallBillBefore = smallBill
        largeBill = max(largeBillBefore, smallBillBefore)
        smallBill = min(largeBillBefore, smallBillBefore)
        answer += 1
    return answer