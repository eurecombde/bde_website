<script>
    import {INFO} from './alert-types';
    import {fly, fade} from 'svelte/transition';

    export let type = INFO;
</script>


<div class="m-10 flex justify-center" in:fly={{y: -100, duration: 1000}} out:fade>
    <div class="lg:w-1/2 p-4 border rounded justify-center flex {type.classes}" role="alert">
        <strong class="text-sm font-medium">
            {type.emoji}
            <slot/>
            {type.emoji}
        </strong>
    </div>
</div>
