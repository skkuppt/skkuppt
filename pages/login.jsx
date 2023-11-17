import Layout from '../components/layout'
import { getCookie } from 'cookies-next';
import Link from 'next/link'
import { useRouter } from 'next/router'

import styles from "./login.module.css";

const Desktop2 = () => {
  return (
  <form action='/api/login' method='POST'>
    <div className={styles.desktop2}>
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
            <div className={styles.groupFrame}>
              <div className={styles.groupFrame}>
                <div className={styles.groupChild} />
                <div className={styles.enterEmailOr}>
                  <input 
                  type="text" 
                  name="username"
                  id = "username"
                  placeholder="Enter your id(email)" 
                  required 
                  className={styles.groupChild}
                />
                </div>
              </div>
            </div>
          </div>
          <div className={styles.groupDiv}>
            <div className={styles.groupParent}>
              <div className={styles.groupParent}>
                <div className={styles.groupItem} />
                <div className={styles.password}>
                <input 
                  type="text" 
                  id = "password"
                  name="password" 
                  placeholder="Enter your password" 
                  required 
                  className={styles.password} 
                /></div>
              </div>
              
            </div>
          </div>
          <div className={styles.groupWrapper1}>
            <div className={styles.groupFrame}>
              <div className={styles.groupInner} />
              
              <input type="submit" value="login" className = {styles.groupInner}/></div>
           
          </div>
          <div className={styles.signIn}>Sign in</div>
        </div>
        <div className={styles.div}>
          <img className={styles.skkuIm1} alt="" src="/skku-im-1@2x.png" />
        </div>
        <div className={styles.home}>home</div>
        <div className={styles.component1}>
          <div className={styles.button}>home</div>
        </div>
      </div>
    </div>
    </form>
  );
};

export default Desktop2;


export async function getServerSideProps(context) {
    const req = context.req
    const res = context.res
    var username = getCookie('username', { req, res });
    if (username != undefined){
        return {
            redirect: {
                permanent: false,
                destination: "/"
            }
        }
    }
    return { props: {username:false} };
};

