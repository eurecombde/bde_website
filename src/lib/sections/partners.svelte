<script>
    import {partners} from '$lib/constants/partners';
    import {fade} from 'svelte/transition';

</script>

<section id="partners" in:fade out:fade>
    <div class="max-w-screen-xl mx-auto mt-20">
        <h1 class="text-2xl font-semibold text-center text-gray-800 lg:text-4xl dark:text-white mb-10">Our <span class="underline decoration-blue-500">Partners</span></h1>
        <div class="flex justify-center items-center">
            {#each partners as partner}
                <a href={partner.url ?? ""} class="flex items-center justify-center col-span-1 md:col-span-2 lg:col-span-1 grayscale mx-8">
                    <img src={partner.logo} width="120px" height="16px" alt={partner.name}/>
                </a>
            {/each}
            <!--Todo: add other partners-->
        </div>
    </div>
</section>
