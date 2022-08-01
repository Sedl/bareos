<?php

// autoload_real.php @generated by Composer

class ComposerAutoloaderInit6df5b8a1471c61873b9f5b638848d4d7
{
    private static $loader;

    public static function loadClassLoader($class)
    {
        if ('Composer\Autoload\ClassLoader' === $class) {
            require __DIR__ . '/ClassLoader.php';
        }
    }

    /**
     * @return \Composer\Autoload\ClassLoader
     */
    public static function getLoader()
    {
        if (null !== self::$loader) {
            return self::$loader;
        }

        spl_autoload_register(array('ComposerAutoloaderInit6df5b8a1471c61873b9f5b638848d4d7', 'loadClassLoader'), true, true);
        self::$loader = $loader = new \Composer\Autoload\ClassLoader(\dirname(__DIR__));
        spl_autoload_unregister(array('ComposerAutoloaderInit6df5b8a1471c61873b9f5b638848d4d7', 'loadClassLoader'));

        require __DIR__ . '/autoload_static.php';
        call_user_func(\Composer\Autoload\ComposerStaticInit6df5b8a1471c61873b9f5b638848d4d7::getInitializer($loader));

        $loader->register(true);

        return $loader;
    }
}
