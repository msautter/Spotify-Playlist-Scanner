import { getPlaylists } from "./spotify/playlists";
import { getTracks}  from "./spotify/tracks";
import { stripEmojies } from "./utils/strippers";
import { TEST_TOKEN as token } from "./utils/env";
import { table } from "table";


let playlistTable = [[ "#", "name", "total", "desc"]];

getPlaylists("memes", token, 10)
  .then(playlists =>
    playlists.map((item: any, index : number) => {
        let total = item.tracks.total;
        let name = String(stripEmojies(item.name)).substr(0,60);
        let desc = String(stripEmojies(item.description)).substr(0,80);
        let url = item.href;
        playlistTable.push([index+1, name, total, desc])
        return {
            total : total,
            name : name,
            desc : desc,
            url : url
        }
    }
     
    )
  )
  .then((playlists) => {
      console.log(table(playlistTable))

      playlists.forEach((playlist : any) => {
        getTracks(playlist.url, token)
      })
    }).catch(err => console.log(err));


//     id : item.id,
//     url : item.href,
//     name : item.name,
//     length : item.tracks.total
// ]
