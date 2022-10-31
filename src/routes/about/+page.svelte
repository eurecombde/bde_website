<script>
    import Team from "$lib/sections/team.svelte";
    import Contact from "$lib/sections/contact.svelte";
    import Partners from "$lib/sections/partners.svelte";
    import Meta from "$lib/components/meta/meta.svelte";
    import { metaOf } from "$lib/components/meta/meta";

    const meta = metaOf({
        title: "About us",
        image: { url: "/images/hero1.jpg", alt: "Photo of the team" },
        description: "Meet the team behind the BDE and learn more about the association.",
    });
</script>

<Meta {meta} />
<!--About us-->
<!--What the BDE does-->
<!--Big events the BDE organises-->
<Team />
<Partners />
<Contact />
