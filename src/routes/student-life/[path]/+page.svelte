<script>
    import Markdown from 'svelte-markdown';

    export let data;
</script>


<h1>{data.name}</h1>

<!--todo: breadcrums-->
<!--todo: history of edits-->
<!--todo: -->
<!--{#each history as commit}-->
<!--    <p>{commit.author.name}</p>-->
<!--    <p>{commit.author.date}</p>-->
<!--{/each}-->

<Markdown source={data.content}/>
