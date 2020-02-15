import { table } from "table";

export const getTable = (headers: string[], objArr: any[], numbered : boolean) => [headers, ...objArr.map(obj => headers.map(header => String(obj[header]).substr(0,70)))]

export const printTable = (headers: string[], objArr: any[]) => console.log(table([headers, ...objArr.map(obj => headers.map(header => String(obj[header]).substr(0,70)))]))

