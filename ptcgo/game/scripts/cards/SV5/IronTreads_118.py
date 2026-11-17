from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="14be13a1-b105-5bc2-8ebf-bdd61641c480",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronTreads.Name",
    display_name="Iron Treads",
    searchable_by=["Iron Treads", "Basic", "Future", "IronTreads"],
    subtypes=["Basic", "Future"],
    collector_number=118,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=990,
    abilities=[
        Ability(
            title="Dual Core",
            game_text="As long as this Pok\u00e9mon has a Future Booster Energy Capsule attached, it is Fighting and Metal type.",
            effect=unimplemented,
        ),
        Attack(
            title="Wheel Pass",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)