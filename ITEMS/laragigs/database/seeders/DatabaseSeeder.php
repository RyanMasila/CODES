<?php

namespace Database\Seeders;

use App\Models\Listing;
use App\Models\User;
// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        // User::factory(10)->create();

        // User::factory()->create([
        //     'name' => 'Test User',
        //     'email' => 'test@example.com',
        // ]);

        $user = User::factory()->create([
            'name' => 'Ryan Masila',
            'email' => 'ryanmasila12@gmail.com'
        ]);

        Listing::factory(6)->create([
            'user_id' => $user->id
        ]);

        // Listing::create([
        //     'title' => 'Laravel Senior Developer',
        //     'tags' => 'laravel, javascript',
        //     'company' => 'Acme Corp',
        //     'location' => 'Boston, MA',
        //     'email' => 'ryanmasila12@gmail.com',
        //     'website' => 'https://www.acme.com',
        //     'description' => 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus et asperiores quas reiciendis rem optio, dolorem ipsam atque, officiis voluptatibus non obcaecati provident laudantium esse. Reiciendis, blanditiis? Libero, vitae. Aut!'
        // ]);

        // Listing::create([
        //     'title' => 'Full-Stack Engineering',
        //     'tags' => 'laravel, backend, api',
        //     'company' => 'Stark Industries',
        //     'location' => 'New York, NY',
        //     'email' => 'ryanmasila13@gmail.com',
        //     'website' => 'https://www.starkindustries.com',
        //     'description' => 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus et asperiores quas reiciendis rem optio, dolorem ipsam atque, officiis voluptatibus non obcaecati provident laudantium esse. Reiciendis, blanditiis? Libero, vitae. Aut!'
        // ]);
    }
}
