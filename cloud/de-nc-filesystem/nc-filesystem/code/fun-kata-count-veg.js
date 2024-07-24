function countVeg(vegetables, type) {
	const matchingVegetables = vegetables.filter(
		(vegetable) => vegetable.type === type
	);
	let totalQuantity = 0;
	matchingVegetables.forEach((vegetable) => {
		totalQuantity += vegetable.quantity;
	});
	return totalQuantity;
}
