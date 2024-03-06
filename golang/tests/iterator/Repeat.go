package iterator


const repeatConst = 5 

func Repeat(str string) string {
	var repeated string
	for i := 0; i < repeatConst; i++ {
		repeated += str 
	}
	return repeated
}