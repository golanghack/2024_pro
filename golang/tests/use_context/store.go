package usecontext

type Store interface {
	Fetch() string
	Cancel() 
}