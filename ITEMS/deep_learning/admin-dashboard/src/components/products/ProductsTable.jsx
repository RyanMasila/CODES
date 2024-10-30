import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Edit, Search, Trash } from 'lucide-react';

const PRODUCT_DATA = [
	{ id: 1, name: "Wireless Earbuds", category: "Electronics", price: 59.99, stock: 143, sales: 1200 },
	{ id: 2, name: "Leather Wallet", category: "Accessories", price: 39.99, stock: 89, sales: 800 },
	{ id: 3, name: "Smart Watch", category: "Electronics", price: 199.99, stock: 56, sales: 650 },
	{ id: 4, name: "Yoga Mat", category: "Fitness", price: 29.99, stock: 210, sales: 950 },
	{ id: 5, name: "Coffee Maker", category: "Home", price: 79.99, stock: 78, sales: 720 },
];

const ProductTable = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredProducts, setFilteredProducts] = useState(PRODUCT_DATA);

  const handleSearch = (e) => {
    const term = e.target.value.toLowerCase();
    setSearchTerm(term);
    const filtered = PRODUCT_DATA.filter(product => product.name.toLowerCase().includes(term) || product.category.toLowerCase().includes(term));

    setFilteredProducts(filtered);
  }
  return (
    <motion.div
    className='bg-gray-800 bg-opacity-50 backdrop-blur-md shadow-lg rounded-xl p-6 border border-gray-700 mb-8'
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ delay: 0.2 }}
  >
    <div className='flex justify-between items-center mb-6'>
      <h2 className='text-xl font-semibold text-gray-100'>Product List</h2>
      <div className='relative'>
        <input type='text'
          placeholder='Search Products...'
          className='bg-gray-700 text-white placeholder-gray-400 rounded-lg pl-10 pr-4 py-2 focus:outline-none
          focus:ring-2 focus:ring-blue-500'
          onChange={handleSearch}
        />
        <Search className='absolute left-3 top-2.5 text-gray-400' size={18}/>
      </div>
    </div>
    <div className='overflow-x-auto'>
      <table className='min-w-full divide-y divide-gray-700'>
        <thead>
          <tr>
            <th
              className='px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider'
            >
              Name
            </th>
            <th
              className='px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider'
            >
              Category
            </th>
            <th
              className='px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider'
            >
              Price
            </th>
            <th
              className='px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider'
            >
              Stock
            </th>
            <th
              className='px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider'
            >
              Sales
            </th>
            <th
              className='px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider'
            >
              Actions
            </th>
          </tr>
        </thead>

        <tbody className='divide-y divide-gray-700'>
          {filteredProducts.map(product => (
            <motion.tr key={product.id}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.3 }}
            >
              <td className='px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-100 flex gap-2 item-center'>
                <img
                  src='data:image/jpeg;base64,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'
                  alt='Product img'
                  className='size-10 rounded-full'
                />
                {product.name}
              </td>
              <td className='px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-300'>
                {product.category}
              </td>
              <td className='px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-300'>
                {product.price.toFixed(2)}
              </td>
              <td className='px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-300'>
                {product.stock}
              </td>
              <td className='px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-300'>
                {product.sales}
              </td>
              <td className='px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-300'>
                <button className='text-indigo-400 hover:text-indigo-300 mr-2'>
                  <Edit size={18}/>
                </button>
                <button className='text-red-400 hover:text-red-300'>
                  <Trash size={18}/>
                </button>
              </td>
            </motion.tr>
          ))}
        </tbody>
      </table>
    </div>
  </motion.div>
  )
}

export default ProductTable