<script>
    import Icon from 'svelte-awesome';
    import {createEventDispatcher} from 'svelte'
    import {close, check, stop, info} from 'svelte-awesome/icons';
    import {fade, fly} from 'svelte/transition'
    import {ToastType} from './store';
    const dispatch = createEventDispatcher()

    export let type = 'error'
    export let dismissible = true
</script>

<article class={type} role="alert" transition:fly={{y: -200, duration: 300}}>
    {#if type === ToastType.SUCCESS}
        <Icon data={check}/>
    {:else if type === ToastType.ERROR}
        <Icon data={stop}/>
    {:else if type === ToastType.INFO}
        <Icon data={info}/>
    {/if}

    <div class="text">
        <slot/>
    </div>

    {#if dismissible}
        <button class="close" on:click={() => dispatch('dismiss')}>
            <Icon data={close}/>
        </button>
    {/if}
</article>

<style lang="postcss">
    article {
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 0.2rem;
        display: flex;
        align-items: center;
        margin: 0 auto 0.5rem auto;
        width: 20rem;
    }

    .error {
        background: IndianRed;
    }

    .success {
        background: MediumSeaGreen;
    }

    .info {
        background: SkyBlue;
    }

    .text {
        margin-left: 1rem;
    }

    button {
        color: white;
        background: transparent;
        border: 0 none;
        padding: 0;
        margin: 0 0 0 auto;
        line-height: 1;
        font-size: 1rem;
    }
</style>
