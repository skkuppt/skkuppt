import styles from "./ppt_result.module.css";

const Desktop7 = () => {
  return (
    <div className={styles.desktop7}>
      <div className={styles.login1}>
        <div className={styles.div}>
          <img className={styles.skkuIm1} alt="" src="/skku-im-1@2x.png" />
        </div>
        <input className={styles.component1} placeholder="Detail" />
      </div>
      <div className={styles.component11}>
        <div className={styles.button}>ppt</div>
      </div>
      <div className={styles.component12}>
        <div className={styles.button}>home</div>
      </div>
    </div>
  );
};

export default Desktop7;

