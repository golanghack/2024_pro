package selectwebsites

func Racer(slowUrl string, fastUrl string) (winner string, error error) {
	return ConfigurationRacer(slowUrl, fastUrl, TenSecondTimeout)
}
