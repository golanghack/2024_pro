package dict

const (
	ErrNotFound = DictErr("could not find a word in dict")
	ErrNoExists = DictErr("cannot add word in dict")
	ErrDoesNotExists = DictErr("word does not exists")
)

type DictErr string

func (e DictErr) Error() string {
	return string(e)
}