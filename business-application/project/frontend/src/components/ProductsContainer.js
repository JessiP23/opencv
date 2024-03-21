import React, {useState} from 'react';
import ProductList from './ProductList';
import AddProduct from './products';

const ProductContainer = () => {
    const [products, setProducts] = useState([]);

    const handleAddProduct = (productName) => {
        setProducts([...products, productName]);
    };

    return (
        <div>
            <AddProduct onAddProduct={handleAddProduct}/>
            <ProductList products={products}/>
        </div>
    );
};

export default ProductContainer;