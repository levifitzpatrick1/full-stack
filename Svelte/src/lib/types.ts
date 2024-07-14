import { writable } from "svelte/store";

export interface UserData {
    username: string;
    photo: string;
    items: ItemData[]
}

export const userData = writable<UserData | null>(null);

export interface ItemData {
    id: string;
    item_name: string;
    description?: string;
    barcode: string;
    item_link: string;
    created_at: Date;
  }

  export const ItemData = writable<ItemData | null>(null)