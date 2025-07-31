import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/products') // or your ngrok URL
      .then(res => setProducts(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>All Products</h2>
      <ul>
        {products.map(p => (
          <li key={p.id}>
            <Link to={`/product/${p.id}`}>{p.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;
