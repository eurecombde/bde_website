<script context="module">
    import {fly} from 'svelte/transition';
    import {clubs} from '$lib/constants/clubs';
    import {page} from '$app/stores';

    const categories = Array.from(new Set(clubs.map((club) => club.category)));
</script>

<script>
    $: filter = ($page.url.hash.length > 0 ? $page.url.hash.replace("#", "") : "featured").toLowerCase();
    $: filteredClubs = filter === "all" ? clubs : clubs.filter((club) => club.category.name.toLowerCase() === filter.toLowerCase() || (filter === "featured" && club.featured));
</script>

<section in:fly={{y: 100 ,duration: 250, delay:250}} out:fly={{y: 100 ,duration: 250}} id>
    <div class="container px-6 py-12 mx-auto">
        <h1 class="text-2xl font-semibold text-gray-800 lg:text-4xl dark:text-white">Clubs</h1>
        <div class="mt-8 xl:mt-16 lg:flex lg:-mx-12">
            <div class="lg:mx-12">
                <h1 class="text-xl font-semibold text-gray-800 dark:text-white">Categories</h1>

                <div class="mt-4 space-y-4 lg:mt-8">
                    <a href="#all" class="pl-6 block hover:underline text-gray-500 dark:text-gray-300"
                       class:text-blue-500={filter==="all"} class:dark:text-blue-400={filter==="all"}>
                        All
                    </a>
                    <a href="#featured" class="block hover:underline text-gray-500 dark:text-gray-300"
                       class:text-blue-500={filter==="featured"} class:dark:text-blue-400={filter==="featured"}>
                        ⭐️ Featured
                    </a>
                    {#each categories as category}
                        <a href="#{category.name.toLowerCase()}" class="block text-gray-500 dark:text-gray-300 hover:underline"
                           class:text-blue-500={filter===category.name.toLowerCase()} class:dark:text-blue-500={filter===category.name.toLowerCase()}>
                            {category.emoji} {category.name}
                        </a>
                    {/each}
                </div>
            </div>

            <div class="flex-1 mt-8 lg:mx-12 lg:mt-0">
                <div class="grid grid-cols-1 gap-8 md:grid-cols-2 xl:grid-cols-3 ">
                    {#each filteredClubs as club, index}
                        <div in:fly={{ x: 100, duration: 250, delay: 250+ index * 100}} id={club.name}>
                            {#if club.photo}
                                <img class="object-cover w-full rounded-lg h-52" alt={club.name}
                                     src={club.photo}>
                            {:else }
                                <img class="object-cover w-full rounded-lg h-52" alt={club.name}
                                     src="https://source.unsplash.com/1080x720/?{club.name.replace(' ', '-')}">
                            {/if}
                            <div class="flex row items-baseline w-full justify-between">
                                <h2 class="mt-4 text-2xl font-semibold text-gray-800 capitalize dark:text-white">{club.name}</h2>
                                <p class="mb-2 text-gray-600 dark:text-gray-300">{club.category.name} {club.category.emoji}</p>
                            </div>
                            {#if club.groupLink}
                                <a href="" class="mt-2 text-lg tracking-wider text-blue-500 dark:text-blue-400 "> See more</a>
                            {/if}
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    </div>
</section>
