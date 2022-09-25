<script>
    import {fade, fly} from 'svelte/transition';
    import {headers} from '$lib/constants/photos';

    export let events = [];
    let page = 0;

    function goto(index) {
        page = Math.abs(index) % headers.length;
    }

    $: current = headers[page];
</script>


<header in:fly={{y: 100 ,duration: 250 , delay:250}} out:fly={{y: 100 ,duration: 250}}>
    <div class="container flex flex-col px-6 py-4 mx-auto space-y-6 lg:h-[32rem] lg:py-16 lg:flex-row lg:items-center">
        <div class="flex flex-col items-center w-full lg:flex-row lg:w-1/2">
            {#if headers.length > 1}
                <div class="flex justify-center order-2 mt-6 lg:mt-0 lg:space-y-3 lg:flex-col">
                    {#each headers as _, i}
                        <button class="w-3 h-3 mx-2 rounded-full lg:mx-0 focus:outline-none"
                                class:bg-blue-500={page === i}
                                class:bg-blue-200={page !== i}
                                transition:fade
                                on:click={() => goto(i)}></button>
                    {/each}
                </div>
            {/if}
            <div class="max-w-lg lg:mx-12 lg:order-2">
                <h1 class="text-3xl font-medium tracking-wide text-gray-800 dark:text-white lg:text-4xl">EURECOMs Student Association</h1>
                <p class="mt-4 text-gray-600 dark:text-gray-300">
                    We are working on this website and we will post clubs, frequently asked questions and more shortly.
                </p>
                {#if events.length > 0}
                    <div class="mt-6">
                        <a href="#events" class="bg-transparent mr-auto text-black-300 hover:text-white rounded shadow hover:shadow-lg py-2 px-4 border border-black-300 hover:border-black hover:bg-black">
                            See what's happening
                        </a>
                    </div>
                {/if}
            </div>
        </div>

        <div class="flex items-center justify-center w-full h-96 lg:w-1/2">
            <img class="object-cover w-full h-full max-w-2xl rounded-md"
                 transition:fade
                 src={current}/>
        </div>
    </div>
</header>
