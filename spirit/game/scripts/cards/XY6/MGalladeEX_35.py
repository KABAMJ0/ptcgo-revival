from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1cc79d5d-1c4c-5a99-9438-958001b90689",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGalladeEX.Name",
    display_name="M Gallade-EX",
    searchable_by=["M Gallade-EX", "MEGA", "EX", "MGalladeEX"],
    subtypes=["MEGA", "EX"],
    collector_number=35,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeEX.Name",
    family_id=475,
    abilities=[
        Attack(
            title="Unwavering Blade",
            game_text="This attack does 30 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=unimplemented,
        ),
    ],
)