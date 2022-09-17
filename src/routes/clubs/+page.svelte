<script>
    import {fade} from 'svelte/transition';
    import {clubs} from '$lib/constants/clubs';
    import {page} from '$app/stores';

    const id = "list"
    const categories = Array.from(new Set(clubs.map((club) => club.category)));

    $: filter = ($page.url.hash.length > 0 ? $page.url.hash.replace("#", "") : "featured").toLowerCase();
    $: filteredClubs = filter === "all" ? clubs : clubs.filter((club) => club.category.name.toLowerCase() === filter.toLowerCase() || (filter === "featured" && club.featured));
</script>

<section in:fade out:fade id>
    <div class="container px-6 py-12 mx-auto">
        <h1 class="text-2xl font-semibold text-gray-800 lg:text-4xl dark:text-white">Clubs</h1>
        <div class="mt-8 xl:mt-16 lg:flex lg:-mx-12">
            <div class="lg:mx-12">
                <h1 class="text-xl font-semibold text-gray-800 dark:text-white">Categories</h1>

                <div class="mt-4 space-y-4 lg:mt-8">
                    <a href="#all" class="pl-6 block hover:underline text-gray-500 dark:text-gray-300"
                       class:text-blue-500={filter==="all"}
                       class:dark:text-blue-400={filter==="all"}>
                        All
                    </a>
                    <a href="#featured" class="block hover:underline text-gray-500 dark:text-gray-300"
                       class:text-blue-500={filter==="featured"}
                       class:dark:text-blue-400={filter==="featured"}>
                        ⭐️ Featured
                    </a>
                    {#each categories as category}
                        <a href="#{category.name.toLowerCase()}"
                           class="block text-gray-500 dark:text-gray-300 hover:underline"
                           class:text-blue-500={filter===category.name.toLowerCase()}
                           class:dark:text-blue-500={filter===category.name.toLowerCase()}>
                            {category.emoji} {category.name}</a>
                    {/each}
                </div>
            </div>

            <div class="flex-1 mt-8 lg:mx-12 lg:mt-0">
                <div class="grid grid-cols-1 gap-8 md:grid-cols-2 xl:grid-cols-3 ">
                    {#each filteredClubs as club}
                        <div in:fade out:fade id={club.name}>
                            {#if club.photo}
                                <img class="object-cover w-full rounded-lg h-96 "
                                     src="https://images.unsplash.com/photo-1621111848501-8d3634f82336?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1565&q=80"
                                     alt="">
                            {/if}
                            <h2 class="mt-4 text-2xl font-semibold text-gray-800 capitalize dark:text-white">{club.name}</h2>
                            <p class="mt-2 text-lg tracking-wider text-blue-500 uppercase dark:text-blue-400 ">Club Group</p>
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    </div>
</section>
