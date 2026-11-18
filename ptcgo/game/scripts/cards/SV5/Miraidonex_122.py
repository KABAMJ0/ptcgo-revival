from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a35e541a-9ed0-5af1-8dad-63d79df39be5",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex", "Basic", "ex", "Future", "Miraidonex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=122,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=1008,
    abilities=[
        Attack(
            title="Repulsion Bolt",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Cyber Drive",
            game_text="During your next turn, this Pok\u00e9mon can't use Cyber Drive.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=unimplemented,
        ),
    ],
)