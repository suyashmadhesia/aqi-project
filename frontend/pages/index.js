import { Inter } from 'next/font/google'
import { Card, Col, Row, Button, Text } from "@nextui-org/react";
import pollutionImage from "../public/assets/pollution.png";

const inter = Inter({ subsets: ['latin'] })

const Card5 = () => (
  <Card css={{ w: "400px", h: "400px" }}>
    <Card.Header css={{ position: "absolute", zIndex: 1, top: 5 }}>
      <Col>
        <Text size={12} weight="bold" transform="uppercase" color="#eee">
          Air Quality Index
        </Text>
        <Text h3 color="white">
          Get AQI for your location
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

    <Card.Footer css={{ justifyItems: "flex-start", background :"#111111" }}>
      <Row wrap="wrap" justify="space-between" align="center">
        <Text css={{
          color:"#eeeeee"
        }}>
          Current AQI: 250
        </Text>
        <Button bordered color="warning" auto>
          Refresh
        </Button>
      </Row>
    </Card.Footer>
  </Card>
);

export default function Home() {
  return (
    <div style={{
      width: "100vw",
      height: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      backgroundColor: "#0C0D12"
    }}>
      <Card5 />
    </div>
  )
}
