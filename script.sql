CREATE TABLE `character_attributes` (
			`char_name` varchar(100) NOT NULL,
			`alignment` varchar(10) NULL,
			`intelligence` int NULL,
			`strength` int NULL,
			`speed` int NULL,
			`durability` int NULL,
			`power` int NULL,
			`combat` int NULL,
			`total` int NULL,
			`gender` varchar(20) NULL,
			`eyecolor` varchar(50) NULL,
			`race` varchar(50) NULL,
			`haircolor` varchar(20) NULL,
			`skincolor` varchar(20) NULL,
			`height` float NULL,
			`weight` float NULL
			);


CREATE TABLE `character_power_matrix` (
		`char_name` varchar(100) not null,
		`agility` varchar(10) null,
		`accelerated_healing` varchar(10) null,
		`lantern_power_ring` varchar(10) null,
		`dimensional_awareness` varchar(10) null,
		`cold_resistance` varchar(10) null,
		`durability` varchar(10) null,
		`stealth` varchar(10) null,
		`energy_absorption` varchar(10) null,
		`flight` varchar(10) null,
		`danger_sense` varchar(10) null,
		`underwater_breathing` varchar(10) null,
		`marksmanship` varchar(10) null,
		`weapons_master` varchar(10) null,
		`power_augmentation` varchar(10) null,
		`animal_attributes` varchar(10) null,
		`longevity` varchar(10) null,
		`intelligence` varchar(10) null,
		`super_strength` varchar(10) null,
		`cryokinesis` varchar(10) null,
		`telepathy` varchar(10) null,
		`energy_armor` varchar(10) null,
		`energy_blasts` varchar(10) null,
		`duplication` varchar(10) null,
		`size_changing` varchar(10) null,
		`density_control` varchar(10) null,
		`stamina` varchar(10) null,
		`astral_travel` varchar(10) null,
		`audio_control` varchar(10) null,
		`dexterity` varchar(10) null,
		`omnitrix` varchar(10) null,
		`super_speed` varchar(10) null,
		`possession` varchar(10) null,
		`animal_oriented_powers` varchar(10) null,
		`weapon-based_powers` varchar(10) null,
		`electrokinesis` varchar(10) null,
		`darkforce_manipulation` varchar(10) null,
		`death_touch` varchar(10) null,
		`teleportation` varchar(10) null,
		`enhanced_senses` varchar(10) null,
		`telekinesis` varchar(10) null,
		`energy_beams` varchar(10) null,
		`magic` varchar(10) null,
		`hyperkinesis` varchar(10) null,
		`jump` varchar(10) null,
		`clairvoyance` varchar(10) null,
		`dimensional_travel` varchar(10) null,
		`power_sense` varchar(10) null,
		`shapeshifting` varchar(10) null,
		`peak_human_condition` varchar(10) null,
		`immortality` varchar(10) null,
		`camouflage` varchar(10) null,
		`element_control` varchar(10) null,
		`phasing` varchar(10) null,
		`astral_projection` varchar(10) null,
		`electrical_transport` varchar(10) null,
		`fire_control` varchar(10) null,
		`projection` varchar(10) null,
		`summoning` varchar(10) null,
		`enhanced_memory` varchar(10) null,
		`reflexes` varchar(10) null,
		`invulnerability` varchar(10) null,
		`energy_constructs` varchar(10) null,
		`force_fields` varchar(10) null,
		`self-sustenance` varchar(10) null,
		`anti-gravity` varchar(10) null,
		`empathy` varchar(10) null,
		`power_nullifier` varchar(10) null,
		`radiation_control` varchar(10) null,
		`psionic_powers` varchar(10) null,
		`elasticity` varchar(10) null,
		`substance_secretion` varchar(10) null,
		`elemental_transmogrification` varchar(10) null,
		`technopath/cyberpath` varchar(10) null,
		`photographic_reflexes` varchar(10) null,
		`seismic_power` varchar(10) null,
		`animation` varchar(10) null,
		`precognition` varchar(10) null,
		`mind_control` varchar(10) null,
		`fire_resistance` varchar(10) null,
		`power_absorption` varchar(10) null,
		`enhanced_hearing` varchar(10) null,
		`nova_force` varchar(10) null,
		`insanity` varchar(10) null,
		`hypnokinesis` varchar(10) null,
		`animal_control` varchar(10) null,
		`natural_armor` varchar(10) null,
		`intangibility` varchar(10) null,
		`enhanced_sight` varchar(10) null,
		`molecular_manipulation` varchar(10) null,
		`heat_generation` varchar(10) null,
		`adaptation` varchar(10) null,
		`gliding` varchar(10) null,
		`power_suit` varchar(10) null,
		`mind_blast` varchar(10) null,
		`probability_manipulation` varchar(10) null,
		`gravity_control` varchar(10) null,
		`regeneration` varchar(10) null,
		`light_control` varchar(10) null,
		`echolocation` varchar(10) null,
		`levitation` varchar(10) null,
		`toxin_and_disease_control` varchar(10) null,
		`banish` varchar(10) null,
		`energy_manipulation` varchar(10) null,
		`heat_resistance` varchar(10) null,
		`natural_weapons` varchar(10) null,
		`time_travel` varchar(10) null,
		`enhanced_smell` varchar(10) null,
		`illusions` varchar(10) null,
		`thirstokinesis` varchar(10) null,
		`hair_manipulation` varchar(10) null,
		`illumination` varchar(10) null,
		`omnipotent` varchar(10) null,
		`cloaking` varchar(10) null,
		`changing_armor` varchar(10) null,
		`power_cosmic` varchar(10) null,
		`biokinesis` varchar(10) null,
		`water_control` varchar(10) null,
		`radiation_immunity` varchar(10) null,
		`vision_-_telescopic` varchar(10) null,
		`toxin_and_disease_resistance` varchar(10) null,
		`spatial_awareness` varchar(10) null,
		`energy_resistance` varchar(10) null,
		`telepathy_resistance` varchar(10) null,
		`molecular_combustion` varchar(10) null,
		`omnilingualism` varchar(10) null,
		`portal_creation` varchar(10) null,
		`magnetism` varchar(10) null,
		`mind_control_resistance` varchar(10) null,
		`plant_control` varchar(10) null,
		`sonar` varchar(10) null,
		`sonic_scream` varchar(10) null,
		`time_manipulation` varchar(10) null,
		`enhanced_touch` varchar(10) null,
		`magic_resistance` varchar(10) null,
		`invisibility` varchar(10) null,
		`sub-mariner` varchar(10) null,
		`radiation_absorption` varchar(10) null,
		`intuitive_aptitude` varchar(10) null,
		`vision_-_microscopic` varchar(10) null,
		`melting` varchar(10) null,
		`wind_control` varchar(10) null,
		`super_breath` varchar(10) null,
		`wallcrawling` varchar(10) null,
		`vision_-_night` varchar(10) null,
		`vision_-_infrared` varchar(10) null,
		`grim_reaping` varchar(10) null,
		`matter_absorption` varchar(10) null,
		`the_force` varchar(10) null,
		`resurrection` varchar(10) null,
		`terrakinesis` varchar(10) null,
		`vision_-_heat` varchar(10) null,
		`vitakinesis` varchar(10) null,
		`radar_sense` varchar(10) null,
		`qwardian_power_ring` varchar(10) null,
		`weather_control` varchar(10) null,
		`vision_-_x-ray` varchar(10) null,
		`vision_-_thermal` varchar(10) null,
		`web_creation` varchar(10) null,
		`reality_warping` varchar(10) null,
		`odin_force` varchar(10) null,
		`symbiote_costume` varchar(10) null,
		`speed_force` varchar(10) null,
		`phoenix_force` varchar(10) null,
		`molecular_dissipation` varchar(10) null,
		`vision_-_cryo` varchar(10) null,
		`omnipresent` varchar(10) null,
		`omniscient` varchar(10) null
		);


CREATE TABLE `character_comics` (
		`char_name` varchar(100) not null,
		`comics_title` varchar(150) null,
		`issue_number` int null,
		`description` varchar(3000) null
		);


CREATE TABLE `character_variation` (
		`name` varchar(100) null,
		`identity` varchar(50) null,
		`alignment` varchar(20) null,
		`eyecolor` varchar(20) null,
		`haircolor` varchar(20) null,
		`gender` varchar(20) null,
		`status` varchar(20) null,
		`appearances` int null,
		`firstappearance` datetime null,
		`year` int null,
		`universe` varchar(20) null,
		`char_name` varchar(100) null
		);