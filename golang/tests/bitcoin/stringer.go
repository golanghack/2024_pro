package bitcoin

import "fmt"

type Stringer interface {
	String() string 
}

func (b Bitcoin) String() string {
	return fmt.Sprintf("%d BTC", b)
}