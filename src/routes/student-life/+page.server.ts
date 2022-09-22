export type StudentGuide = {
    name: string,
    path: string,
    download_url: string,
}

export type StudentGuideMetadata = {
    title?: string,
    category?: string,
    summary?: string,
}

class JsonToStudentGuideTransformer {
    transform(json: any): StudentGuide {
        return {
            name: json.name.replace(".md", ""),
            path: json.path.split('/')[1],
            download_url: json.download_url,
        }
    }
}

class TextToStudentGuideMetadataTransformer {
    transform(text: string): StudentGuideMetadata {
        return {
            title: this.extract('title', text),
            category: this.extract('category', text),
            summary: this.extract('summary', text),
        };
    }

    private tagRegex(tag: string): RegExp {
        return new RegExp('\[\/\/\]: # \(' + tag + ': (.*)\)', 'g');
    }

    private extract(tag: string, text: string): string | undefined {
        const matcher = this.tagRegex(tag);
        return text.match(matcher)
            ?.pop()
            ?.replace(matcher, "$1");
    }
}

/** @type {import('./$types').PageServerLoad} */
export async function load(): Promise<{ guides?: { guide: StudentGuide, metadata: StudentGuideMetadata }[], error?: any }> {
    return { guides: []};
}
// export async function load(): Promise<{ guides?: { guide: StudentGuide, metadata: StudentGuideMetadata }[], error?: any }> {
//     const transformer = new JsonToStudentGuideTransformer();
//     const textToMetadataTransformer = new TextToStudentGuideMetadataTransformer();
//     try {
//         const guidesRequest = await fetch("https://api.github.com/repos/eurecombde/student-life/contents/student-guides", {
//             headers: {
//                 "User-Agent": "EURECOM BDE",
//
//             }
//         });
//         const guides = await guidesRequest.json() ?? [];
//         console.log('Got ', guides.length, ' guides');
//         const guidesWithMetadataRequest = await Promise.all(guides.map(async (guide: any) => {
//             const guideRequest = await fetch(guide.download_url);
//             const guideMetadata = await guideRequest.text();
//             const metadata = textToMetadataTransformer.transform(guideMetadata);
//             console.log(metadata);
//             return {
//                 guide: transformer.transform(guide),
//                 metadata: metadata
//             };
//         }));
//
//         return {guides: guidesWithMetadataRequest};
//     } catch
//         (error) {
//         console.error('+page.server#load', 'Github has resturned an error');
//         console.error(error)
//         return {error};
//     }
// }
