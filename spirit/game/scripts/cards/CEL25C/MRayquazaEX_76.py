from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ef04ca94-67d1-5c36-828b-2123f9180b39",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MRayquazaEX.Name",
    display_name="M Rayquaza-EX",
    searchable_by=["M Rayquaza-EX", "MEGA", "EX", "MRayquazaEX"],
    subtypes=["MEGA", "EX"],
    collector_number=76,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    family_id=384,
    abilities=[
        Attack(
            title="Emerald Break",
            game_text="This attack does 30 damage times the number of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)