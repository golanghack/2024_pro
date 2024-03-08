package dict


type Dict map[string]string

func (d Dict) Search(word string) (string, error) {
	definition, ok := d[word]

	if !ok {
		return "", ErrNotFound
	}
	return definition, nil
}

func (d Dict) Add(word string, definition string) error {
	_, err := d.Search(word)
	switch err {
	case ErrNotFound:
		d[word] = definition
	case nil:
		return ErrNoExists
	default:
		return err 
	}
	return nil 
}

func (d Dict) Update(word, definition string) error {
	_, err := d.Search(word)

	switch err {
	case ErrNotFound:
		return ErrDoesNotExists
	case nil:
		d[word] = definition
	default:
		return err
	}
	return nil
}

func (d Dict) Delete(word string) {
	delete(d, word)
}