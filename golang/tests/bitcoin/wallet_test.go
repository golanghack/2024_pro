package bitcoin

import (
	"testing"
)

func TestWallet(t *testing.T) {
	t.Run("deposit", func(t *testing.T) {
		wallet := Wallet{}
		wallet.Deposit(Bitcoin(10))
		AssertBalance(t, wallet, Bitcoin(10))
	})

	t.Run("withdraw funds", func(t *testing.T) {
		wallet := Wallet{Bitcoin(20)}
		err := wallet.Withdraw(Bitcoin(10))

		AssertError(t, err, ErrFunds)
		AssertBalance(t, wallet, Bitcoin(20))
	})

	t.Run("withdraw with funds", func(t *testing.T) {
		wallet := Wallet{Bitcoin(20)}
		err := wallet.Withdraw(Bitcoin(10))

		AssertNoError(t, err)
		AssertBalance(t, wallet, Bitcoin(10))
	})
}


	
