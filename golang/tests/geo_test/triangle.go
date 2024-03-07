package geotest

type Triangulum struct {
	Base float64
	Height float64
}

func (t Triangulum) Area() float64 {
	return (t.Base * t.Height) * 0.5
}