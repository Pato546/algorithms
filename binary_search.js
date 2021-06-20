function binary_search(array, item){
	let min = 0;
	let max = array.length - 1;

	while ( min <= max) {
		let mid = Math.round((min + max) / 2);
		if (array[mid] === item) {
			return mid;
		}
		if (array[mid] < item) {
			min = mid + 1;
		}
		else {
			max = mid -1;
		}
	}
	return -1;
}

let array = ['Ababio', 'Patrick']
console.log(binary_search(array, 'Ababio'))

