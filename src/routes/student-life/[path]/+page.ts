export const prerender = true;
//
// type Commit = {
//     author: { name: string, email: string, date: string },
//     message: string,
// }
//
// class JsonToCommitTransformer {
//     transform(json: any): Commit {
//         const commit = json.commit;
//         return {
//             author: {name: commit.author.name, email: commit.author.email, date: commit.author.date},
//             message: commit.message,
//         };
//     }
// }
//
// /** @type {import('./$types').PageServerLoad<Promise<{ events:CalendarEvent[], ical: string, error: string}>>} */
// export async function load({params}): Promise<{ source?: string, history?: any, error?: any }> {
//     const transformer = new JsonToCommitTransformer();
//     try {
//         const sanetizedPath = params.path.replace(/[\.\/\\]*/, '');
//         const historyRequest = await fetch("https://api.github.com/repos/eurecombde/Student-Life/commits?path=student-guides/" + sanetizedPath);
//         const sourceRequest = await fetch("https://raw.githubusercontent.com/eurecombde/Student-Life/main/student-guides/" + sanetizedPath);
//
//         const source = await sourceRequest.text()
//         const history = await historyRequest.json()
//         console.log(sanetizedPath, source, history.map(transformer.transform));
//
//         return {source, history: history.map(transformer.transform)};
//     } catch (error) {
//         console.error('+page.server#load', 'Github returned an error');
//         console.error(error)
//         return {error};
//     }
// }
import {guides} from '$lib/constants/student-guides';
import type {Guide} from '$lib/constants/student-guides';

/** @type {import('./$types').PageLoad} */
export async function load({params}): Guide {
    const guide = guides.find(guide => guide.slug === params.path);
    if (!guide) throw Error("No guide found");
    guide.content = guide.content.replace(/\n */, "\n")
    return guide;
}
