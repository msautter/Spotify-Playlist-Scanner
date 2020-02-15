import { getPlaylists } from "./spotify/playlists";
import { printTable } from "./utils/output";
import { resolve } from "path";
import { TEST_TOKEN } from "./utils/env";

const term = "memes";

getPlaylists(term, TEST_TOKEN, 50)
    .then(playlists =>
        playlists.map((playlist: any, index : number) => ({
            "#" : index +1,
            total: playlist.tracks.total,
            name: playlist.name,
            desc: playlist.description,
            url: playlist.href,
        }))
    ).then(playlists => printTable(["#", "name", "total", "desc"], playlists)
    ).catch(err => console.log(err));