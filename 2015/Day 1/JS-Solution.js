whatFloor = (inputText) => {
	inputText = inputText.split('');
	floor = 0;
	for(let char of inputText){
	  if (char == '('){
	    floor += 1;
	  }
	  else{
	    floor -= 1;
	  }
	}
	
	return floor;
};

//This one is less readable in my opinion, but it's shorter.

/*
whatFloor = (inputText) => {
	inputText = inputText.split('');
	goUp = (inputText.filter(char => char == '(')).length;
	goDown = inputText.length - goUp;
	floor = goUp - goDown;
	
	return floor;
};
*/