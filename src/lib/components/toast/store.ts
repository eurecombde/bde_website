import {writable} from 'svelte/store'

export enum ToastType {
    SUCCESS = 'success',
    INFO = 'info',
    ERROR = 'error',
}

export type Toast = {
    id: number,
    message: string,
    type: ToastType,
    dismissible: boolean,
    timeout: number,
}

export type ToastParameters = {
    message: string,
    type: ToastType,
    dismissible: boolean,
    timeout: number,
}

export const toasts = writable<Toast[]>([])


export const dismissToast = (id: number) => {
    toasts.update((all: Toast[]) => all.filter((t: Toast) => t.id !== id))
}

export const addToast = (toast: ToastParameters) => {
    // Create a unique ID so we can easily find/remove it
    // if it is dismissible/has a timeout.
    const id = Math.floor(Math.random() * 10000)

    // Setup some sensible defaults for a toast.
    const t: Toast = Object.assign({
        id,
        type: ToastType.INFO,
        dismissible: true,
        timeout: 3000,
    }, toast);

    // Push the toast to the top of the list of toasts
    toasts.update((all: Toast[]) => [t, ...all])

    // If toast is dismissible, dismiss it after "timeout" amount of time.
    if (t.timeout) setTimeout(() => dismissToast(id), t.timeout)
}
