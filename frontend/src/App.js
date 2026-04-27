import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  PieChart,
  Pie,
  Tooltip,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend
} from "recharts";

function App() {
  const [cityData, setCityData] = useState([]);
  const [categoryData, setCategoryData] = useState([]);
  const [sourceData, setSourceData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const city = await axios.get("http://127.0.0.1:8000/city-wise-count");
    const category = await axios.get("http://127.0.0.1:8000/category-wise-count");
    const source = await axios.get("http://127.0.0.1:8000/source-wise-count");

    setCityData(city.data);
    setCategoryData(category.data);
    setSourceData(source.data);
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>Business Listings Dashboard</h1>

      <h2>City-wise Count</h2>
      <BarChart width={700} height={300} data={cityData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="city" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="count" />
      </BarChart>

      <h2>Category-wise Count</h2>
      <PieChart width={500} height={300}>
        <Pie
          data={categoryData}
          dataKey="count"
          nameKey="category"
        />
        <Tooltip />
      </PieChart>

      <h2>Source-wise Count</h2>
      <PieChart width={500} height={300}>
        <Pie
          data={sourceData}
          dataKey="count"
          nameKey="source"
        />
        <Tooltip />
      </PieChart>
    </div>
  );
}

export default App;