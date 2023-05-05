import { Inter } from 'next/font/google'
import { Card, Col, Row, Button, Text } from "@nextui-org/react";
import pollutionImage from "../public/assets/pollution.png";
import { useEffect, useState } from 'react';

const inter = Inter({ subsets: ['latin'] })

const Card5 = ({ aqi, refetch, isLoading, temp }) => (
  <Card css={{ w: "400px", h: "400px" }}>
    <Card.Header css={{ position: "absolute", zIndex: 1, top: 5 }}>
      <Col>
        <Text size={12} weight="bold" transform="uppercase" color="#eee">
          Air Quality Index
        </Text>
        <Text h3 color="white">
          Get AQI
        </Text>
      </Col>
    </Card.Header>
    <Card.Body css={{ p: 0 }}>
      <Card.Image
        src={pollutionImage.src}
        objectFit="cover"
        width="100%"
        height="100%"
        alt="air quality"
      />
    </Card.Body>

    <Card.Footer css={{ justifyItems: "flex-start", background: "#111111" }}>
      <Row wrap="wrap" justify="space-between" align="center">
        {isLoading ? <Text css={{
          color: "#eeeeee"
        }}>
          Loading....
        </Text> : <Text css={{
          color: "#eeeeee"
        }}>
          Current AQI: {aqi} and Temperature: {temp}°C
        </Text>}
        <Button bordered color="warning" auto onPress={refetch}>
          Refresh
        </Button>
      </Row>
    </Card.Footer>
  </Card>
);

export default function Home() {
  const [aqi, setAqi] = useState(0);
  const [temp, setTemp] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  async function fetchData() {
    try {
      setIsLoading(true)
      const data = await fetch("http://192.168.43.139:8000/api/aqi");
      const jsonData = await data.json();
      setAqi(jsonData.AQI);
      setTemp(jsonData.temp);
      setIsLoading(false);
    }
    catch (e) {
      setIsLoading(false);
      console.log(e);
    }
  }
  useEffect(() => {
    fetchData();
  }, [])
  return (
    <div style={{
      width: "100vw",
      height: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      backgroundColor: "#0C0D12"
    }}>
      <Card5 aqi={aqi} refetch={fetchData} isLoading={isLoading} temp={temp} />
    </div>
  )
}
