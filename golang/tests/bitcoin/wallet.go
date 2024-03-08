package bitcoin

import "fmt"


type Wallet struct {
	balance Bitcoin

}

func (w *Wallet) Deposit(amount Bitcoin) {
	fmt.Printf("address of balance -> %p \n", &w.balance)
	w.balance += amount

}

func (w *Wallet) Balance() Bitcoin{
	return w.balance
}