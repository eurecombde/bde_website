import { ChangeFrequency, type Page, type Section } from '$lib/constants/routes';
import { routes, domain } from '$lib/constants/routes';


export function GET() {
    function httpsOf(path: string, tag?: string): string {
        return `https://${domain}${path}${tag ?? ''}`;
    }

    function sitemapOf(resource: Page | Section): string {
        return `
        <priority>${resource.priorty ?? 0}</priority>
        <changefreq>${(resource.changefequency ?? ChangeFrequency.NEVER).toString()}</changefreq>
        `;
    }

    function urlOf(page: Page) {
        return `
        <url>
            <loc>${httpsOf(page.path)}</loc>
            ${sitemapOf(page)}
        </url>
        ` + page.sections?.map(section => `
        <url>
            <loc>${httpsOf(page.path, section.tag)}</loc>
            ${sitemapOf(section)}
        </url>
        `);
    };


    return new Response(
        `<?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            ${routes.map(urlOf).join('')}
        </urlset>
        `,
        {
            headers: {
                "Cache-Control": `max-age=0, s-max-age=${600}`,
                "Content-Type": "application/xml"
            },
        });
}