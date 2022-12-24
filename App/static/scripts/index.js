let sentiment_images = {
	Anger: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRJ837oFr_R38b-ti0ApEkkOJmeDUTyAspCbFLHuxud76HwWzwKAN6FEyRBzYPiyClnqA&usqp=CAU",
	Sadness:
		"https://i.pinimg.com/736x/d6/8c/cc/d68cccf57faa218d16c582f5218c9df3--sad-faces-kid-activities.jpg",
	Fear: "https://easydrawingguides.com/wp-content/uploads/2021/11/Scared-Face-step-by-step-drawing-tutorial-step-10.png",
	Joy: "https://thumbs.dreamstime.com/b/cute-boy-face-cartoon-vector-illustration-graphic-design-cute-boy-face-cartoon-110656400.jpg",
	Surprise:
		"https://i.pinimg.com/originals/90/4a/0c/904a0c3e06315437a3a6938a4308725c.png",
	Disgust:
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXpZFCGDJKsFBbrPJoF0HpL1rK7BHsZJehkQ&usqp=CAU",
};
const sentiment_values = ["Anger", "Fear", "Joy", "Disgust", "Surprise", "Anger"];
window.onload=()=>{
	const input = document.getElementById("input");
	const MainOutputContainer = document.getElementById("MainOutputContainer");
	const FilterationSection = document.getElementById("FilterationSection");
	const ValidationSection = document.getElementById("ValidationSection");
	const TokenizationSection = document.getElementById("TokenizationSection");
	const LemmetizationSection = document.getElementById("LemmetizationSection");
	const POSTaggingSection = document.getElementById("POSTaggingSection");
}
async function getResult(event) {
	event.preventDefault();
	// console.log(input.value);
	if (input.value.trim().trim() == "") {
		// window.alert("Please Enter Your Sentiment First");
	} else {
		try {
			let response = await fetch("/getresult", {
				method: "POST",
				headers: {
					"Content-Type": "Application/json",
				},
				body: JSON.stringify({
					text: input.value.trim(),
				}),
			});
			let result = await response.json();
			// console.log(result);
			MainOutputContainer.style.display = "grid";
			FilterationSection.style.display = "none";
			ValidationSection.style.display = "none";
			TokenizationSection.style.display = "none";
			LemmetizationSection.style.display = "none";
			POSTaggingSection.style.display = "none";
			for (const key in sentiment_values) {
				// console.log(key);
				if (
					sentiment_values[key].toLocaleLowerCase() ==
					result.sentiment
				) {
					MainOutputContainer.innerHTML = `
				<div class="finalOutput">
					<h2>Predicted Sentiment is</h2>
					<h1> ${sentiment_values[key]}</h1>
					<img src="${sentiment_images[sentiment_values[key]]}" alt="">
					<p>Generalized Sentiment is :<strong> ${
						result.generalizedPrediction
					}</strong></p>
					<p>More Specific Sentiment is : <strong>${
						result.specificPrediction
					}</strong></p>
				</div>					
				<div class="fileration">
					<h4>Filteration</h4>
					<div class="value">${result.filtered}</div>
				</div>
				<div class="tokenization">
					<h4>Tokenization</h4>
					<div class="value">${result.tokenized}</div>
				</div>
				<div class="lemmetization">
					<h4>Lemmetization</h4>
					<div class="value">${result.lemmetized}</div>
				</div>
				<div class="Vectorization">
					<h4>POS Tagging</h4>
					<div class="value">${result.POSTagged}</div>
				</div>
					`;
					window.location = `#input`;
				}
			}
		} catch (error) {
			// console.log(error);
		}
	}
}

function clearInput(event) {
	document.getElementById("input").value = "";
}

async function SubmitFile(event) {
	// console.log("submitted");
	let file = document.getElementById("file").files[0];
	if (!!file) {
		// console.log(file);
		let filename = file.name;
		// console.log(filename);
		let extention = file.name.split(".")[file.name.split(".").length - 1];
		// console.log(extention);
		if (extention.toLowerCase() == "txt") {
			// console.log("extension accepted");
			if (file.size < 1000000) {
				try {
					let formData = new FormData();
					formData.append("file", file ? file : "");
					let response = await fetch("/upload", {
						method: "POST",
						body: formData,
					});
					// console.log(response);
					let data = await response.json();
					// console.log(data);
					document.getElementById("input").value = data.data;
				} catch (error) {
					// console.log(error);
				}
			} else {
				window.alert("more than 1 mb is mot allowed");
			}
		} else {
			window.alert("extension not allowed, only txt file is permitted");
		}
	} else {
		window.alert("Please Select File Frst");
	}
}

async function validateTheScript(event) {
	event.preventDefault();
	if (input.value.trim() == "") {
		window.alert("Please Enter Your Sentiment First");
	} else {
		try {
			let response = await fetch("/validate", {
				method: "POST",
				headers: {
					"Content-Type": "Application/json",
				},
				body: JSON.stringify({
					text: input.value.trim(),
				}),
			});
			let result = await response.json();
			// console.log(result);
			MainOutputContainer.style.display = "none";
			FilterationSection.style.display = "none";
			ValidationSection.style.display = "flex";
			TokenizationSection.style.display = "none";
			LemmetizationSection.style.display = "none";
			POSTaggingSection.style.display = "none";
			if (!!result.data) {
				if (result.data == "Valid") {
					ValidationSection.innerHTML = `
					<h1>Validation Output</h1>
				<div class="output">
					<img src="https://media.istockphoto.com/id/924932028/vector/grunge-green-valid-square-rubber-seal-stamp-on-white-background.jpg?s=170667a&w=0&k=20&c=X6KOlHSu-YOQIeiZKoZCgw4pqsK7ayrwJfIuVZNAbXw=" alt="">
					<h1>Given Text is Valid As per the English Language</h1>
					`;
				} else {
					ValidationSection.innerHTML = `
					<h1>Validation Output</h1>
				<div class="output">
					<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTne1vTscvxPsxY5-YxsMDrBwmfPEPmpP7fcXnoU259U2pApYFVdCTR1aq-RpWyyAvI0bU&usqp=CAU" alt="">
					<h1>Given Text is InValid As per the English Language</h1>
					`;
				}
			} else {
				window.alert("Some Error occured");
			}
		} catch (error) {
			// console.log(error);
		}
	}
}

async function filterTheScript(event) {
	event.preventDefault();
	if (input.value.trim() == "") {
		window.alert("Please Enter Your Sentiment First");
	} else {
		try {
			let response = await fetch("/filterthetext", {
				method: "POST",
				headers: {
					"Content-Type": "Application/json",
				},
				body: JSON.stringify({
					text: input.value.trim(),
				}),
			});
			let result = await response.json();
			// console.log(result);
			MainOutputContainer.style.display = "none";
			FilterationSection.style.display = "flex";
			ValidationSection.style.display = "none";
			TokenizationSection.style.display = "none";
			LemmetizationSection.style.display = "none";
			POSTaggingSection.style.display = "none";
			if (!!result.data) {
				if (result.data == "ERROR") {
					FilterationSection.innerHTML = `
					<h1>Filtered Output is</h1>
					<div class="output">Sorry Some Error Occurred</div>
					`;
				} else {
					FilterationSection.innerHTML = `
					<h1>Filtered Output is</h1>
					<div class="output">" ${result.data} "</div>
					`;
				}
			} else {
				window.alert("Some Error occurred");
			}
		} catch (error) {
			// console.log(error);
		}
	}
}
async function getTokens(event) {
	event.preventDefault();
	if (input.value.trim() == "") {
		window.alert("Please Enter Your Sentiment First");
	} else {
		try {
			let response = await fetch("/tokenize", {
				method: "POST",
				headers: {
					"Content-Type": "Application/json",
				},
				body: JSON.stringify({
					text: input.value.trim(),
				}),
			});
			let result = await response.json();
			// console.log(result);
			MainOutputContainer.style.display = "none";
			FilterationSection.style.display = "none";
			ValidationSection.style.display = "none";
			TokenizationSection.style.display = "flex";
			LemmetizationSection.style.display = "none";
			POSTaggingSection.style.display = "none";
			if (!!result.data) {
				if (result.data == "ERROR") {
					TokenizationSection.innerHTML = `
					<h1>Tokenization Output</h1>
				<div class="output">Sorry Some Error Occurred</div>
					`;
				} else {
					TokenizationSection.innerHTML = `
					<h1>Tokenization Output</h1>
				<div class="output">${result.data}</div>
					`;
				}
			} else {
				window.alert("Some Error occured");
			}
		} catch (error) {
			// console.log(error);
		}
	}
}

async function getStems(event) {
	event.preventDefault();
	if (input.value.trim() == "") {
		window.alert("Please Enter Your Sentiment First");
	} else {
		try {
			let response = await fetch("/lemmetization", {
				method: "POST",
				headers: {
					"Content-Type": "Application/json",
				},
				body: JSON.stringify({
					text: input.value.trim(),
				}),
			});
			let result = await response.json();
			// console.log(result);
			MainOutputContainer.style.display = "none";
			FilterationSection.style.display = "none";
			ValidationSection.style.display = "none";
			TokenizationSection.style.display = "none";
			LemmetizationSection.style.display = "flex";
			POSTaggingSection.style.display = "none";
			if (!!result.data) {
				if (result.data == "ERROR") {
					LemmetizationSection.innerHTML = `
					<h1>Lemmetization Output</h1>
				<div class="output">Sorry Some Error Occurred</div>
					`;
				} else {
					LemmetizationSection.innerHTML = `
					<h1>Lemmetization Output</h1>
				<div class="output">${result.data}</div>
					`;
				}
			} else {
				window.alert("Some Error occured");
			}
		} catch (error) {
			// console.log(error);
		}
	}
}

async function getPOSTags(event) {
	event.preventDefault();
	if (input.value.trim() == "") {
		window.alert("Please Enter Your Sentiment First");
	} else {
		try {
			let response = await fetch("/postagging", {
				method: "POST",
				headers: {
					"Content-Type": "Application/json",
				},
				body: JSON.stringify({
					text: input.value.trim(),
				}),
			});
			let result = await response.json();
			// console.log(result);
			window.alert("result is fetched and shown below");
			MainOutputContainer.style.display = "none";
			FilterationSection.style.display = "one";
			ValidationSection.style.display = "none";
			TokenizationSection.style.display = "none";
			LemmetizationSection.style.display = "none";
			POSTaggingSection.style.display = "flex";
			if (!!result.data) {
				if (result.data == "ERROR") {
					POSTaggingSection.innerHTML = `
					<h1>POSTagging Output</h1>
					<div class="output">Sorry Some Error Occurred</div>
					`;
				} else {
					POSTaggingSection.innerHTML = `
					<h1>POSTagging Output</h1>
					<div class="output">${result.data}</div>
					`;
				}
			} else {
				window.alert("Some Error occured");
			}
		} catch (error) {
			// console.log(error);
		}
	}
}
