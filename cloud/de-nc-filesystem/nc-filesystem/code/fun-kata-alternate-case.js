function alternateCase(string) {
	let alternatingString = "";
	// start with a capital letter
	let toUpper = true;
	for (letter of string) {
		alternatingString += toUpper ? letter.toUpperCase() : letter.toLowerCase();
		// if letter wasn't a space then toggle toUpper
		if (letter !== " ") toUpper = !toUpper;
	}
	return alternatingString;
}
