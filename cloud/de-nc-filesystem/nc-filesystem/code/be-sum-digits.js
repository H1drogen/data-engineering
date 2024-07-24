function sumDigits(number) {
	const digits = String(number).match(/\d/g);
	let sum = 0;
	digits.forEach((digit) => (sum += Number(digit)));
	return sum;
}
