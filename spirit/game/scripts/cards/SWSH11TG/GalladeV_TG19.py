from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="645d064d-75a0-59f9-bddf-a214a81bfb19",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeV.Name",
    display_name="Gallade V",
    searchable_by=["Gallade V", "Basic", "V", "GalladeV"],
    subtypes=["Basic", "V"],
    collector_number=19,
    set_code="SWSH11TG",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=475,
    abilities=[
        Attack(
            title="Rising Sword",
            game_text="This attack does 50 more damage for each Prize card you have taken.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Buster Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)