import Layout from '../components/layout'
import { getCookie } from 'cookies-next';
import Link from 'next/link'
import styles from "./index.module.css";

const Desktop1 = ({ username }) => {
  return (
    <Layout pageTitle="Home">
      {username ? (
        <>
          <div className={styles.desktop1}>
          <div className={styles.login1}>
            <div className={styles.login1Inner}>
              <div className={styles.groupWrapper}>
                <div className={styles.skkuPptMaker}>SKKU PPT Maker</div>
                <div className={styles.createSimply}>Create simply</div>
              </div>
            </div>
            <div className={styles.groupParent}>
              <div className={styles.orWrapper}>
                <div className={styles.or}> or</div>
              </div>
              <Link href="/profile">
                <div className={`${styles.signInButton} ${styles.iconsParent}`}>
                  <img className={styles.icons} alt="" src="/icons.svg" />
                  <div className={styles.signUp}>profile</div>
                </div>
              </Link>
              <Link href="/profile">
                <div className={`${styles.signInButton} ${styles.iconsParent}`}>
                  <img className={styles.icons} alt="" src="/icons.svg" />
                  <div className={styles.signUp}>profile</div>
                </div>
              </Link>
              <Link href="/api/logout">
                <div className={`${styles.signUpButton} ${styles.iconsGroup}`}>
                  <img className={styles.icons} alt="" src="/icons1.svg" />
                  <div className={styles.signUp}>logout</div>
                </div>
              </Link>
            </div>
            <div className={styles.div}>
              <img className={styles.skkuIm1} alt="" src="/skku-im-1@2x.png" />
            </div>
          </div>
        </div>
        </>
      ) : (
        <div className={styles.desktop1}>
          <div className={styles.login1}>
            <div className={styles.login1Inner}>
              <div className={styles.groupWrapper}>
                <div className={styles.skkuPptMaker}>SKKU PPT Maker</div>
                <div className={styles.createSimply}>Create simply</div>
              </div>
            </div>
            <div className={styles.groupParent}>
              <div className={styles.orWrapper}>
                <div className={styles.or}> or</div>
              </div>
              <Link href="/signup">
                <div className={`${styles.signInButton} ${styles.iconsParent}`}>
                  <img className={styles.icons} alt="" src="/icons.svg" />
                  <div className={styles.signUp}>Sign up</div>
                </div>
              </Link>
              <Link href="/login">
                <div className={`${styles.signUpButton} ${styles.iconsGroup}`}>
                  <img className={styles.icons} alt="" src="/icons1.svg" />
                  <div className={styles.signUp}>Sign in</div>
                </div>
              </Link>
            </div>
            <div className={styles.div}>
              <img className={styles.skkuIm1} alt="" src="/skku-im-1@2x.png" />
            </div>
          </div>
        </div>
      )}
    </Layout>
  );
};

export default Desktop1;

export async function getServerSideProps(context) {
    const req = context.req;
    const res = context.res;
    var username = getCookie('username', { req, res });
    if (username === undefined) {
        username = false;
    }
    return { props: {username} };
};

