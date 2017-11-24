
lib = File.expand_path("../lib", __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require "discord_logger/version"

Gem::Specification.new do |spec|
  spec.name          = "discord_logger"
  spec.version       = DiscordLogger::VERSION
  spec.authors       = ["Andrea Pascal"]
  spec.email         = ["andrea@anodium.net"]
  spec.license       = 'MIT'

  spec.summary       = "Log Discord conversations to a file"
  spec.homepage      = "https://github.com/anodium/discord_logger"

  spec.files         = `git ls-files -z`.split("\x0").reject do |f|
    f.match(%r{^(test|spec|features)/})
  end
  spec.bindir        = "exe"
  spec.executables   = spec.files.grep(%r{^exe/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.16"
  spec.add_development_dependency "rake", "~> 10.0"
  spec.add_development_dependency "rspec", "~> 3.0"

  spec.add_runtime_dependency 'discordrb', '~> 3.2', '>= 3.2.1'
end
