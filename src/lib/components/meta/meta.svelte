<script>
    import { defaultMeta, metaOf } from "$lib/components/meta/meta";
    export let meta = defaultMeta;
    console.log(meta);
</script>

<!-- 
<meta property="og:type" content="information"/>
<meta property="og:title" content="EURECOM BDE"/>
<meta property="og:desctiption" content="EURECOM Student Union"/>
<meta property="og:url" content="bde.eurecom.fr"/>
<meta property="og:locale" content="en_FR"/>
<meta property="og:image" content="%sveltekit.assets%/images/logo_black.png"/>
<meta property="og:image:secure_url" content="%sveltekit.assets%/images/logo_black.png"/>
<meta property="og:image:width" content="3508"/>
<meta property="og:image:height" content="2480"/>
<meta property="og:image:alt" content="BedRocksv     Logo"/> -->
<svelte:head>
    <link rel="icon" href={meta.icon} />
    <meta property="og:locale" content={meta.locale} />
    <meta property="og:type" content={meta.type} />
    <meta property="og:title" content={meta.title} />
    <meta property="og:desctiption" content={meta.description} />
    <meta property="og:url" content={meta.url} />
    <meta property="og:image" content={meta.image.url} />
    <meta property="og:image:secure_url" content={meta.image.url} />
    <!-- <meta property="og:image:width" content="3508"/> -->
    <!-- <meta property="og:image:height" content="2480"/> -->
    <meta property="og:image:alt" content={meta.image.alt} />


  <!-- HTML Meta Tags -->
  <!-- <title>EURECOM BDE</title> -->
  <!-- <meta name="description" content="undefined"> -->

  <!-- Facebook Meta Tags -->
  <!-- <meta property="og:url" content="https://bde.eurecom.fr">
  <meta property="og:type" content="website">
  <meta property="og:title" content="EURECOM BDE">
  <meta property="og:description" content="undefined">
  <meta property="og:image" content="https://bde.eurecom.fr./images/logo_black.png"> -->

  <!-- Twitter Meta Tags -->
  <meta name="twitter:card" content={meta.image.url}>
  <meta property="twitter:domain" content={meta.domain}>
  <meta property="twitter:url" content={meta.url}>
  <meta name="twitter:title" content="EURECOM BDE">
  <meta name="twitter:description" content={meta.description}>
  <meta name="twitter:image" content={meta.image.url}>
</svelte:head>
