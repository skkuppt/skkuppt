import { useCallback } from "react";
import styles from "./ppt_home.module.css";

const Desktop6 = () => {
  const onDesktop6Click = useCallback(() => {
    // Please sync "Desktop - 7" to the project
  }, []);

  return (
    <div className={styles.desktop6} onClick={onDesktop6Click}>
      <div className={styles.login1}>
        <div className={styles.login1Inner}>
          <div className={styles.groupWrapper}>
            <div className={styles.groupWrapper}>
              <div className={styles.skkuPptMaker}>SKKU PPT Maker</div>
              <div className={styles.createSimply}>{`Create simply `}</div>
            </div>
          </div>
        </div>
        <div className={styles.instanceParent}>
          <div className={styles.groupContainer}>
            <div className={styles.rectangleParent}>
              <div className={styles.groupChild} />
              <div className={styles.login}>submit</div>
            </div>
          </div>
          <div className={styles.makeAPpt}>Make a PPT</div>
        </div>
        <div className={styles.div}>
          <img className={styles.skkuIm1} alt="" src="/skku-im-1@2x.png" />
        </div>
        <div className={styles.home}>home</div>
        <input className={styles.component1} placeholder="Topic" />
        <input
          className={styles.component11}
          placeholder="Detail"
          
        />
        <input
          className={styles.component12}
          placeholder="API KEY"
          
        />
      </div>
    </div>
  );
};

export default Desktop6;

