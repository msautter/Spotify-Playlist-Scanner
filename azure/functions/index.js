const axios = require("axios");
const https = require("https");

const agent = new https.Agent({  
  rejectUnauthorized: false
});

axios({
    method : "GET",
    url : `https://api.spotify.com/v1/search?q=memes&type=playlist`,
    headers : {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : `Bearer BQDvhSd1PF14l9go6ssRW5zUwOvnVeYJ9cUzQmg7vgXh5y7BP0mtJWqC61bxMNyD8arBvQBodI7opfyyEJ8jvnFz22JEHWSXK5pd2hWPhB_jLvGjroSto3ZfymYNPpgBvC2BbQyAL0Ez0J7AngWvR0-LU4jBNEyYp1DnAvgNlCnVjjYEYArxWxVBi7Ycl1aa2bX07o2y8ocbxcgO1hv0Kn5HMqB2bPBju1gBtDvmEoeqE8c73y9cLWb6ZCGA4XC2zLwjE6kLDIgCVF4Z`
    },
    httpsAgent : agent
}).then(data => console.log(data))
.catch(err => console.log(err))