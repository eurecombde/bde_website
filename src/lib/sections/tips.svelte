<script>
    import {fade} from 'svelte/transition';
    import {offers} from '$lib/constants/partners';
    import Icon from 'svelte-awesome';
</script>

<section id="tips" in:fade out:fade>
    <div class="container px-6 py-10 mx-auto">
        <h1 class="text-3xl font-semibold text-gray-800 capitalize lg:text-4xl dark:text-white">explore our <span class="underline decoration-blue-500">deals & partners</span></h1>

        <p class="mt-4 text-gray-500 xl:mt-6 dark:text-gray-300">
            Take advantage of the deals and partnerships available for you. If you want to join the list or have a suggestion please do <a href="/about#contact" class="underline text-blue-500">reach out to us</a>
        </p>

        <div class="grid grid-cols-1 gap-8 mt-8 xl:mt-12 xl:gap-12 md:grid-cols-2 xl:grid-cols-3">
            {#each offers as offer}
                <div class="p-8 space-y-3 border-2 border-blue-400 dark:border-blue-300 rounded-xl">
                    <span class="inline-block text-blue-500 dark:text-blue-400">
                        <Icon data={offer.icon}/>
                    </span>

                    <h1 class="text-2xl font-semibold text-gray-700 capitalize dark:text-white">{offer.name}</h1>

                    <p class="text-gray-500 dark:text-gray-300">
                        {offer.description}
                    </p>
                    {#if offer.url}
                        <a href={offer.url} class="inline-flex p-2 text-blue-500 capitalize transition-colors duration-300 transform bg-blue-100 rounded-full rtl:-scale-x-100 dark:bg-blue-500 dark:text-white hover:underline hover:text-blue-600 dark:hover:text-blue-500">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 9l3 3m0 0l-3 3m3-3H8m13 0a9 9 0 11-18 0 9 9 0 0118 0z"/>
                            </svg>
                        </a>
                    {/if}
                </div>
            {/each}
        </div>
    </div>
</section>
