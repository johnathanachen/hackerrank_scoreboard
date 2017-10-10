const listDiv = document.querySelectorAll('.container')
const button = document.getElementById('button');
const newDiv = listDiv[0];
button.addEventListener('click', function(event){
	const leaderboard = newDiv.parentNode;
	alert(leaderboard.tagName);
	var cln = newDiv.cloneNode(true);
	leaderboard.appendChild(cln);

});
console.log(listDiv);

listDiv.forEach(function(elem) { 
	elem.addEventListener('input', function(event){
		updateScoreboard();
		alert('updated', event.target.childNodes);
	});
});

function updateScoreboard(){
	[].forEach.call(listDiv, function(div) {
	console.log(div)
	})
}
