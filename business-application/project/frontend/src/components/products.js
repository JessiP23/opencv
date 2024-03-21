import React, {useState} from 'react';

const AddProduct = ({ onAddProduct }) => {
    const [productName, setProductName] = useState('');

    const handleAddProduct = () => {
        onAddProduct(productName);
        setProductName('');
    };

    return (
        <div>
            <input
                type='text'
                placeholder='Enter product name'
                value={productName}
                onChange={(e) => setProductName(e.target.value)}
            />
            <button onClick={handleAddProduct}>Add Product</button>
        </div>
    );
};

export default AddProduct;


