<?php

use App\Http\Controllers\ListingController;
use App\Http\Controllers\UserController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Models\Listing;

// gig = listing = job
// All Listings
Route::get('/', [ListingController::class, 'index']);

// Single Listing
// Route::get('listings/{id}', function($id) {
//     return view('listing', [
//         'listing' => Listing::find($id)
//     ]);
// });

// Show Create Form
Route::get('/listings/create', [ListingController::class, 'create'])->middleware('auth');

// Store Listing data
Route::post('/listings', [ListingController::class, 'store'])->middleware('auth');

// Manage Listings
Route::get('/listings/manage', [ListingController::class, 'manage'])->middleware('auth');

// Single Listing
Route::get('/listings/{listing}', [ListingController::class, 'show']);


// Show Edit Form
Route::get('/listings/{listing}/edit', [ListingController::class, 'edit'])->middleware('auth');

// delete listings
Route::delete('/listings/{listing}', [ListingController::class, 'destroy'])->middleware('auth');


// Update listings
Route::put('/listings/{listing}', [ListingController::class, 'update'])->middleware('auth');

// Show Register/Create Form
Route::get('/register', [UserController::class, 'create'])->middleware('guest');

// Create New User
Route::post('/users', [UserController::class, 'store']);

// Log User Out
Route::post('/logout', [UserController::class, 'logout'])->middleware('auth');

// Show Login Form
Route::get('/login', [UserController::class, 'login'])->name('login')->middleware('guest');

// Log In User
Route::post('/users/authenticate', [UserController::class, 'authenticate']);


// Route::get('/hello', function() {
    //     return response("<h1>Hello World</h1>", 200)
    //     ->header("Content-Type", "text/plain")
//     ->header("foo", "bar");
// });

// Route::get("/posts/{id}", function ($id) {
//     // dd($id); // die and dump
//     // ddd($id); // die dump and debug
//     return response("Post " . $id);
// })->where("id", '[0-9]+'); // Constraint

// Route::get('/post', function() {
//     return response()->json([
//         'posts' => [
//             [
//                 'title' => 'Post One'
//             ]
//         ]
//         ]);
// });

// Route::get("/search", function(Request $request) {
//     dd($request->name. ' '.$request->city);
// });
