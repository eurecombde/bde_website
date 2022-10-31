<script>
  import { defaultMeta, metaOf } from "$lib/components/meta/meta";
  export let meta = defaultMeta;
</script>

<svelte:head>
  <link rel="icon" href={meta.icon} />
  <meta property="og:locale" content={meta.locale} />
  <meta property="og:type" content={meta.type} />
  <meta property="og:title" content={meta.title} />
  <meta property="og:description" content={meta.description} />
  <meta property="og:url" content={meta.url} />
  <meta property="og:image" content={meta.image.url} />
  <meta property="og:image:secure_url" content={meta.image.url} />
  <meta property="og:image:alt" content={meta.image.alt} />

  <!-- Twitter Meta Tags -->
  <meta name="twitter:card" content={meta.image.url} />
  <meta property="twitter:domain" content={meta.domain} />
  <meta property="twitter:url" content={meta.url} />
  <meta name="twitter:title" content="EURECOM BDE" />
  <meta name="twitter:description" content={meta.description} />
  <meta name="twitter:image" content={meta.image.url} /> 
</svelte:head>
