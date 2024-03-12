package generics

import "testing"

func TestStack(t *testing.T) {
	t.Run("integer stack", func(t *testing.T) {
		myStackInts := new(Stack[int])


		AssertTrue(t, myStackInts.IsEmpty())
		// add 
		myStackInts.Push(123)
		AssertFalse(t, myStackInts.IsEmpty())
		// add another
		myStackInts.Push(456)
		value, _ := myStackInts.Pop()
		AssertEqual(t, value, 456)
		value, _ = myStackInts.Pop()
		AssertEqual(t, value, 123)
		AssertTrue(t, myStackInts.IsEmpty())

		// can get numbers
		myStackInts.Push(1)
		myStackInts.Push(2)
		first, _ := myStackInts.Pop()
		second, _ := myStackInts.Pop()
		AssertEqual(t, first + second, 3)
	})
}