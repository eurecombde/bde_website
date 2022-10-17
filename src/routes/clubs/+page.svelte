<script context="module">
    import {fly, fade} from 'svelte/transition';
    import {clubs} from '$lib/constants/clubs';
    import {page} from '$app/stores';
    import {GOOGLE_MAPS_QUERY} from "$lib/constants/links";
    import Icon from 'svelte-awesome';
    import {whatsapp, facebookSquare} from 'svelte-awesome/icons';

    const categories = Array.from(new Set(clubs.map((club) => club.category)));

</script>

<script>
    import {asDateTime} from "$lib/types/calendar-event";

    export let data;
    const {weekEvents, ical, error} = data;
    const hasEvents = weekEvents.find((event) => event.events.length > 0) !== undefined;
    $: filter = ($page.url.hash.length > 0 ? $page.url.hash.replace("#", "") : "featured").toLowerCase();
    $: filteredClubs = filter === "all" ? clubs : clubs.filter((club) => club.category.name.toLowerCase() === filter.toLowerCase() || (filter === "featured" && club.featured));
</script>


<section in:fly={{y: 100 ,duration: 250, delay:250}} out:fly={{y: 100 ,duration: 250}}>
    <div class="container px-6 pt-12 mx-auto">
        <h1 class="text-3xl font-semibold text-gray-800 lg:text-5xl dark:text-white mb-6">Clubs</h1>
    </div>
</section>

{#if hasEvents}
    <section in:fly={{y: 100 ,duration: 250, delay:250}} out:fly={{y: 100 ,duration: 250}}>
        <div class="container px-6 mx-auto">
            <h2 class="text-2xl font-semibold text-gray-800 lg:text-4xl dark:text-white mb-6">Events</h2>
            <div class="grid md:grid-cols-7 md:grid-flow-col grid-rows-[24px_1fr] grid-flow-row border-gray-400 border-l-2 md:border-l-0">
                {#each weekEvents as day, weekdayIndex}
                    <h1 class="text-left md:text-center text-gray-400 md:border-t-2 border-gray-400 relative py-2 uppercase md:flex-row flex-col">
                        <span class="absolute text-left md:text-center -left-2 md:left-0 md:right-0 md:-top-3.5 text-gray-400">●</span>
                        <span class="md:pl-0 pl-8">{day.name}</span>
                    </h1>

                    <ul class="px-8 pt-2 flex flex-col">
                        {#each day.events as event, eventIndex}
                            <div class="py-2" in:fly={{y: 100, duration: 250, delay: 250 + (weekdayIndex * 100) + (eventIndex * 100)}}>
                                {#if event.time !== null}
                                    <p class="text-base text-300">{asDateTime(event.start).toLocaleTimeString("en-FR", {hour: "2-digit", minute: "2-digit"})}</p>
                                {/if}
                                <h4 class="font-bold text-lg md:text-2xl">{event.summary}</h4>
                                {#if event.description}
                                    <h4 class="text-blue-500 dark:text-blue-400">{event.description}</h4>
                                {/if}
                                {#if event.location}
                                    <a href="{GOOGLE_MAPS_QUERY}{event.location}">
                                        <p class="text-sm md:text-base leading-snug text-gray-500 hover:text-blue-500 mb-3 flex w-full -timeline">
                                            <span>@</span>
                                            <span class="mx-1">{event.location?.split(',')[0]}</span>
                                        </p>
                                    </a>
                                {/if}
                            </div>
                        {/each}
                    </ul>
                {/each}
            </div>
        </div>
    </section>
{/if}

<section in:fly={{y: 100 ,duration: 250, delay:250}} out:fly={{y: 100 ,duration: 250}} id>
    <div class="container px-6 mx-auto">
        <div class="mt-8 lg:flex lg:-mx-12">
            <div class="lg:mx-12">
                <h2 class="text-2xl lg:text-4xl font-semibold text-gray-800 dark:text-white">Categories</h2>

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
                        <div in:fly={{ y: 100, duration: 250, delay: 250+ index * 100}} id={club.name}>
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
                            <p class="mb-2 text-gray-600 dark:text-gray-300">⭐️ {club.president}</p>
                            {#if club.vicePresident}
                                <p class="mb-2 text-gray-600 dark:text-gray-300">✨ {club.vicePresident}</p>
                            {/if}
                            {#if club.facebook}
                                <a href={club.facebook} class="ml-1.5 mt-2 text-lg tracking-wider text-blue-500 dark:text-blue-400">
                                    <Icon data={facebookSquare} class="mb-1 mr-0.5"/>
                                    <span>Join the group</span>
                                </a>
                            {/if}

                            {#if club.whatsapp}
                                <a href={club.whatsapp} class="ml-1.5 mt-2 text-lg tracking-wider text-green-500 dark:text-green-400 flex align-center">
                                    <Icon data={whatsapp} class="mt-1.5 mr-2"/>
                                    <span>Join the chat</span>
                                </a>
                            {/if}
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    </div>
</section>
