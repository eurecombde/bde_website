<script>
    import Team from "$lib/sections/team.svelte";
    import Contact from "$lib/sections/contact.svelte";
    import Partners from "$lib/sections/partners.svelte";
    import Meta from "$lib/components/meta/meta.svelte";
    import { metaOf } from "$lib/components/meta/meta";

    const meta = metaOf({
        title: "About us",
        image: { url: "/images/hero1.jpg", alt: "Photo of the team" },
        description:
            "We are all here doing our best to help make our student life the best we can." +
            "If there is something you are wondering about, feel free to ask here or any of our members 😊",
    });
</script>

<Meta {meta} />
<!--About us-->
<!--What the BDE does-->
<!--Big events the BDE organises-->
<Team />
<Partners />
<Contact />
