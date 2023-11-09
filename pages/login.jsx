import Layout from '../components/layout'
import { getCookie } from 'cookies-next';
import Link from 'next/link'
import { useRouter } from 'next/router'
import styles from "./login.module.css"; 

export default function LoginPage({ username }) {
  const router = useRouter();
  const { msg } = router.query;

  return (
    <Layout pageTitle="Login">
      <div className={styles.desktop2}>
        <div className={styles.login1}>
          <div className={styles.login1Inner}>
            <div className={styles.groupWrapper}>
              <div className={styles.skkuPptMaker}>SKKU PPT Maker</div>
              <div className={styles.createSimply}>Create simply</div>
            </div>
          </div>
          <div className={styles.instanceParent}>
            <form action='/api/login' method='POST'> {/* Form을 추가합니다. */}
              <div className={styles.groupContainer}>
                <div className={styles.groupFrame}>
                  <input
                    className={styles.groupChild}
                    type="text"
                    name="username"
                    placeholder='Enter email or user name'
                    required
                  />
                </div>
              </div>
              <div className={styles.groupDiv}>
                <div className={styles.groupParent}>
                  <input
                    className={styles.groupItem}
                    type="password"
                    name="password"
                    placeholder='Password'
                    required
                  />
                  <img
                    className={styles.invisible1Icon}
                    alt="Show Password"
                    src="/invisible-1.svg"
                  />
                </div>
              </div>
              <div className={styles.groupWrapper1}>
                <button type="submit" className={styles.groupInner}>
                  Login
                </button>
              </div>
            </form>
            <div className={styles.signIn}>Sign in</div>
          </div>
          <Link href="/" className={styles.home}>
            home
          </Link>
          <div className={styles.div}>
            <img className={styles.skkuIm1} alt="SKKU Image" src="/skku-im-1@2x.png" />
          </div>
          <div className={styles.component1}>
            <div className={styles.button}>home</div>
          </div>
        </div>
      </div>
    </Layout>
  );
}

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
