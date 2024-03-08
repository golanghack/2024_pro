package bitcoin

import "errors"

var ErrFunds = errors.New("oh my god")

func (w *Wallet) Withdraw(amount Bitcoin) error {
	if amount > w.balance {
		return ErrFunds
	}
	w.balance -= amount
	return nil 
}