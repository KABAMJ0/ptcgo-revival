from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b3f35c05-a72e-538a-926c-fa52aeb6d2a6",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronTreadsex.Name",
    display_name="Iron Treads ex",
    searchable_by=["Iron Treads ex", "Basic", "ex", "IronTreadsex"],
    subtypes=["Basic", "ex"],
    collector_number=248,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=990,
    abilities=[
        Attack(
            title="Triple Laser",
            game_text="This attack does 30 damage to 3 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
        Attack(
            title="Cybernetic Wheels",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)