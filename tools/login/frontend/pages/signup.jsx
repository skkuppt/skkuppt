import Layout from '../components/layout'
import { getCookie } from 'cookies-next';
import Link from 'next/link'
import { useRouter } from 'next/router'
import styles from "./signup.module.css";

const Desktop5 = () => {
  return (
  <form action='/api/signup' method='POST'>
    <div className={styles.desktop5}>
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
            <div className={styles}>
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
            <div className={styles.rectangleGroup}>
              <div className={styles.rectangleGroup}>
                <div className={styles.groupItem} />
                <div className={styles.password}>
                <input 
                  type="text" 
                  id = "password"
                  name="password" 
                  placeholder="Enter your password" 
                  required 
                  className={styles} 
                /></div>
              </div>
            </div>
          </div>
          <div className={styles.groupWrapper2}>
            <div className={styles.groupFrame}>
              <div className={styles.groupInner} />
              <input type="submit" value="Signup" className = {styles.groupInner}/><br/></div>
            
          </div>
          <div className={styles.signUp}>Sign up</div>
          <div className={styles.groupWrapper3}>
            <div className={styles.rectangleGroup}>
              <div className={styles.rectangleGroup}>
                <div className={styles.groupItem} />
                <div className={styles.password}>
                <input 
                  type="text" 
                  name="passwordagain"
                  id = "passwordagain" 
                  placeholder="Enter your password again" 
                  required 
                  className={styles} 
                /></div>
              </div>
              <div className={styles.invisible1} />
            </div>
          </div>
          <div className={styles.groupWrapper4}>
            <div className={styles.rectangleGroup}>
              <div className={styles.rectangleGroup}>
                <div className={styles.groupItem} />
                <div className={styles.emailValidation}><input 
                  type="text" 
                  name="email"
                  id = "email" 
                  placeholder="Enter your email" 
                  required 
                  className={styles.input} // 스타일을 위한 클래스
                /></div>
              </div>
            </div>
          </div>
          <div className={styles.groupWrapper6}>
            <div className={styles.groupWrapper7}>
              <div className={styles.groupWrapper7}>
                <div className={styles.validation} />
                
                <input type="submit" value="validation" className = {styles.groupWrapper7}/><br/>
                </div>
             
            </div>
          </div>
        </div>
        <div className={styles.div}>
          <img className={styles.skkuIm1} alt="" src="/skku-im-1@2x.png" />
        </div>
        <div className={styles.home}>home</div>
      </div>
    </div>
    </form>
  );
};

export default Desktop5;


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
