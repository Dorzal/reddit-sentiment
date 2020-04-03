import './loader.css'
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css"
import Loader from 'react-loader-spinner'
export default ({
    loading
}) => {
    return (
        <div style={{
            position: "absolute",
            top:0,
            left:0,
            right:0,
            bottom:0,
            backgroundColor: 'rgb(200,200,200,.5)',
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            transition: "all 250ms",
            transform: loading ? "translateY(0)" : "translateY(100%)"
            }}>
            <Loader
            type="Plane"
            color="#673AB7"
            height={100}
            width={100}
            />
        </div>
    )
}