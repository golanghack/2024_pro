package usemath

func RouthlyEqualPoint(a, b Point) bool {
	return RouthlyEqualFloat(a.X, b.X) && RouthlyEqualFloat(a.Y, b.Y)
}