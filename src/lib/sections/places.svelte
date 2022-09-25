<script>
    import {Icon} from 'svelte-awesome';
    import {tripadvisor} from 'svelte-awesome/icons';
    import {fade, fly} from 'svelte/transition';
    import {places} from '$lib/constants/places';

    let page = 0;

    function next() {
        page = (page + 1) % places.length;
    }

    function previous() {
        page = Math.abs(page - 1) % places.length;
    }

    $: currentPlace = places[page];
</script>

<section id="places" in:fade out:fade>
    <div class="relative flex">
        <div class="min-h-screen lg:w-1/3"></div>
        <div class="hidden w-3/4 min-h-screen bg-gray-100 dark:bg-gray-800 lg:block"></div>

        <div class="container flex flex-col justify-center w-full min-h-screen px-6 py-10 mx-auto lg:absolute lg:inset-x-0">
            <h1 class="text-3xl font-semibold text-gray-800 capitalize lg:text-4xl xl:text-5xl dark:text-white">
                Places <span class="text-blue-500">in the area</span> we think are <br> worth seeing
            </h1>


            <div class="mt-10 lg:mt-20 lg:flex lg:items-center" id="place{page}">
                <img class="object-cover object-center w-full lg:w-[32rem] rounded-lg h-96" src={currentPlace.photo} alt="Jardin Exotique d'Èze">
                <div class="mt-8 lg:px-10 lg:mt-0">
                    <h1 class="text-2xl font-semibold text-gray-800 dark:text-white lg:w-72">
                        {currentPlace.name}
                    </h1>

                    <p class="max-w-lg mt-6 text-gray-500 dark:text-gray-400">{currentPlace.description}</p>
                    {#if currentPlace.tripadvisor}
                        <a href="{currentPlace.tripadvsor}">

                            <h3 class="mt-6 text-lg font-medium text-gray-800 dark:text-white">
                                <Icon data={tripadvisor}/>
                                Tripadvisor
                            </h3>
                        </a>
                    {/if}
                </div>
            </div>
            {#if places.length > 1}
                <div class="flex items-center justify-between mt-12 lg:justify-start">
                    <button class="p-2 text-gray-800 transition-colors duration-300 border rounded-full rtl:-scale-x-100 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800 hover:bg-gray-100"
                            on:click={previous}>
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"/>
                        </svg>
                    </button>

                    <button class="p-2 text-gray-800 transition-colors duration-300 border rounded-full rtl:-scale-x-100 dark:border-gray-700 dark:text-gray-200 dark:hover:bg-gray-800 lg:mx-6 hover:bg-gray-100"
                            on:click={next}>
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/>
                        </svg>
                    </button>
                </div>
            {/if}
        </div>
    </div>
</section>
