<script>
    const ACTIVE_ROUTE_STYLE = "text-gray-800 dark:text-gray-200 border-b-2 border-blue-500 mx-1.5 sm:mx-6";
    const INACTIVE_ROUTE_STYLE = "border-b-2 border-transparent hover:text-gray-800 dark:hover:text-gray-200 hover:border-blue-500 mx-1.5 sm:mx-6";

    import "../app.css";
    import {page} from '$app/stores';
    import Icon from 'svelte-awesome';
    import {facebookSquare, instagram} from 'svelte-awesome/icons';
    import {routes} from '$lib/constants/routes';
    import {contact} from '$lib/constants/team';

    $: activePath = $page.url.pathname;
    $: activeRoute = routes.find((route) => route.path === activePath);
    $: title = activeRoute ?  `${contact.brand} | ${activeRoute.name} ${activeRoute.emoji ?? ''}`: contact.brand;

</script>

<svelte:head>
    <title>{title}</title>
</svelte:head>

<nav>
    <div class="container p-6 mx-auto">
        <a class="block text-2xl font-bold text-center text-gray-800 dark:text-white lg:text-3xl hover:text-gray-700 dark:hover:text-gray-300" href="/">BEDrock @ EURECOM</a>
        <div class="flex items-center justify-center mt-6 text-gray-600 capitalize dark:text-gray-300">
            {#each routes as route}
                <a class="{route.path === activePath ? ACTIVE_ROUTE_STYLE : INACTIVE_ROUTE_STYLE}" href={route.path}>{route.name}</a>
            {/each}

            {#each contact.socials as social}
                <a href={social.url} class="border-b-2 border-transparent hover:text-gray-800 dark:hover:text-gray-200 hover:border-blue-500 mx-1.5 sm:mx-6">
                    <Icon data={social.icon}/>
                </a>
            {/each}
        </div>
    </div>
</nav>

<slot/>

<footer>
    <div class="container p-6 mx-auto">
        <div class="lg:flex">
            <div class="w-full -mx-6 lg:w-2/5">
                <div class="px-6">
                    <div>
                        <a href="/" class="text-xl font-bold text-gray-800 dark:text-white hover:text-gray-700 dark:hover:text-gray-300">{contact.brand}</a>
                    </div>

                    <p class="max-w-sm mt-2 text-gray-500 dark:text-gray-400">{contact.tagline}</p>

                    <div class="flex mt-6 -mx-2">
                        {#each contact.socials as social}
                            <a href={social.url}
                               class="mx-2 text-gray-600 transition-colors duration-300 dark:text-gray-300 hover:text-blue-500 dark:hover:text-blue-400"
                               aria-label={social.name}>
                                <Icon data={social.icon}/>
                            </a>
                        {/each}
                    </div>
                </div>
            </div>

            <div class="mt-6 lg:mt-0 lg:flex-1">
                <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
                    {#each routes as route}
                        <div>
                            <a href={route.path}><h3 class="text-gray-700 uppercase dark:text-white">{route.name}</h3></a>
                            {#if route.sections}
                                {#each route.sections as section}
                                    <a href={route.path + section.tag} class="block mt-2 text-sm text-gray-600 dark:text-gray-400 hover:underline">{section.name}</a>
                                {/each}
                            {/if}
                        </div>
                    {/each}
                </div>
            </div>
        </div>

        <hr class="h-px my-6 bg-gray-200 border-none dark:bg-gray-700">

        <div>
            <p class="text-center text-gray-500 dark:text-gray-400">© Brand 2020 - All rights reserved</p>
        </div>
    </div>
</footer>
