<script>
    import {fade} from 'svelte/transition';
</script>


<header in:fade out:fade>
    <div class="container flex flex-col px-6 py-4 mx-auto space-y-6 lg:h-[32rem] lg:py-16 lg:flex-row lg:items-center">
        <div class="flex flex-col items-center w-full lg:flex-row lg:w-1/2">
            <div class="flex justify-center order-2 mt-6 lg:mt-0 lg:space-y-3 lg:flex-col">
                <button class="w-3 h-3 mx-2 bg-blue-500 rounded-full lg:mx-0 focus:outline-none"></button>
                <button class="w-3 h-3 mx-2 bg-gray-300 rounded-full lg:mx-0 focus:outline-none hover:bg-blue-500"></button>
                <button class="w-3 h-3 mx-2 bg-gray-300 rounded-full lg:mx-0 focus:outline-none hover:bg-blue-500"></button>
                <button class="w-3 h-3 mx-2 bg-gray-300 rounded-full lg:mx-0 focus:outline-none hover:bg-blue-500"></button>
            </div>

            <div class="max-w-lg lg:mx-12 lg:order-2">
                <h1 class="text-3xl font-medium tracking-wide text-gray-800 dark:text-white lg:text-4xl">The best a student can get</h1>
                <p class="mt-4 text-gray-600 dark:text-gray-300">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aut quia asperiores alias vero magnam recusandae adipisci ad vitae laudantium quod rem voluptatem eos accusantium cumque.</p>
                <div class="mt-6">
                    <a href="#events" class="bg-transparent mr-auto text-black-300 hover:text-white rounded shadow hover:shadow-lg py-2 px-4 border border-black-300 hover:border-black hover:bg-black">
                        See what's happening
                    </a>
                </div>
            </div>
        </div>

        <div class="flex items-center justify-center w-full h-96 lg:w-1/2">
            <img class="object-cover w-full h-full max-w-2xl rounded-md" src="images/hero1.jpeg" alt="apple watch photo">
        </div>
    </div>
</header>
